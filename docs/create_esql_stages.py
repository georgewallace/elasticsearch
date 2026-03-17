#!/usr/bin/env python3
"""
Create exemplipy stage YAML files for ES|QL sample datasets.
Converts the CSV fixture files into inline bulk indexing operations.
"""
import csv
import io
import json
import re
from pathlib import Path

FIXTURES = Path("/Users/georgewallace/elastic-repos/elasticsearch/x-pack/plugin/esql/qa/testFixtures/src/main/resources")
STAGES_DIR = Path("/Users/georgewallace/elastic-repos/exemplipy/stages")

# Type mapping from CSV type hints to ES field types
TYPE_MAP = {
    "keyword": "keyword",
    "text": "text",
    "integer": "integer",
    "long": "long",
    "short": "short",
    "byte": "byte",
    "double": "double",
    "float": "float",
    "half_float": "half_float",
    "scaled_float": "scaled_float",
    "boolean": "boolean",
    "date": "date",
    "ip": "ip",
    "geo_point": "geo_point",
    "geo_shape": "geo_shape",
    "unsigned_long": "unsigned_long",
}


def parse_csv_value(value, field_type):
    """Parse a single CSV value, handling multi-values and type conversion."""
    value = value.strip()

    # Handle multi-value: [val1,val2] -> list
    if value.startswith("[") and value.endswith("]"):
        inner = value[1:-1]
        if inner == "":
            return []
        # Split on comma but respect nested brackets
        parts = split_mv(inner)
        return [parse_single_value(p.strip(), field_type) for p in parts]

    return parse_single_value(value, field_type)


def split_mv(s):
    """Split multi-value string by comma, respecting nesting."""
    parts = []
    depth = 0
    current = []
    for ch in s:
        if ch == "[":
            depth += 1
            current.append(ch)
        elif ch == "]":
            depth -= 1
            current.append(ch)
        elif ch == "," and depth == 0:
            parts.append("".join(current))
            current = []
        else:
            current.append(ch)
    if current:
        parts.append("".join(current))
    return parts


def parse_single_value(value, field_type):
    """Convert a string value to the appropriate Python type."""
    if value == "" or value == "null":
        return None
    if field_type in ("integer", "long", "short", "byte", "unsigned_long"):
        try:
            return int(value)
        except ValueError:
            return value
    if field_type in ("double", "float", "half_float", "scaled_float"):
        try:
            return float(value)
        except ValueError:
            return value
    if field_type == "boolean":
        return value.lower() in ("true", "1", "yes")
    return value


def parse_esql_csv(csv_path):
    """Parse an ES|QL test fixture CSV file.
    Returns (fields, rows) where fields is list of (name, type) tuples.
    Skips dot-notation sub-fields (duplicates of parent with different type).
    """
    text = csv_path.read_text(encoding="utf-8")
    reader = csv.reader(io.StringIO(text))
    rows = list(reader)
    if not rows:
        return [], []

    # Parse header: "field_name:type" with possible whitespace
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
            name = col
            ftype = "keyword"
        # Skip dot-notation sub-fields (e.g., languages.long, height.float)
        if "." in name:
            fields.append(None)  # placeholder to keep column alignment
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
        for i, field_spec in enumerate(fields):
            if field_spec is None:
                continue
            if i >= len(row):
                continue
            name, ftype = field_spec
            val = parse_csv_value(row[i], ftype)
            if val is not None and val != []:
                doc[name] = val
        data_rows.append(doc)
    return [(f[0], f[1]) for f in fields if f is not None], data_rows


def build_mapping(fields, extra_props=None):
    """Build ES mapping properties from field list."""
    props = {}
    for name, ftype in fields:
        es_type = TYPE_MAP.get(ftype, "keyword")
        if es_type == "scaled_float":
            props[name] = {"type": "scaled_float", "scaling_factor": 100}
        elif es_type in ("text",):
            props[name] = {"type": "text", "fields": {"keyword": {"type": "keyword"}}}
        else:
            props[name] = {"type": es_type}
    if extra_props:
        props.update(extra_props)
    return props


def bulk_ndjson(index, docs):
    """Generate _bulk NDJSON lines."""
    lines = []
    for doc in docs:
        lines.append(json.dumps({"index": {"_index": index}}))
        lines.append(json.dumps(doc))
    return "\n".join(lines)


def indent(text, spaces=8):
    pad = " " * spaces
    return "\n".join(pad + line if line.strip() else line for line in text.splitlines())


def write_stage(name, setup_code, teardown_code, description=""):
    """Write a stage YAML file."""
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
    print(f"  Written: {out}")


def create_employees_stage():
    print("Creating employees stage...")
    fields, docs = parse_esql_csv(FIXTURES / "data/employees.csv")
    # Use the mapping that matches what ES|QL tests expect
    mapping_props = {
        "birth_date": {"type": "date"},
        "emp_no": {"type": "integer"},
        "first_name": {"type": "keyword"},
        "gender": {"type": "keyword"},
        "hire_date": {"type": "date"},
        "languages": {"type": "integer"},
        "last_name": {"type": "keyword"},
        "salary": {"type": "integer"},
        "height": {"type": "double"},
        "still_hired": {"type": "boolean"},
        "avg_worked_seconds": {"type": "long"},
        "job_positions": {"type": "keyword"},
        "is_rehired": {"type": "boolean"},
        "salary_change": {"type": "double"},
    }

    mapping_json = json.dumps({"mappings": {"properties": mapping_props}}, indent=2)

    # Build bulk from only the core fields
    core_fields = set(mapping_props.keys())
    bulk_lines = []
    for doc in docs:
        filtered = {k: v for k, v in doc.items() if k in core_fields}
        bulk_lines.append(json.dumps({"index": {}}))
        bulk_lines.append(json.dumps(filtered))
    bulk_body = "\n".join(bulk_lines)

    setup = f"PUT employees\n{mapping_json}\n\nPOST employees/_bulk?refresh\n{bulk_body}"
    teardown = "DELETE employees?ignore_unavailable=true"
    write_stage("employees", setup, teardown)
    print(f"  Indexed {len(docs)} employees")


