#!/usr/bin/env python3
"""Validate an everything2frontend artifact before delivery.

Checks the mechanical parts of the quality bar:
  * file exists and is non-trivial
  * HTML: doctype, closing tag, self-contained (no external resources / fetch)
  * no leftover {{ templates }} and no TODO markers
  * spec: has TypeScript code fences and an acceptance-test table

Usage:
    python validate_output.py path\\to\\artifact.html
    python validate_output.py path\\to\\artifact.spec.md

Exit code 0 = pass, 1 = failed checks.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

EXTERNAL_RE = re.compile(
    r"""(?:src|href)\s*=\s*["'](?:https?:)?//""",
    re.IGNORECASE,
)
IMPORT_URL_RE = re.compile(r"""import\s*\(\s*["']https?://""", re.IGNORECASE)
FETCH_HTTP_RE = re.compile(r"""fetch\s*\(\s*["']https?://""", re.IGNORECASE)
TOKEN_RE = re.compile(r"\{\{[A-Z0-9_]+\}\}")
TODO_RE = re.compile(r"\bTODO\b|FIXME|PLACEHOLDER", re.IGNORECASE)


def check_html(text: str, problems: list[str]) -> None:
    low = text.lower()
    if "<!doctype html>" not in low:
        problems.append("missing <!DOCTYPE html>")
    if "</html>" not in low:
        problems.append("missing closing </html>")
    if "<script" not in low and "<svg" not in low:
        problems.append("no <script> or <svg> found - is this really a frontend artifact?")
    for name, rx in (("external resource ref", EXTERNAL_RE),
                     ("dynamic import of a URL", IMPORT_URL_RE),
                     ("fetch() to a URL", FETCH_HTTP_RE)):
        if rx.search(text):
            problems.append(f"not self-contained: {name} detected")
    if "@import" in low and "http" in low:
        problems.append("not self-contained: remote CSS @import detected")


def check_spec(text: str, problems: list[str]) -> None:
    if "```ts" not in text and "```typescript" not in text:
        problems.append("spec has no TypeScript code fence (```ts)")
    if "|" not in text or "acceptance" not in text.lower():
        problems.append("spec has no acceptance-test table")


def main() -> int:
    if len(sys.argv) != 2:
        print("usage: validate_output.py <artifact>", file=sys.stderr)
        return 2

    path = Path(sys.argv[1])
    if not path.exists():
        print(f"FAIL: file not found: {path}", file=sys.stderr)
        return 1

    text = path.read_text(encoding="utf-8", errors="replace")
    problems: list[str] = []

    if len(text.strip()) < 200:
        problems.append(f"file is suspiciously small ({len(text.strip())} chars)")

    ext = path.suffix.lower()
    if ext in (".html", ".htm"):
        check_html(text, problems)
    elif ext in (".md", ".markdown"):
        check_spec(text, problems)
    else:
        print(f"note: unrecognised extension {ext!r}; running generic checks only")

    if TOKEN_RE.search(text):
        found = ", ".join(sorted(set(TOKEN_RE.findall(text))))
        problems.append(f"unfilled template tokens: {found}")

    todos = TODO_RE.findall(text)
    if todos:
        problems.append(f"{len(todos)} TODO/FIXME/PLACEHOLDER marker(s) remain")

    name = path.name
    if problems:
        print(f"FAIL  {name}")
        for p in problems:
            print(f"  - {p}")
        return 1

    print(f"PASS  {name}  ({len(text)} chars, {text.count(chr(10)) + 1} lines)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
