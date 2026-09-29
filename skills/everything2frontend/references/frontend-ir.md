# The Frontend IR

The Frontend IR is the intermediate representation every problem is compiled
into. If you can fill every field, you have a frontend. If a field is empty, the
problem is under-specified — make the assumption explicit rather than skipping it.

## Schema

```yaml
id: <slug>                       # short kebab-case identifier
raw_problem: <verbatim>          # exactly what the user said
restated: <one testable sentence>
domain: <math|logic|data|decision|physics|finance|text|process|...>
mode: <interactive|visual|spec>

state:                           # the NOUNS — everything the problem is about
  - name: <identifier>
    type: <number|string|boolean|list<T>|record|...>
    unit: <unit or none>
    sample: <concrete example value>

inputs:                          # the VERBS — what a person can change or ask
  - name: <identifier>
    type: <number|string|boolean|select>
    range: <min..max or options>
    default: <value>
    unit: <unit or none>
    label: <human label shown in the UI>

transforms:                      # PURE rules: state + inputs -> derived
  - name: <identifier>
    signature: <(state, inputs) -> T>
    rule: <formula or plain-language rule>
    example: <inputs -> output, one concrete worked case>

view:                            # the MAPPING to the screen
  - element: <controls|readout|chart|table|diagram|steps|text>
    binds: <state/derived names>
    note: <what the viewer sees>

verify:                          # the PROOF
  - assertion: <plain-language claim>
    test: <checkable condition over (state, inputs, derived)>
    expected: <value or pass condition>

assumptions:                     # everything you filled in that wasn't given
  - <assumption>

answer: <the headline result the artifact must show>
```

## Rules per field

- **state** — name the *nouns*. If you wrote a verb, it belongs in inputs or
  transforms. Every state entry needs a type and a concrete sample value.
- **inputs** — only include things a human would actually want to change. Give
  each a sensible default so the artifact is meaningful on first load.
- **transforms** — must be pure. `(state, inputs) -> derived`. No I/O, no clock,
  no randomness. If a transform needs randomness, expose a seed as an input.
- **view** — each entry maps a data name to a visual channel. Prefer the
  simplest channel that works: readout > table > chart > diagram.
- **verify** — at least one assertion must check the headline `answer`. These
  become the on-page verification panel.

## Worked example

Raw problem: *"Is the 3-year phone contract worth it over buying outright?"*

```yaml
id: phone-contract-vs-outright
raw_problem: "Is the 3-year phone contract worth it over buying outright?"
restated: "Total contract cost over 36 months minus outright cost, in local currency."
domain: finance
mode: interactive

state:
  - { name: months, type: number, unit: months, sample: 36 }
inputs:
  - { name: retailPrice, type: number, range: 0..20000, default: 6999, unit: HKD, label: "Outright price" }
  - { name: monthlyFee,   type: number, range: 0..2000,  default: 299,  unit: HKD, label: "Monthly plan fee" }
  - { name: upfrontFee,   type: number, range: 0..20000, default: 0,    unit: HKD, label: "Upfront payment" }
  - { name: interestRate, type: number, range: 0..1,     default: 0.0,  unit: decimal, label: "Annual interest on loan" }

transforms:
  - name: contractTotal
    signature: "(state, inputs) -> number"
    rule: "upfrontFee + monthlyFee * months"
    example: "0 + 299*36 = 10764 HKD"
  - name: outrightTotal
    signature: "(state, inputs) -> number"
    rule: "retailPrice (ignoring interest for the base case)"
    example: "6999 HKD"
  - name: difference
    signature: "(state, inputs) -> number"
    rule: "contractTotal - outrightTotal"
    example: "10764 - 6999 = 3765 HKD"

view:
  - { element: controls, binds: [retailPrice, monthlyFee, upfrontFee, interestRate], note: "sliders for each parameter" }
  - { element: readout,  binds: [contractTotal, outrightTotal, difference], note: "headline numbers with units" }
  - { element: chart,    binds: [contractTotal, outrightTotal], note: "side-by-side bar comparison" }

verify:
  - { assertion: "With defaults, the contract costs more than buying outright", test: "difference > 0", expected: true }
  - { assertion: "Difference equals contractTotal minus outrightTotal", test: "abs(difference - (contractTotal - outrightTotal)) < 1e-6", expected: true }

assumptions:
  - Interest is ignored in the base comparison and only applies to the loan case.

answer: "With default values the contract costs 3,765 HKD more than buying outright."
```

This IR renders directly to the `interactive` mode: controls for the inputs, a
readout for the totals, a bar chart for the comparison, and a verification panel
running the two assertions.
