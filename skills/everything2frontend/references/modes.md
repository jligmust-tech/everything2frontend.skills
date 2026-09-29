# Modes

A mode is a render target for the Frontend IR. Pick one per artifact.

## Choosing a mode

| Signal in the problem | Mode |
|-----------------------|------|
| "what if…", "if I change…", "depends on…", numbers that move | `interactive` |
| "explain", "show how", structure, flow, hierarchy, timeline, process | `visual` |
| "design", "how should we build", "give me the types/components" | `spec` |
| ambiguous / none of the above | `interactive` (safe default) |

The user can force a mode; if they do, honor it even if the table suggests another.

---

## Mode: interactive

**Deliverable:** one self-contained `.html` file, no build, no network.

**Structure**

```
Header        title + restated problem + assumptions line
Controls      one <label>+control per input, grouped
Outputs       readouts (label + value + unit), a chart, and/or a table
Verification  a panel listing each verify assertion with PASS / FAIL
Footer        "state + inputs -> derive() -> view", seed/assumption notes
```

**Harness contract** (see `assets/template-interactive.html`):

- `CONTROLS` — declarative array describing each input.
- `derive(state, inputs)` — pure, deterministic, returns all derived values.
- `VIEWS` — readouts bound to `state`/`derived` names.
- `VERIFY` — assertions evaluated against the current derived values, rendered as a checklist.
- Optional `TABLE` / `series` for tabular and chart output.

**Acceptance:** editing any control updates every dependent readout instantly;
refresh returns to defaults; the verification panel is all-green for a correct solution.

---

## Mode: visual

**Deliverable:** one self-contained `.html` file, no build, no network.

**Structure**

```
Header        title, restated problem, one-line answer
Hero visual   the diagram / chart / timeline (inline SVG or canvas, no libs)
Steps / parts numbered sections explaining the structure
Key numbers   a table of the important quantities (label + value + unit)
Takeaway      the single sentence the viewer should leave with
Assumptions   explicit, in the page
```

**Rules**

- Prefer **inline SVG** for diagrams — it scales and needs no library.
- A chart must have axes labels and units.
- A process/timeline must be readable top-to-bottom without interaction.
- No animation that hides content; motion is optional garnish only.

**Acceptance:** a viewer who reads top-to-bottom understands the problem and the
answer without touching anything.

---

## Mode: spec

**Deliverable:** Markdown (optionally plus `.ts` snippets) describing the frontend.

**Structure** (see `assets/template-spec.md`):

```
# <Problem>
Restatement + assumptions
## Frontend IR          the full IR block
## State (TypeScript)   interfaces/types for state
## Inputs / Events       discriminated-union event types
## Transforms            pure function signatures + one-line semantics
## View                  component tree, props, and how data flows
## Edge cases            empty, singular, extreme, invalid
## Acceptance tests      table: input -> expected output
```

**Rules**

- Types are real TypeScript, not prose.
- Every transform signature is `(state, inputs) -> derived` and marked pure.
- Acceptance tests are concrete: given inputs, expected outputs, tolerance.

**Acceptance:** a developer could implement the interactive mode from the spec
without asking further questions.

---

## Multi-mode

A thorough answer may ship `interactive` + `spec` together (a running page and
the design behind it). Never merge them into one file: the spec is Markdown, the
app is HTML. Keep each deliverable single-purpose.
