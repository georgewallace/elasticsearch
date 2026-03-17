#!/usr/bin/env python3
"""
Patch stage: into existing ES|QL test YAML files based on which index the query uses.
Also adds annotation comments to non-generated markdown files.
"""
import re
import sys
from pathlib import Path

EXAMPLES_DIR = Path("/Users/georgewallace/elastic-repos/elasticsearch/docs/examples")
DOCS_REF = Path("/Users/georgewallace/elastic-repos/elasticsearch/docs/reference")

# Map FROM <index> patterns to stage names
INDEX_TO_STAGE = {
    "employees": "employees",
    "sample_data": "sample_data",
    "books": "books",
    "airports": "airports",
    "airport_city_boundaries": "airport_city_boundaries",
    "colors": "colors",
    "k8s": None,              # no stage yet
    "hosts": "hosts",
    "metrics": None,          # no stage yet
    "languages_lookup": "languages_lookup",
    "cooking_blog": "cooking_blog",
    "seats": "seats",
    "twitter": "twitter",
    "retrievers_example": "retrievers_example",
    "my-data-stream": "my-data-stream",
    "aliases": "aliases",
}

# Patterns to detect which index a query uses
FROM_RE = re.compile(r"^\s*FROM\s+([a-zA-Z0-9_*,\s-]+?)(?:\s*\||\s*$)", re.MULTILINE | re.IGNORECASE)


def extract_code_section(yaml_text):
    """Extract the content of the !code section."""
    m = re.search(r"--- !code\s*\n\|?\n?(.*?)(?=\n--- !)", yaml_text, re.DOTALL)
    if m:
        return m.group(1)
    return ""


def detect_stage(code):
    """Return the stage name for the index used in the code, or None."""
    matches = FROM_RE.findall(code)
    for m in matches:
        # Handle comma-separated indices or wildcard patterns
        for idx in re.split(r"[,\s]+", m.strip()):
            idx = idx.strip().rstrip("*").split("-")[0]  # normalize
            if idx in INDEX_TO_STAGE:
                stage = INDEX_TO_STAGE[idx]
                if stage:
                    return stage
    return None


def has_stage(yaml_text):
    """Check if the !test section already has a stage: field."""
    test_m = re.search(r"--- !test\s*\n(.*)", yaml_text, re.DOTALL)
    if not test_m:
        return False
    test_body = test_m.group(1)
    return bool(re.search(r"^stage\s*:", test_body, re.MULTILINE))


def patch_yaml_stage(yaml_text, stage):
    """Insert stage: <stage> into the !test section."""
    # Insert after --- !test line
    return re.sub(
        r"(--- !test\s*\n)",
        f"\\1stage: {stage}\n",
        yaml_text,
        count=1
    )


def process_yaml_files(dry_run=False):
    patched = 0
    skipped_no_stage = 0
    already_has = 0

    for yaml_file in sorted(EXAMPLES_DIR.rglob("test_*.yaml")):
        text = yaml_file.read_text(encoding="utf-8")

        # Skip if already has stage
        if has_stage(text):
            already_has += 1
            continue

        code = extract_code_section(text)
        stage = detect_stage(code)
        if not stage:
            skipped_no_stage += 1
            continue

        if dry_run:
            print(f"WOULD PATCH: {yaml_file.relative_to(EXAMPLES_DIR)} -> stage: {stage}")
        else:
            new_text = patch_yaml_stage(text, stage)
            yaml_file.write_text(new_text, encoding="utf-8")
        patched += 1

    print(f"\nYAML patch summary:")
    print(f"  Patched: {patched}")
    print(f"  Already had stage: {already_has}")
    print(f"  No matching stage: {skipped_no_stage}")
    return patched


# Markdown files that need stage annotations (non-generated)
ESQL_MD_FILES = [
    "query-languages/esql/esql-syntax.md",
    "query-languages/esql/esql-getting-started.md",
    "query-languages/esql/esql-query-tips.md",
    "query-languages/esql/esql-time-spans.md",
    "query-languages/esql/esql-multi-index.md",
    "query-languages/esql/esql-metadata-fields.md",
    "query-languages/esql/esql-multivalued-fields.md",
    "query-languages/esql/esql-implicit-casting.md",
    "query-languages/esql/esql-rest.md",
    "query-languages/esql/esql-enrich-data.md",
    "query-languages/esql/esql-lookup-join.md",
    "query-languages/esql/esql-process-data-with-dissect-grok.md",
]

# Additional console-block markdown files (non-esql) that need stage annotations
CONSOLE_MD_FILES = [
    "scripting-languages/painless/painless-context-examples.md",
    "scripting-languages/painless/painless-bucket-script-agg-context.md",
    "scripting-languages/painless/painless-update-by-query-context.md",
    "scripting-languages/painless/painless-score-context.md",
    "scripting-languages/painless/painless-min-should-match-context.md",
    "scripting-languages/painless/painless-bucket-selector-agg-context.md",
    "scripting-languages/painless/painless-watcher-transform-context.md",
]

# Index-to-stage for console blocks (REST API, not ES|QL)
CONSOLE_INDEX_TO_STAGE = {
    "seats": "seats",
    "cooking_blog": "cooking_blog",
    "twitter": "twitter",
    "retrievers_example": "retrievers_example",
}

