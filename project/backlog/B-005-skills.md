---
id: B-005
title: Skills for the recurring motions
milestone: M1
priority: P0
status: done
role: implementer
depends_on: B-004
questions:
owner:
updated: 2026-10-31
---

## Goal
`skills/<name>/SKILL.md` for: scaffold, session-start, backlog-item, question, adr,
decision, sitrep, status, check, merge-sync, arch-review, process-review, journal. Each
reads as prose a human could follow by hand, names the files it touches and ends with the
validator.

## Acceptance
- [x] Thirteen skills, each with `description` (and `argument-hint` where arguments make sense); `disable-model-invocation: true` on scaffold, arch-review and process-review
- [x] merge-sync exists specifically to close the tracking-lag and missed-issue-close findings from the source project
- [x] session-start begins with "push the branch first"
- [x] No command files (`commands/`), per D-007
- [x] `claude plugin validate .` passes

## Notes
Built in the bootstrap session (D-002). Skills are not copied into adopting projects
(ADR-0001); `WORKFLOW.md` states the same motions in prose for cloud sessions.
