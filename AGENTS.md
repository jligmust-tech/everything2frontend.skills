# AGENTS.md — everything2frontend.skills

Portable instructions for **Codex, Claude, and any general-purpose agent**.

## What this repo gives you

A skill collection whose single purpose is:

> Take **any** question, problem, dataset, decision, or vague request, and
> **solve it by regarding it as a frontend problem** — an actor interacting with
> state through a view, scored by pure transforms and verifications — then render
> it as something a human can see and handle.

The frontend language is a fixed 5-part structure (the *Frontend IR*):

| Part | Meaning |
|------|---------|
| **State** | the nouns — everything the problem is about (typed values) |
| **Inputs** | the verbs — what a person can change or ask |
| **Transforms** | pure rules: `state + inputs -> derived` |
| **View** | how state/derived map onto controls, readouts, charts, tables, diagrams |
| **Verify** | assertions that prove the answer is right |

Any problem expressed this way becomes a frontend. It then renders to one of
three targets: **interactive app**, **visual explainer**, or **frontend spec**.

## How to use it (any agent)

1. Read the canonical skill: `skills/everything2frontend/SKILL.md`.
2. Read its references: `references/solve-as-frontend.md`,
   `references/frontend-ir.md`, `references/modes.md`, `references/quality-bar.md`.
3. Copy a template from `assets/` (or run `scripts/scaffold.py`).
4. Fill the Frontend IR, then fill the template.
5. Run `scripts/validate_output.py` on the artifact before delivering.

Per-skill `AGENTS.md` files (e.g. `skills/everything2frontend/AGENTS.md`) are
self-contained entry points when a skill is copied out of this repo alone.

## Non-negotiables

- Output is a **single self-contained HTML file** (interactive/visual) that
  works **offline, with no build step and no network calls**.
- `derive()` must be **pure and deterministic** — same inputs, same outputs.
- Every number shown has a **label and a unit**.
- Ship a **verification panel** proving the stated answer.
- If the problem is ambiguous, state assumptions explicitly in the artifact.

## Commands

```powershell
python skills\everything2frontend\scripts\scaffold.py --mode interactive `
  --problem "<raw problem>" --slug <slug> --out .\out

python skills\everything2frontend\scripts\validate_output.py .\out\<slug>.html
```

## Repo map

```
skills/everything2frontend/   CORE router skill (choose + run a mode)
skills/problem2interactive/   mode: runnable, live-computed page
skills/problem2visual/        mode: diagram / chart / step explainer
skills/problem2spec/          mode: state + component design (TypeScript)
```
