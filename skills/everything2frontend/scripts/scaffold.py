#!/usr/bin/env python3
"""Scaffold a frontend artifact from the everything2frontend templates.

Usage:
    python scaffold.py --mode interactive --problem "..." --slug my-problem --out ./out
    python scaffold.py --mode visual      --problem "..." --slug my-diagram --out ./out
    python scaffold.py --mode spec        --problem "..." --slug my-design  --out ./out
"""
from __future__ import annotations

import argparse
import datetime as _dt
import html
import json
import re
import sys
from pathlib import Path

ASSETS = Path(__file__).resolve().parent.parent / "assets"

TEMPLATES = {
    "interactive": ("template-interactive.html", "{slug}.html"),
    "visual": ("template-visual.html", "{slug}.html"),
    "spec": ("template-spec.md", "{slug}.spec.md"),
}

TOKEN_RE = re.compile(r"\{\{([A-Z0-9_]+)\}\}")


def slugify(text: str) -> str:
    text = re.sub(r"[^a-zA-Z0-9]+", "-", text.strip().lower()).strip("-")
    return text[:60] or "frontend-problem"


def js_safe(text: str) -> str:
    """Make text safe inside a JS block comment."""
    return text.replace("*/", "* /").replace("\r", " ").replace("\n", " ")


def main() -> int:
    ap = argparse.ArgumentParser(description="Scaffold an everything2frontend artifact.")
    ap.add_argument("--mode", required=True, choices=sorted(TEMPLATES))
    ap.add_argument("--problem", required=True, help="the raw problem statement")
    ap.add_argument("--slug", default=None, help="output slug (defaults to problem)")
    ap.add_argument("--out", default="./out", help="output directory")
    ap.add_argument("--title", default=None)
    ap.add_argument("--restated", default=None)
    ap.add_argument("--answer", default=None)
    ap.add_argument("--assumptions", default=None)
    args = ap.parse_args()

    slug = slugify(args.slug or args.problem)
    template_name, out_pattern = TEMPLATES[args.mode]
    tpl_path = ASSETS / template_name
    if not tpl_path.exists():
        print(f"error: template not found: {tpl_path}", file=sys.stderr)
        return 2

    title = args.title or args.problem.strip().splitlines()[0][:90]
    restated = args.restated or args.problem.strip()
    answer = args.answer or "ANSWER: <state the headline result here>"
    assumptions = args.assumptions or "ASSUMPTION: none beyond the raw problem as stated."

    mapping = {
        "TITLE": html.escape(title),
        "SLUG": slug,
        "DATE": _dt.date.today().isoformat(),
        "RESTATED": html.escape(restated),
        "ANSWER": html.escape(answer),
        "ASSUMPTIONS": html.escape(assumptions),
        "ASSUMPTION_1": html.escape(assumptions),
        "ASSUMPTION_2": "Add any further assumptions here.",
        "RAW_PROBLEM": js_safe(args.problem),
    }

    src = tpl_path.read_text(encoding="utf-8")

    def sub(match: "re.Match[str]") -> str:
        key = match.group(1)
        if key in mapping:
            return str(mapping[key])
        print(f"  note: no value for token {{{{{key}}}}} (left as-is)", file=sys.stderr)
        return match.group(0)

    out_text = TOKEN_RE.sub(sub, src)

    out_dir = Path(args.out)
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / out_pattern.format(slug=slug)
    out_path.write_text(out_text, encoding="utf-8")

    print(f"scaffolded {args.mode} -> {out_path}")
    print("next: fill the Frontend IR (state / inputs / transforms / view / verify), then run")
    print(f"      python validate_output.py \"{out_path}\"")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
