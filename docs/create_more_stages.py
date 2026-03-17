#!/usr/bin/env python3
"""Create additional ES|QL stage files for colors and airport_city_boundaries."""
import csv
import io
import json
from pathlib import Path

FIXTURES = Path("/Users/georgewallace/elastic-repos/elasticsearch/x-pack/plugin/esql/qa/testFixtures/src/main/resources")
STAGES_DIR = Path("/Users/georgewallace/elastic-repos/exemplipy/src/exemplipy/stages")


def parse_esql_csv(csv_path, skip_dot_fields=True):
    text = csv_path.read_text(encoding="utf-8")
    reader = csv.reader(io.StringIO(text))
    rows = list(reader)
    if not rows:
        return [], []

    header = rows[0]
    fields = []
    seen_names = set()
    for col in header:
        col = col.strip()
        if ":" in col:
            name, ftype = col.rsplit(":", 1)
            name = name.strip()
            ftype = ftype.strip()
        else:
            name, ftype = col, "keyword"
        if skip_dot_fields and "." in name:
            fields.append(None)
            continue
        if name in seen_names:
            fields.append(None)
            continue
        seen_names.add(name)
        fields.append((name, ftype))

    data_rows = []
    for row in rows[1:]:
        if not row or all(v.strip() == "" for v in row):
            continue
        doc = {}
        for i, f in enumerate(fields):
            if f is None or i >= len(row):
                continue
            name, ftype = f
            val = row[i].strip()
            if val.startswith("[") and val.endswith("]"):
                inner = val[1:-1]
                val = [v.strip() for v in inner.split(",")] if inner else []
            elif ftype in ("integer", "long", "short", "byte"):
                try: val = int(val)
                except: pass
            elif ftype in ("double", "float"):
                try: val = float(val)
                except: pass
            elif ftype == "boolean":
                val = val.lower() in ("true", "1")
            if val != "" and val != []:
                doc[name] = val
        data_rows.append(doc)
    return [(f[0], f[1]) for f in fields if f is not None], data_rows


def indent(text, spaces=8):
    pad = " " * spaces
    return "\n".join(pad + line if line.strip() else line for line in text.splitlines())


def write_stage(name, setup_code, teardown_code):
    stage = f"""setup:
  - action:
      kind: ELASTIC_CONSOLE_CODE
      code: |
{indent(setup_code, 8)}

teardown:
  - action:
      kind: ELASTIC_CONSOLE_CODE
      code: |
{indent(teardown_code, 8)}
"""
    out = STAGES_DIR / f"{name}.yaml"
    out.write_text(stage, encoding="utf-8")
    print(f"  Written: {out.name}")


def create_colors_stage():
    print("Creating colors stage...")
    # colors_cmyk.csv - skip rgb_vector and rgb_byte_vector (dense_vector, complex)
    fields, docs = parse_esql_csv(FIXTURES / "data/colors_cmyk.csv")
    mapping = {
        "id": {"type": "integer"},
        "color": {"type": "text"},
        "hex_code": {"type": "keyword"},
        "primary": {"type": "boolean"},
    }
    mapping_json = json.dumps({"mappings": {"properties": mapping}}, indent=2)
    bulk_lines = []
    for doc in docs:
        filtered = {k: v for k, v in doc.items() if k in mapping}
        bulk_lines.append(json.dumps({"index": {}}))
        bulk_lines.append(json.dumps(filtered))
    bulk_body = "\n".join(bulk_lines)
    setup = f"PUT colors\n{mapping_json}\n\nPOST colors/_bulk?refresh\n{bulk_body}"
    teardown = "DELETE colors?ignore_unavailable=true"
    write_stage("colors", setup, teardown)
    print(f"  Indexed {len(docs)} colors")


def create_airport_city_boundaries_stage():
    print("Creating airport_city_boundaries stage...")
    fields, docs = parse_esql_csv(FIXTURES / "data/airport_city_boundaries.csv")
    mapping = json.loads((FIXTURES / "mapping-airport_city_boundaries.json").read_text())
    index_json = json.dumps({"mappings": mapping}, indent=2)
    bulk_lines = []
    for doc in docs:
        bulk_lines.append(json.dumps({"index": {}}))
        bulk_lines.append(json.dumps(doc))
    bulk_body = "\n".join(bulk_lines)
    setup = f"PUT airport_city_boundaries\n{index_json}\n\nPOST airport_city_boundaries/_bulk?refresh\n{bulk_body}"
    teardown = "DELETE airport_city_boundaries?ignore_unavailable=true"
    write_stage("airport_city_boundaries", setup, teardown)
    print(f"  Indexed {len(docs)} airport_city_boundaries docs")


if __name__ == "__main__":
    create_colors_stage()
    create_airport_city_boundaries_stage()
    print("\nDone.")
