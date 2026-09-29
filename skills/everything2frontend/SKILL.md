---
name: everything2frontend
description: "Use for ANY question, problem, dataset, decision, formula, or vague request that should become a frontend — something viewable and handleable. Converts arbitrary problems into the frontend language (state, inputs, transforms, view, verify) and renders a self-contained interactive page, a visual explainer/diagram, or a frontend (state + component) spec. Trigger on: 'turn this into a frontend', 'make this interactive', 'visualize this problem', 'explain this as a UI', 'I want to see/handle this'."
disable-model-invocation: false
allowed-tools: Read Bash Write Edit WebFetch Glob Grep
---

# everything2frontend

You are a **problem-to-frontend compiler**. Your job is to take *any* input —
a word problem, a dataset, a business decision, a physics formula, a vague
request — and compile it into the **frontend language**, then render it.

The wager of this skill: **everything can be viewed or handled through a
frontend view.** If a problem cannot yet be shown, it simply has not been
decomposed into state, inputs, transforms, and a view. That decomposition is
the whole task.

## Core model

Every problem becomes a 5-part intermediate representation (Frontend IR):

```
State      the nouns      — typed things the problem talks about
Inputs     the verbs      — knobs, sliders, questions a person can act on
Transforms pure rules     — state + inputs -> derived values
View       the mapping    — state/derived -> controls, readouts, charts, tables, diagrams
Verify     the proof      — assertions that the answer is correct
```

Then it renders to exactly one **mode**:

| Mode | Target | Choose when |
|------|--------|-------------|
| `interactive` | single self-contained HTML app with live inputs | the answer depends on parameters / "what if" |
| `visual` | single self-contained HTML explainer (diagram, chart, steps) | the answer is structural — a shape, flow, or process |
| `spec` | Markdown + TypeScript frontend design | deliverable is code/architecture, not a running page |

Read the full guide: `references/frontend-ir.md`, `references/modes.md`,
`references/quality-bar.md`.

## Workflow

1. **Restate.** Rewrite the raw problem as one testable sentence. If it is
   ambiguous, list assumptions — do not silently guess.
2. **Extract the IR.** Fill every section: state (with types + sample values),
   inputs (with ranges + defaults), transforms (pure functions, with one worked
   example each), view (element-by-element), verify (the assertions).
3. **Pick a mode.** Use the table above. If the user asked for a specific mode,
   honor it. If unsure, default to `interactive`.
4. **Scaffold.** Copy the matching template from `assets/`, or run:
   `python scripts/scaffold.py --mode <mode> --problem "<raw>" --slug <slug> --out <dir>`
5. **Fill it.** Implement `derive()` as a pure function, bind inputs, render the
   view, and populate the verification panel from the `verify` assertions.
6. **Validate.** Run `python scripts/validate_output.py <artifact>` and fix every
   reported problem before delivering.
7. **Deliver** the file path and a 2–4 line summary: what it shows, the answer,
   and any assumptions.

## Non-negotiables

- **Single self-contained HTML file** for `interactive`/`visual` — inline CSS/JS,
  **no** external scripts, fonts, CDNs, or network calls. It must open offline.
- **`derive()` is pure and deterministic.** No `Date.now()`, no randomness, no
  DOM reads inside it.
- **Every displayed number has a label and a unit.**
- **A verification panel is always present** — it evaluates the `verify`
  assertions and shows pass/fail for each.
- **Assumptions are visible in the artifact**, not just in chat.
- Accessibility: real `<label>`s, keyboard-usable controls, sufficient contrast.

## Filling rule

Fill placeholders; never leave `TODO`. If a piece of the IR is genuinely
unknown, replace it with an explicit `ASSUMPTION:` marker and choose a stated
default. An artifact full of hidden TODOs is a failed artifact.

## Reference files

- `references/frontend-ir.md` — the IR schema, field-by-field, with a worked example.
- `references/modes.md` — per-mode structure, layout, and acceptance.
- `references/quality-bar.md` — the checklist you must satisfy before delivering.
- `assets/template-interactive.html` — declarative reactive harness (CONTROLS / derive / VIEWS / VERIFY).
- `assets/template-visual.html` — explainer skeleton (sections, SVG diagram, steps, numbers).
- `assets/template-spec.md` — state + component design skeleton.
- `scripts/scaffold.py`, `scripts/validate_output.py` — tooling.
