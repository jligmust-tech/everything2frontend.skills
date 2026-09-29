# {{TITLE}}

> **Raw problem:** {{RAW_PROBLEM}}
>
> **Restated:** {{RESTATED}}

## Assumptions

- {{ASSUMPTION_1}}
- {{ASSUMPTION_2}}

---

## Frontend IR

```yaml
id: {{SLUG}}
domain: <domain>
mode: spec
state:
  - { name: <n>, type: <T>, unit: <u>, sample: <v> }
inputs:
  - { name: <n>, type: <T>, range: <r>, default: <v>, label: "<human label>" }
transforms:
  - { name: <n>, signature: "(state, inputs) -> T", rule: "<rule>", example: "<in -> out>" }
view:
  - { element: <controls|readout|chart|table|diagram|steps>, binds: [<names>] }
verify:
  - { assertion: "<claim>", test: "<condition>", expected: <value> }
answer: "<headline result>"
```

---

## State (TypeScript)

```ts
export interface State {
  readonly <field>: <type>; // <unit>
}

export interface Inputs {
  readonly <field>: <type>; // <unit>, default <v>
}

export interface Derived {
  readonly <field>: <type>; // <unit>
}
```

---

## Inputs / Events

```ts
export type Event =
  | { type: "SET_INPUT"; id: keyof Inputs; value: Inputs[keyof Inputs] }
  | { type: "RESET" };
```

| Event | Payload | Effect |
|-------|---------|--------|
| `SET_INPUT` | `{ id, value }` | updates `inputs[id]`, re-derives |
| `RESET` | — | restores defaults |

---

## Transforms (pure)

```ts
/** (state, inputs) -> derived — pure, deterministic, no I/O. */
export function derive(state: State, inputs: Inputs): Derived {
  throw new Error("implement");
}
```

| Transform | Signature | Semantics | Worked example |
|-----------|-----------|-----------|----------------|
| `<name>` | `(state, inputs) -> T` | `<rule>` | `<in> -> <out>` |

---

## View

```
<App>
├── <Header title restated answer />
├── <Controls>
│   └── <Field label unit />            // one per input
├── <Result>
│   ├── <Readout label value unit />    // one per key derived value
│   └── <Chart series />
└── <Verification assertions />
```

**Data flow:** `inputs → derive(state, inputs) → Derived → { Readout, Chart, Verification }`

---

## Edge cases

| Case | State / Inputs | Expected behaviour |
|------|----------------|--------------------|
| empty | `<...>` | `<...>` |
| single | `<...>` | `<...>` |
| extreme | `<...>` | `<...>` |
| invalid | `<...>` | reject / clamp, never crash |

---

## Acceptance tests

| # | Given (inputs) | Expect (derived) | Tolerance |
|---|----------------|------------------|-----------|
| 1 | `<...>` | `<...>` | exact |
| 2 | `<...>` | `<...>` | `±1e-9` |
| 3 | defaults | headline answer holds | pass |
