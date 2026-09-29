# Solve everything as a frontend problem

The thesis of this skill is stronger than "make a picture":

> **Every problem can be solved by regarding it as a frontend problem.**

A *frontend problem* is any problem of this shape:

> An actor sees a **view** of some **state**, can change it through **inputs**,
> and a set of **pure transforms** and **verifications** decides whether the
> result is correct.

If you can restate a problem in that shape, you have not merely visualised it —
you have reduced it to something with a definite solution procedure: make the
transforms correct, make the view faithful, and make the verifications green.

## The reduction: any problem -> a frontend problem

Answer these five questions in order. The answers *are* the reduction.

| Question | Frontend concept | Why it helps you solve |
|----------|------------------|------------------------|
| What are the things? | **state** | Difficulty is usually hidden in unnamed nouns. Naming them shrinks the problem. |
| What can be changed / asked? | **inputs** | Every assumption becomes an explicit knob instead of a silent guess. |
| What is computed from those? | **transforms** | Forces the messy real problem into pure, testable rules. |
| How would a person see it? | **view** | Externalises the reasoning; you spot gaps you cannot see in your head. |
| How do we know it's right? | **verify** | Turns "I think" into checkable assertions with expected values. |

A problem that resists all five is not unsolvable — it is under-specified. Split
it until a piece accepts all five.

## Why this solves rather than decorates

- **Naming state** converts an entangled mess into independent variables you can
  reason about one at a time.
- **Exposing inputs** converts hidden assumptions into visible parameters, so a
  wrong assumption becomes a visible wrong output, not a hidden one.
- **Pure transforms** remove context (time, I/O, randomness) so results are
  reproducible and therefore debuggable.
- **A view** forces every claim to become a concrete, inspectable mapping.
- **Verification** gives a stopping condition: you are done when the assertions
  pass — not when it "feels right".

## The five solving moves (apply when stuck)

1. **Name it** — list the nouns; every noun becomes typed state.
2. **Knob it** — turn each unknown or assumption into an input with a default.
3. **Purify it** — extract the deterministic core `(state, inputs) -> derived`;
   push all context to the edges.
4. **Render it** — draw the state and its relationships; make the invisible visible.
5. **Assert it** — write the check that must hold; make it run automatically.

Repeat until the artifact's verification panel is green.

## Worked reduction (non-numeric example)

Problem: *"Should our team adopt this new process?"*

- **State:** team size, current cycle time (days), defect rate (%), onboarding cost (person-days).
- **Inputs:** adoption fraction (0–100%), training hours per person, process efficiency gain (%).
- **Transforms:** projected cycle time, projected defect rate, net benefit = value of speed/quality − onboarding cost.
- **View:** controls for the inputs; readouts for the three projections; a break-even chart vs adoption fraction.
- **Verify:** net benefit is positive only above X% adoption; break-even matches the chart crossing zero.

The fuzzy "should we?" is now a precise question — *above what adoption fraction
does net benefit turn positive?* — with a computed answer and a check. That is
what it means to solve a question by treating it as a frontend problem.

## Non-negotiables of the reduction

- Never drop a noun for convenience; make it state (or an explicit assumption).
- Never bury an assumption; make it an input.
- Never leave the solution as prose only; render it, and verify it.
