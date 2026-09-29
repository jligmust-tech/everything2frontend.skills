---
name: problem2interactive
description: "Turn a problem into a runnable, self-contained interactive HTML frontend where changing inputs recomputes the answer live. Use when the answer depends on parameters, for 'what if' analysis, calculators, pickers, simulators, and any problem that should be handled by adjusting knobs. A focused mode of the everything2frontend skill."
disable-model-invocation: false
allowed-tools: Read Bash Write Edit Glob Grep
---

# problem2interactive

Render a problem as a **live interactive page**: knobs on the left, computed
answer on the right, a verification panel below.

This is the `interactive` mode of `everything2frontend`. Read the core skill at
`../everything2frontend/SKILL.md` for the full Frontend IR; this file is the
focused checklist for building the page.

## Output contract

- **One** self-contained `.html` file. Inline CSS + JS. No CDN, no web fonts,
  no network calls. Opens offline.
- A pure, deterministic `derive(state, inputs)` function.
- A **verification panel** that runs the `verify` assertions and shows PASS/FAIL.
- Defaults chosen so the page is meaningful on first load.

## Build steps

1. Fill the Frontend IR: state, inputs (with ranges + defaults), transforms,
   view, verify. See `../everything2frontend/references/frontend-ir.md`.
2. Copy `../everything2frontend/assets/template-interactive.html` — it is a
   working reference app (declarative `CONTROLS`, `derive()`, `VIEWS`, `VERIFY`,
   SVG bar chart, table, verification panel). Adapt it rather than starting blank.
3. Replace the example data with the problem's state and transforms.
   `derive()` must not read the DOM, the clock, or randomness.
4. Add at least one `VERIFY` entry for the headline answer and one for an
   invariant.
5. Validate: `python ../everything2frontend/scripts/validate_output.py <file>`.

## Interaction rules

- Every input has a real `<label>` and `<output>` showing its current value+unit.
- Changing any input immediately updates **every** dependent readout, chart, and
  table — recompute the whole derived object, do not patch fields.
- Include a way to return to defaults (reload does it; a Reset button is nicer).
- Numbers use `toLocaleString` and always show a unit.
- Works keyboard-only and down to ~360px wide.

## Done when

All `VERIFY` items are PASS, `validate_output.py` passes, and moving any control
visibly changes the answer.
