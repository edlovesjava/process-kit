# Architecture goals and non-functional requirements

The goals are what the architecture is for. The NFRs are how we know we are meeting them;
each has a fitness function (a test, a measurement or a check) and a status. The architect
agent re-evaluates this register at every milestone boundary (see `docs/arch/`), and a
change to a goal or an NFR is a decision for {{APPROVER}}, recorded in
`project/decisions.md` or an ADR.

Statuses: `met` (fitness function exists and passes), `partial` (met in part or by
convention only), `gap` (no fitness function yet), `pending <Mn>` (the milestone that
delivers it).

## Architecture goals

| Goal | Statement | Source |
| --- | --- | --- |
| G1 Name | One sentence a reviewer can test the design against. | Invariant N; ADR-NNNN |
| G2 Maintainable by agents | Small pure modules, literate code, every interface documented, one item per PR, warning-clean. | CLAUDE.md conventions |

## NFR register

| ID | Requirement | Fitness function | Evidence ({{DATE}}) | Status |
| --- | --- | --- | --- | --- |
| N-001 | No secret or token appears in logs or in the repository | a test, and a CI grep for secret shapes | not built | gap |
| N-002 | Every test runs offline; CI needs no network beyond package registries | test suite; CI config | not built | gap |
| N-003 | Build is warning-clean; forbidden dependencies fail the build | compiler flags; a dependency check task | not built | gap |

## How to change this register

- A new NFR or a changed threshold is a decision (D-NNN) or an ADR; the architect proposes,
  {{APPROVER}} decides.
- The architect's milestone review re-evaluates every row and may move a status; it does
  not add rows on its own.
- When a `gap` gains a fitness function, link the test or check in the Fitness function
  column and set the status from its result.
