---
id: B-038
title: Should-fix tooling from the M2 process review: merge rows, two validator warnings, review-template metrics
milestone: M3
priority: P1
status: blocked
role: implementer
depends_on: B-037
questions: Q-010
owner:
updated: 2026-11-02
---

## Goal
The should-fix half of `docs/process/review-M2-2026-11-01.md`, once Ed decides W6 to W8
in Q-010: the validator warns on `done` with an unchecked acceptance box that names no
item (S4) and on `in-progress` with no journal row that day (S2); a row that changes an
item's status names one item (W8), stated in the journal template; the process review
template gains the metrics the first review could not count (O1: items that skipped
`ready`, items per PR, decision wait from raised to answered, "count elapsed time from
git"); the review file-name case is settled in both READMEs.

## Acceptance
- [ ] Two validator warnings, each stated in the template it checks, each with a test
- [ ] `templates/project/activity.md` and the journal skill: one item per status-changing row (W8), batches allowed for new `idea` items, questions and decisions
- [ ] `templates/docs/process/0000-review-template.md` and the kit's copy carry the new metric rows
- [ ] `docs/arch/README.md`, `docs/process/README.md` and the two review skills agree on `review-<Milestone>-<date>`
- [ ] W6 (interim id rule) recorded in `WORKFLOW.md` if Ed adopts it, with a decision row; `--next-id` stays with B-028

## Notes
Split from B-037 on 2026-11-02 when Ed fixed the blocking findings first. S1 (id
collisions) is B-028's; the hook test is B-032; session rows are B-027's.
