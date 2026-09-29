---
name: problem2spec
description: "Turn a problem into a frontend specification: a Markdown document with real TypeScript state types, a discriminated-union event model, pure transform signatures, a component tree with data flow, edge cases, and acceptance tests. Use when the deliverable is a design or implementation plan rather than a running page. A focused mode of the everything2frontend skill."
disable-model-invocation: false
allowed-tools: Read Bash Write Edit Glob Grep
---

# problem2spec

Render a problem as a **frontend specification** a developer can implement
without asking further questions.

This is the `spec` mode of `everything2frontend`. Read
`../everything2frontend/SKILL.md` for the Frontend IR; this file is the focused
checklist.

## Output contract

- A Markdown document following the spec skeleton.
- State expressed as **real TypeScript** (`interface` / `type`), not prose.
- Events as a **discriminated union** plus an event table.
- Every transform typed `(state, inputs) -> derived` and marked pure.
- A component tree with props and the data flow.
- Edge-case table (empty / single / extreme / invalid).
- Concrete acceptance tests: given -> expected, with tolerances.

## Build steps

1. Fill the Frontend IR (`../everything2frontend/references/frontend-ir.md`).
2. Copy `../everything2frontend/assets/template-spec.md` and replace every
   placeholder with real content — no `{{ }}` left behind.
3. Turn state/inputs into TypeScript types with units in comments.
4. Turn the event model into a discriminated union.
5. Write pure transform signatures with one worked example each.
6. Draw the component tree and label the data flow.
7. Enumerate edge cases and write the acceptance-test table.
8. Validate: `python ../everything2frontend/scripts/validate_output.py <file>`.

## Done when

An engineer could build the `interactive` mode from this document alone; every
acceptance test has a concrete expected value and tolerance.

## Optional pairing

If the user wants both design and demo, deliver the spec **and** an interactive
page (via `problem2interactive`) as two separate files.
