---
id: B-011
title: Architecture review of the kit at the M2 boundary (covers M0 to M2)
milestone: M2
priority: P0
status: review
role: architect
depends_on: B-001, B-002, B-003, B-004, B-005, B-006, B-007, B-008, B-009, B-010
questions:
owner: lead session (PR for B-011)
updated: 2026-11-01
---

## Goal
The architect reviews the kit as built against its invariants, ADR-0001 and
`docs/design/nfrs.md`, and writes `docs/arch/review-m2-<date>.md`. First review, so it
covers the whole bootstrap. Its blocking findings gate M3 (D-002).

## Acceptance
- [x] Review follows `docs/arch/0000-review-template.md`: scope, goals scorecard, NFR status, ranked findings, looking ahead to M3 and M4, proposals as records
- [x] Every NFR row re-evaluated with evidence; `gap` rows get a proposed fitness function
- [x] Proposals folded into `project/` by the lead; row added to `docs/arch/README.md`
- [x] Journal row with role `architect`

## Notes
Run with the `arch-review` skill. Written as `docs/arch/review-M2-2026-11-01.md` (the
README's `review-<milestone>-<date>` form; this item's `m2` was the slip). Folded on
2026-11-01: ADR-0002, Q-007 to Q-009, B-030 to B-036, dependency edits on B-014, B-015,
B-018, B-020, B-028, NFR register evidence and two candidate rows. `done` follows the merge. Things the bootstrap session already knows are weak:
no test for the hook (N-007), `claude plugin validate` not in CI (N-005), no update path
for copied validator and agents (ADR-0001 consequences).