ESQL_OPEN_RE = re.compile(r"^```esql(?!\-)\b", re.MULTILINE)
CONSOLE_OPEN_RE = re.compile(r"^([ \t]*)```console(?!\-)\b", re.MULTILINE)
EXISTING_ANNOTATION_RE = re.compile(r"<!--\s*\n\s*---\s*!example.*?-->", re.DOTALL)


def detect_stage_from_code_block(block_code):
    """Detect stage from an esql code block."""
    return detect_stage(block_code)


def annotate_markdown_file(path, dry_run=False):
    """Add stage annotations before esql blocks in a markdown file."""
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines(keepends=True)
    changes = []

    i = 0
    while i < len(lines):
        line = lines[i]
        if not ESQL_OPEN_RE.match(line):
            i += 1
            continue

        open_idx = i
        # Find closing fence
        close_idx = None
        j = i + 1
        while j < len(lines):
            if re.match(r"^```\s*$", lines[j]):
                close_idx = j
                break
            j += 1
        if close_idx is None:
            i += 1
            continue

        # Extract block body to detect stage
        block_body = "".join(lines[open_idx + 1:close_idx])
        stage = detect_stage_from_code_block(block_body)
        if not stage:
            i = close_idx + 1
            continue

        # Check if already annotated (look backwards)
        prev = open_idx - 1
        while prev >= 0 and lines[prev].strip() == "":
            prev -= 1
        already_annotated = prev >= 0 and lines[prev].strip() == "-->"

        if already_annotated:
            i = close_idx + 1
            continue

        comment = f"<!--\n--- !example\nstage: {stage}\n-->\n"
        changes.append({"open_idx": open_idx, "stage": stage, "comment": comment})
        i = close_idx + 1

    if not changes:
        return 0

    if dry_run:
        for ch in changes:
            print(f"  WOULD ADD stage: {ch['stage']} before line {ch['open_idx']+1}")
        return len(changes)

    # Apply in reverse order
    for ch in sorted(changes, key=lambda c: c["open_idx"], reverse=True):
        idx = ch["open_idx"]
        comment_lines = ch["comment"].splitlines(keepends=True)
        lines[idx:idx] = comment_lines

    path.write_text("".join(lines), encoding="utf-8")
    return len(changes)


def annotate_console_file(path, dry_run=False):
    """Add stage annotations before console blocks in a markdown file."""
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines(keepends=True)
    changes = []

    i = 0
    while i < len(lines):
        line = lines[i]
        m = CONSOLE_OPEN_RE.match(line)
        if not m:
            i += 1
            continue
        indent_str = m.group(1)
        open_idx = i
        close_idx = None
        j = i + 1
        while j < len(lines):
            if re.match(rf"^{re.escape(indent_str)}```\s*$", lines[j]):
                close_idx = j
                break
            j += 1
        if close_idx is None:
            i += 1
            continue
        block_body = "".join(lines[open_idx + 1:close_idx])
        # Detect stage from index names in block
        stage = None
        for idx_name, stage_name in CONSOLE_INDEX_TO_STAGE.items():
            if re.search(rf"\b{re.escape(idx_name)}\b", block_body, re.IGNORECASE):
                stage = stage_name
                break
        if not stage:
            i = close_idx + 1
            continue
        prev = open_idx - 1
        while prev >= 0 and lines[prev].strip() == "":
            prev -= 1
        if prev >= 0 and lines[prev].strip() == "-->":
            i = close_idx + 1
            continue
        comment = f"{indent_str}<!--\n{indent_str}--- !example\n{indent_str}stage: {stage}\n{indent_str}-->\n"
        changes.append({"open_idx": open_idx, "stage": stage, "comment": comment})
        i = close_idx + 1

    if not changes:
        return 0
    if dry_run:
        for ch in changes:
            print(f"  WOULD ADD stage: {ch['stage']} before line {ch['open_idx']+1}")
        return len(changes)
    for ch in sorted(changes, key=lambda c: c["open_idx"], reverse=True):
        idx = ch["open_idx"]
        lines[idx:idx] = ch["comment"].splitlines(keepends=True)
    path.write_text("".join(lines), encoding="utf-8")
    return len(changes)


def process_markdown_files(dry_run=False):
    total = 0
    for rel in ESQL_MD_FILES:
        path = DOCS_REF / rel
        if not path.exists():
            print(f"  MISSING: {rel}")
            continue
        n = annotate_markdown_file(path, dry_run=dry_run)
        if n:
            print(f"  {'Would add' if dry_run else 'Added'} {n} annotation(s) to {rel}")
        total += n
    for rel in CONSOLE_MD_FILES:
        path = DOCS_REF / rel
        if not path.exists():
            print(f"  MISSING: {rel}")
            continue
        n = annotate_console_file(path, dry_run=dry_run)
        if n:
            print(f"  {'Would add' if dry_run else 'Added'} {n} annotation(s) to {rel}")
        total += n
    return total


def main():
    dry_run = "--dry-run" in sys.argv
    if dry_run:
        print("=== DRY RUN ===\n")

    print("=== Patching test YAML files ===")
    process_yaml_files(dry_run=dry_run)

    print("\n=== Adding annotations to markdown files ===")
    n = process_markdown_files(dry_run=dry_run)
    print(f"  Total markdown annotations: {n}")

    if dry_run:
        print("\nRun without --dry-run to apply changes.")


if __name__ == "__main__":
    main()
