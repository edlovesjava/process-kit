---
id: B-016
title: Journal rows from hooks
milestone: M4
priority: P2
status: blocked
role: implementer
depends_on:
questions: Q-003
owner:
updated: 2026-10-31
---

## Goal
If Q-003 chooses a hook, a `SubagentStop` hook records each dispatch (JSONL under
`project/activity/` or a direct table row with blank judgement columns) and the operator or
lead completes it; the validator learns the chosen shape.

## Acceptance
- [ ] As decided in Q-003
- [ ] Validator tolerates and checks the new shape; tests added
- [ ] `docs/tailoring.md` journal section updated

## Notes
Not built until a process review shows hand-written rows being missed (Q-003 option a).
