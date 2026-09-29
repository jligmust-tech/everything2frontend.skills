# Quality bar

Everything below must hold before an artifact is delivered. `scripts/validate_output.py`
checks the mechanical parts; you are responsible for the rest.

## Universal

- [ ] The raw problem was **restated** as one testable sentence.
- [ ] Assumptions are **listed in the artifact** (not only in chat).
- [ ] The headline **answer** is stated explicitly and shown on screen.
- [ ] No `TODO` markers remain — only real content or explicit `ASSUMPTION:`.
- [ ] Every number has a **label and a unit**.

## Interactive / visual (HTML)

- [ ] **Single file**, self-contained: all CSS/JS inline.
- [ ] **No external resources**: no CDN, no `<script src="http…">`, no web fonts,
      no images fetched over the network, no `fetch()` to remote hosts.
- [ ] **Works offline** when opened directly from disk.
- [ ] `derive()` is **pure and deterministic** — no clock, no randomness, no DOM
      access inside it. Any seed is an explicit input.
- [ ] A **verification panel** exists and evaluates the `verify` assertions,
      rendering PASS/FAIL per item.
- [ ] Inputs have real `<label>` elements and sensible defaults.
- [ ] Changing an input immediately updates all dependent outputs (interactive).
- [ ] Readable contrast; usable via keyboard; responsive down to ~360px.

## Spec (Markdown / TypeScript)

- [ ] State is expressed as **real TypeScript** types.
- [ ] Events are a **discriminated union** (or an explicit event table).
- [ ] Every transform signature is `(state, inputs) -> derived` and marked pure.
- [ ] A component tree with props and data flow is present.
- [ ] Edge cases enumerated (empty / single / extreme / invalid).
- [ ] Acceptance tests are concrete: given -> expected, with tolerances.

## Verification discipline

1. Name at least one assertion that checks the **headline answer**.
2. Add at least one assertion that checks an **invariant** (a relationship that
   must always hold, e.g. `difference == a - b`).
3. Run `validate_output.py`; fix everything it reports.
4. Only then report completion, with the file path and the answer.

## Common failure modes (avoid)

- Leaving a template's placeholder text in the final artifact.
- Pulling a charting library from a CDN — draw with inline SVG or canvas instead.
- Hiding a wrong answer behind pretty visuals — verify first, then style.
- Silently choosing an assumption that changes the answer — surface it.
- Numbers without units, or units that change silently when an input changes.
