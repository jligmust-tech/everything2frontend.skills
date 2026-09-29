# AGENTS.md — everything2frontend (portable entry)

This folder is the **everything2frontend** skill. Point any agent (Codex, Claude,
or a general-purpose agent) here and it can compile any problem into a frontend.

## Mission

> Every problem can be **solved** by regarding it as a frontend problem: an actor
> interacting with state through a view, scored by pure transforms and
> verifications. Take any question, problem, dataset, decision, or vague request
> and reduce it to that shape, then render it.

## The frontend language (Frontend IR)

| Part | Meaning |
|------|---------|
| State | the nouns — typed values the problem is about |
| Inputs | the verbs — what a person can change |
| Transforms | pure rules: `(state, inputs) -> derived` |
| View | state/derived -> controls, readouts, charts, tables, diagrams |
| Verify | assertions proving the answer |

## Modes

- `interactive` — single self-contained HTML page with live inputs (default).
- `visual` — single self-contained HTML explainer (diagram / chart / steps).
- `spec` — Markdown + TypeScript state and component design.

## Procedure

1. Reduce the problem to a frontend problem (see `references/solve-as-frontend.md`):
   name the state, expose the inputs, purify the transforms, pick the view,
   define the verification.
2. Restate as one testable sentence; list assumptions.
3. Fill the IR (see `references/frontend-ir.md`).
4. Pick a mode (see `references/modes.md`).
5. Scaffold: `python scripts/scaffold.py --mode <mode> --problem "<raw>" --slug <slug> --out <dir>`
6. Fill the template from `assets/`, keeping the artifact self-contained.
7. Validate: `python scripts/validate_output.py <artifact>` and fix everything.
8. Satisfy every item in `references/quality-bar.md`.

## Hard rules

- One self-contained HTML file; offline; no build step; no network calls.
- `derive()` is pure and deterministic.
- Every number carries a label and a unit.
- A verification panel with PASS/FAIL is always present.
- Assumptions live inside the artifact.
