#!/usr/bin/env python3
"""
Find all ```console blocks in docs/reference that have a % TEST[setup:<stage>] line
immediately after the closing fence, and which do NOT already have a
  <!--
  --- !example
  stage: <stage>
  -->
annotation immediately before the opening fence.

Prints a dry-run report showing every file and change that WOULD be made.
Pass --apply to actually write the changes.

Usage:
    python find_console_samples.py           # dry-run report
    python find_console_samples.py --apply   # write changes
"""

import argparse
import re
import sys
from pathlib import Path

DOCS_ROOT = Path(__file__).parent / "reference"

# % TEST[setup:stage_name] — capture the raw value inside setup:...
TEST_SETUP_RE = re.compile(r"^%\s*TEST\[setup:([^\]]+)\]")

# Already-present annotation comment block
EXISTING_ANNOTATION_RE = re.compile(
    r"<!--\s*\n\s*---\s*!example.*?-->", re.DOTALL
)


def stage_from_setup(raw: str) -> str:
    """Extract the stage name from the raw setup value.

    Examples:
      "sales"                          -> "sales"
      "sales s/now-10M\\/M/10-2015/"  -> "sales"
      "ledger,stored_scripted_metric"  -> "ledger,stored_scripted_metric"
    """
    # Strip substitution patterns (everything from first space onward)
    stage = raw.split()[0]
    return stage


def find_changes(path: Path) -> list[dict]:
    """Return a list of changes needed in *path*.

    Each change dict has:
      line      : 1-based line number of the ```console opening fence
      stage     : stage name to inject
      comment   : the exact comment string to insert
      raw_setup : the full raw value from % TEST[setup:...]
    """
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines(keepends=True)
    changes = []

    i = 0
    while i < len(lines):
        line = lines[i]

        # Look for ```console (but not ```console-result)
        if not re.match(r"^```console(?!\-)\b", line):
            i += 1
            continue

        open_idx = i  # 0-based index of the opening fence

        # Find the closing fence
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

        # Check the line immediately after the closing fence for % TEST[setup:...]
        after_idx = close_idx + 1
        if after_idx >= len(lines):
            i = close_idx + 1
            continue

        m = TEST_SETUP_RE.match(lines[after_idx].strip())
        if not m:
            i = close_idx + 1
            continue

        raw_setup = m.group(1).strip()
        stage = stage_from_setup(raw_setup)
        comment = f"<!--\n--- !example\nstage: {stage}\n-->\n"

        # Check whether an annotation already precedes this ```console line.
        # Look backward (skipping blank lines) for an existing --> closing tag.
        prev = open_idx - 1
        while prev >= 0 and lines[prev].strip() == "":
            prev -= 1

        already_annotated = prev >= 0 and lines[prev].strip() == "-->"

        if already_annotated:
            i = close_idx + 1
            continue

        changes.append(
            {
                "line": open_idx + 1,  # 1-based
                "stage": stage,
                "raw_setup": raw_setup,
                "comment": comment,
                "open_idx": open_idx,
            }
        )

        i = close_idx + 1

    return changes


def apply_changes(path: Path, changes: list[dict]) -> None:
    """Insert annotation comments into *path* for all changes (in reverse order)."""
    lines = path.read_text(encoding="utf-8").splitlines(keepends=True)

    # Process in reverse so line indices remain valid
    for change in sorted(changes, key=lambda c: c["open_idx"], reverse=True):
        idx = change["open_idx"]
        comment_lines = change["comment"].splitlines(keepends=True)
        lines[idx:idx] = comment_lines

    path.write_text("".join(lines), encoding="utf-8")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--apply", action="store_true", help="Write changes (default: dry-run only)"
    )
    args = parser.parse_args()

    md_files = sorted(DOCS_ROOT.rglob("*.md"))

    all_changes: list[tuple[Path, list[dict]]] = []
    for path in md_files:
        changes = find_changes(path)
        if changes:
            all_changes.append((path, changes))

    if not all_changes:
        print("No files need annotation.")
        return

    total_blocks = sum(len(c) for _, c in all_changes)
    print(f"{'='*70}")
    print(f"DRY RUN — files that would be annotated")
    print(f"Files : {len(all_changes)}")
    print(f"Blocks: {total_blocks}")
    print(f"{'='*70}\n")

    for path, changes in all_changes:
        rel = path.relative_to(DOCS_ROOT.parent)
        print(f"FILE: {rel}  ({len(changes)} block(s))")
        for ch in changes:
            stage_note = ""
            if ch["raw_setup"] != ch["stage"]:
                stage_note = f"  [raw: {ch['raw_setup']!r}]"
            print(f"  Line {ch['line']:>5}  stage={ch['stage']!r}{stage_note}")
            print(f"          INSERT before line {ch['line']}:")
            for ln in ch["comment"].splitlines():
                print(f"            {ln}")
        print()

    if args.apply:
        for path, changes in all_changes:
            apply_changes(path, changes)
        print(f"✅ Applied {total_blocks} annotation(s) across {len(all_changes)} file(s).")
    else:
        print("Run with --apply to write these changes.")


if __name__ == "__main__":
    main()
