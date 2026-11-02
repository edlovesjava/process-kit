# Architecture reviews

One review per milestone boundary, written by the architect agent after a milestone's
code is complete and before the next starts. Each review re-evaluates the goals and the
NFR register in `docs/design/nfrs.md`, ranks findings, and proposes records (ADRs,
questions, backlog items) that the lead folds into `project/` and `docs/adr/`.
Ed decides on every proposal. The program manager's process review of the same
boundary lives in `docs/process/`.

Files: `review-<milestone>-<yyyy-mm-dd>.md`, from `0000-review-template.md`. The review is
a snapshot; its proposals live on in the tracking files, so an old review is never edited.

| Review | Covers | Outcome |
| --- | --- | --- |
| [review-M2-2026-11-01.md](review-M2-2026-11-01.md) | M0 to M2 as built at `main` 90b6346, first review (B-011) | 2 blocking, 6 should-fix, 5 opportunities; NFRs: no status moves, N-007 reword and N-010, N-011 proposed; records: ADR-0002 (Proposed), Q-007 to Q-009, B-030 to B-036, edits to B-014, B-015, B-018, B-020, B-028 |
