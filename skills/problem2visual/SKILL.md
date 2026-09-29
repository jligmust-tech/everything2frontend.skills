---
name: problem2visual
description: "Turn a problem into a self-contained visual explainer: an HTML page with diagrams, charts, timelines, or step-by-step structure that makes the answer obvious at a glance. Use for explaining how something works, showing structure/flow/hierarchy, or any problem whose answer is a shape or process rather than a number. A focused mode of the everything2frontend skill."
disable-model-invocation: false
allowed-tools: Read Bash Write Edit Glob Grep
---

# problem2visual

Render a problem as a **visual explainer**: a static, self-contained page a
person reads top-to-bottom and understands.

This is the `visual` mode of `everything2frontend`. Read
`../everything2frontend/SKILL.md` for the Frontend IR; this file is the focused
checklist for the page.

## Output contract

- **One** self-contained `.html` file. Inline CSS. No libs, no network calls.
- The diagram is **inline SVG** (scales, no dependency) or a simple `<canvas>`.
- Readable with **zero interaction**.
- Shows the headline answer and the assumptions in the page.

## Build steps

1. Fill the Frontend IR. For a visual answer the `view` is the star: decide the
   single diagram/chart/timeline that carries the idea.
2. Copy `../everything2frontend/assets/template-visual.html` (header + hero SVG +
   steps + key-numbers table + takeaway + assumptions).
3. Replace the example diagram with the problem's structure. Keep the SVG
   hand-authored: boxes, edges, labels, arrows via a `<marker>`.
4. Numbers table: every quantity with a label and unit; note the source.
5. Validate: `python ../everything2frontend/scripts/validate_output.py <file>`.

## Visual rules

- One idea per diagram. If you need a second idea, add a second section.
- Label axes and edges; a viewer should never guess what an arrow means.
- Prefer a clear layout over decoration. Colour carries meaning, not mood.
- No animation that is required to reveal content.
- Logical heading order (`h1` then `h2`) for accessibility.

## Done when

Someone who knows nothing about the problem reads the page once and can state the
answer and the reason.