def create_sample_data_stage():
    print("Creating sample_data stage...")
    fields, docs = parse_esql_csv(FIXTURES / "data/sample_data.csv")
    mapping_props = {
        "@timestamp": {"type": "date"},
        "client_ip": {"type": "ip"},
        "event_duration": {"type": "long"},
        "message": {"type": "keyword"},
    }
    mapping_json = json.dumps({"mappings": {"properties": mapping_props}}, indent=2)
    bulk_lines = []
    for doc in docs:
        # rename @timestamp
        bulk_lines.append(json.dumps({"index": {}}))
        bulk_lines.append(json.dumps(doc))
    bulk_body = "\n".join(bulk_lines)
    setup = f"PUT sample_data\n{mapping_json}\n\nPOST sample_data/_bulk?refresh\n{bulk_body}"
    teardown = "DELETE sample_data?ignore_unavailable=true"
    write_stage("sample_data", setup, teardown)
    print(f"  Indexed {len(docs)} sample_data docs")


def create_hosts_stage():
    print("Creating hosts stage...")
    fields, docs = parse_esql_csv(FIXTURES / "data/hosts.csv")
    mapping_props = {
        "host": {"type": "keyword"},
        "host_group": {"type": "text"},
        "description": {"type": "text"},
        "card": {"type": "keyword"},
        "ip0": {"type": "ip"},
        "ip1": {"type": "ip"},
    }
    mapping_json = json.dumps({"mappings": {"properties": mapping_props}}, indent=2)
    bulk_lines = []
    for doc in docs:
        bulk_lines.append(json.dumps({"index": {}}))
        bulk_lines.append(json.dumps(doc))
    bulk_body = "\n".join(bulk_lines)
    setup = f"PUT hosts\n{mapping_json}\n\nPOST hosts/_bulk?refresh\n{bulk_body}"
    teardown = "DELETE hosts?ignore_unavailable=true"
    write_stage("hosts", setup, teardown)
    print(f"  Indexed {len(docs)} hosts")


def create_languages_stage():
    print("Creating languages_lookup stage...")
    fields, docs = parse_esql_csv(FIXTURES / "data/languages.csv")
    mapping_props = {
        "language_code": {"type": "integer"},
        "language_name": {"type": "keyword"},
    }
    mapping_json = json.dumps({"mappings": {"properties": mapping_props}}, indent=2)
    bulk_lines = []
    for doc in docs:
        bulk_lines.append(json.dumps({"index": {}}))
        bulk_lines.append(json.dumps(doc))
    bulk_body = "\n".join(bulk_lines)
    setup = f"PUT languages_lookup\n{mapping_json}\n\nPOST languages_lookup/_bulk?refresh\n{bulk_body}"
    teardown = "DELETE languages_lookup?ignore_unavailable=true"
    write_stage("languages_lookup", setup, teardown)
    print(f"  Indexed {len(docs)} languages")


def create_books_stage():
    print("Creating books stage...")
    fields, docs = parse_esql_csv(FIXTURES / "data/books.csv")

    # Read extra settings (for dense_vector dims etc.) if present
    settings_path = FIXTURES / "books-settings.json"
    settings = json.loads(settings_path.read_text()) if settings_path.exists() else {}

    mapping_path = FIXTURES / "mapping-books.json"
    mapping = json.loads(mapping_path.read_text()) if mapping_path.exists() else {}

    index_body = {}
    if settings:
        index_body["settings"] = settings
    if mapping:
        index_body["mappings"] = mapping

    index_json = json.dumps(index_body, indent=2) if index_body else "{}"

    bulk_lines = []
    for doc in docs:
        bulk_lines.append(json.dumps({"index": {}}))
        bulk_lines.append(json.dumps(doc))
    bulk_body = "\n".join(bulk_lines)
    setup = f"PUT books\n{index_json}\n\nPOST books/_bulk?refresh\n{bulk_body}"
    teardown = "DELETE books?ignore_unavailable=true"
    write_stage("books", setup, teardown)
    print(f"  Indexed {len(docs)} books")


def create_airports_stage():
    print("Creating airports stage...")
    fields, docs = parse_esql_csv(FIXTURES / "data/airports.csv")

    mapping_path = FIXTURES / "mapping-airports.json"
    mapping = json.loads(mapping_path.read_text()) if mapping_path.exists() else {}
    index_json = json.dumps({"mappings": mapping}, indent=2)

    bulk_lines = []
    for doc in docs:
        bulk_lines.append(json.dumps({"index": {}}))
        bulk_lines.append(json.dumps(doc))
    bulk_body = "\n".join(bulk_lines)
    setup = f"PUT airports\n{index_json}\n\nPOST airports/_bulk?refresh\n{bulk_body}"
    teardown = "DELETE airports?ignore_unavailable=true"
    write_stage("airports", setup, teardown)
    print(f"  Indexed {len(docs)} airports")


def main():
    STAGES_DIR.mkdir(exist_ok=True)
    create_employees_stage()
    create_sample_data_stage()
    create_hosts_stage()
    create_languages_stage()
    create_books_stage()
    create_airports_stage()
    print("\nDone! Stage files written to:", STAGES_DIR)


if __name__ == "__main__":
    main()
