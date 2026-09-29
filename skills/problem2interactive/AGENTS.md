# AGENTS.md — problem2interactive

Focused mode of **everything2frontend**: render a problem as a runnable,
self-contained interactive HTML page.

## Deliverable

One `.html` file with inline CSS/JS, no network calls, that computes an answer
live as the user changes inputs, plus a PASS/FAIL verification panel.

## Steps

1. Fill the Frontend IR (`../everything2frontend/references/frontend-ir.md`).
2. Copy `../everything2frontend/assets/template-interactive.html` and adapt it.
3. Implement a pure `derive(state, inputs)`; bind inputs; render readouts/chart/table.
4. Add `verify` assertions (one for the headline answer, one invariant).
5. Run `python ../everything2frontend/scripts/validate_output.py <file>`.

## Rules

- Self-contained; offline; no CDN; no randomness or clock inside `derive()`.
- Labels + units on every number; real `<label>`s on controls.
- Recompute all outputs on any input change.
