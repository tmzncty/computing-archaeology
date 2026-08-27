#!/usr/bin/env python3
"""Fail when a local Markdown link points to a missing repository path."""

from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import unquote

LINK_RE = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")
SKIP_PREFIXES = ("http://", "https://", "mailto:", "data:")


def iter_markdown_files(root: Path):
    for path in root.rglob("*.md"):
        if ".git" not in path.parts:
            yield path


def normalize_target(raw: str) -> str:
    target = raw.strip()
    if target.startswith("<") and target.endswith(">"):
        target = target[1:-1]
    # Markdown permits an optional title after whitespace. Local paths in this
    # repository do not contain spaces, so the first token is the path.
    target = target.split(maxsplit=1)[0]
    return unquote(target.split("#", 1)[0].split("?", 1)[0])


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    failures: list[str] = []

    for markdown in iter_markdown_files(root):
        text = markdown.read_text(encoding="utf-8")
        for match in LINK_RE.finditer(text):
            raw = match.group(1).strip()
            if not raw or raw.startswith("#") or raw.startswith(SKIP_PREFIXES):
                continue

            target = normalize_target(raw)
            if not target:
                continue

            resolved = (markdown.parent / target).resolve()
            try:
                resolved.relative_to(root)
            except ValueError:
                failures.append(f"{markdown.relative_to(root)} -> {raw} escapes repository")
                continue

            if not resolved.exists():
                failures.append(f"{markdown.relative_to(root)} -> {raw} (missing)")

    if failures:
        print("Broken internal Markdown links:", file=sys.stderr)
        for failure in failures:
            print(f"  {failure}", file=sys.stderr)
        return 1

    print("Internal Markdown links: OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
