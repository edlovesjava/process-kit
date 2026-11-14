---
id: B-037
title: Fix the M2 process review's blocking findings: journal clock, review and done, decided rows
milestone: M3
priority: P0
status: review
role: implementer
depends_on:
questions:
owner: lead session (PR for B-037)
updated: 2026-11-02
---

## Goal
The three blocking findings of `docs/process/review-M2-2026-11-01.md`, as Ed decided on
2026-11-02 (D-017 to D-021): journal rows carry the clock time, `review` means an open PR
and `done` follows the merge, tracking-only changes travel light, and only a human row
decides, with a validator warning behind it. Prose first: WORKFLOW (template and kit),
the journal template, the backlog README, the journal and merge-sync skills, the
implementer and program-manager agents; then the check and its test.

## Acceptance
- [x] `templates/project/WORKFLOW.md` and `project/WORKFLOW.md`: the journal rule carries the clock and the human-only `decided`; new rules "Review means an open PR" and "Tracking-only changes travel light"; step 4 never sets `done`, step 6 sets it only in the merge-sync
- [x] `templates/project/activity.md` and the kit's copy state the clock rule, `late: HH:MM`, and human-only `decided`; `skills/journal/SKILL.md` runs `date -u +'%Y-%m-%d %H:%M'`
- [x] `check.py` warns on `decided` in a row whose role is not in `journal.decided_roles` and whose day is on or after `journal.decided_roles_from`; a bad date is a config problem; both keys in the `process.toml` template (`{{DATE}}`) and the kit's (2026-11-02); test `test_decided_on_a_non_human_row_warns_from_the_configured_date`; `docs/tailoring.md` documents the keys
- [x] `skills/merge-sync/SKILL.md` is the only place `done` is set and adds the approver's merge row; `agents/implementer.md` never sets `done` and never records `decided`; `agents/program-manager.md` treats commit times as the clock; `.claude/agents/` copies follow
- [x] B-014 and B-015 depend on B-013 (done in B-012's fold); D-018 closes D-002's open end
- [x] Scaffold smoke test and `claude plugin validate .` pass; the kit's own `check.py` reports zero warnings

## Notes
From `docs/process/review-M2-2026-11-01.md` B1, B2, B3; Q-010 progress line of 2026-11-02.
The should-fix tooling (merge rows as a validator check, `done` with an unchecked box,
`in-progress` without a row, review-template metrics, file-name case) is B-038, blocked on
the rest of Q-010. Merge rows are written by hand from this PR on (merge-sync skill).
