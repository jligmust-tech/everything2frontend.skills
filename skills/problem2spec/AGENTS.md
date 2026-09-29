# AGENTS.md — problem2spec

Focused mode of **everything2frontend**: render a problem as a frontend
specification (Markdown + TypeScript).

## Deliverable

A Markdown spec: restatement + assumptions, full Frontend IR, TypeScript state
and event types, pure transform signatures, component tree with data flow, edge
cases, and a concrete acceptance-test table.

## Steps

1. Fill the Frontend IR (`../everything2frontend/references/frontend-ir.md`).
2. Copy `../everything2frontend/assets/template-spec.md` and replace every token.
3. Write real TypeScript types (units in comments).
4. Model events as a discriminated union.
5. Give each transform a signature and one worked example.
6. Enumerate edge cases and acceptance tests with tolerances.
7. Run `python ../everything2frontend/scripts/validate_output.py <file>`.

## Rules

- No prose where a type belongs.
- Every transform is `(state, inputs) -> derived` and pure.
- Acceptance tests are concrete: given -> expected.
