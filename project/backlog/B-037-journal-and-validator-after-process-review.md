---
id: B-037
title: Journal clock, merge rows and three validator warnings from the M2 process review
milestone: M3
priority: P1
status: blocked
role: implementer
depends_on:
questions: Q-010
owner:
updated: 2026-11-01
---

## Goal
The tooling half of the M2 process review, once Ed answers Q-010: the `journal` skill
reads Date-time from `date -u`; the `merge-sync` skill and the operator write a merge row
in step 6; the validator warns on `decided` in a non-human row dated after the decision
row, on `done` with an unchecked box that names no item, and on `in-progress` with no
journal row that day; the process review template gains the metrics the first review
could not count; the program-manager agent treats commit times as the authority when the
journal disagrees.

## Acceptance
- [ ] `skills/journal/SKILL.md` runs `date -u +'%Y-%m-%d %H:%M'` and says how a late row marks the real time; `templates/project/activity.md` states the rule
- [ ] `skills/merge-sync/SKILL.md` and `agents/operator.md` write the merge row; `WORKFLOW.md` template step 6 names it (after the decision row)
- [ ] Three validator warnings, each stated in the template it checks and each with a test
- [ ] `templates/docs/process/0000-review-template.md` adds: items that skipped `ready`, items per PR, decision wait from raised to answered, and "count elapsed time from git"; the kit's copy follows
- [ ] `agents/program-manager.md`: commit times are the clock when the journal disagrees
- [ ] File-name case for reviews settled in both READMEs and both review items (`review-<Milestone>-<date>`)

## Notes
From `docs/process/review-M2-2026-11-01.md` B1, B3, S2, S4, O1. The WORKFLOW sentences
themselves land with Q-010's decision rows, not here. The hook test the review asks for is
B-032.
