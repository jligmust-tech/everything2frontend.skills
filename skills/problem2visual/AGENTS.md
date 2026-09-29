# AGENTS.md — problem2visual

Focused mode of **everything2frontend**: render a problem as a self-contained
visual explainer.

## Deliverable

One `.html` file, inline CSS, inline SVG (or canvas), no network calls, readable
without any interaction. Sections: header (restated problem + answer), hero
diagram, steps, key-numbers table, takeaway, assumptions.

## Steps

1. Fill the Frontend IR (`../everything2frontend/references/frontend-ir.md`);
   make the `view` a single carrying diagram.
2. Copy `../everything2frontend/assets/template-visual.html` and adapt it.
3. Hand-author the SVG: boxes, edges, labels, arrow marker.
4. Every number gets a label and unit.
5. Run `python ../everything2frontend/scripts/validate_output.py <file>`.

## Rules

- One idea per diagram; label every axis and edge.
- Content is visible without animation or interaction.
- Self-contained; offline; no CDN.
