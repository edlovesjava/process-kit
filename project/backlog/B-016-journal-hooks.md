---
id: B-016
title: Journal rows from hooks
milestone: M4
priority: P2
status: idea
role: implementer
depends_on:
questions: Q-003
owner:
updated: 2026-10-31
---

## Goal
Q-003 chose hand-written rows for the proof-of-concept phase and a later competitive design of
hand-written against hook-appended rows (D-014). This item is that comparison: a `SubagentStop` hook records each dispatch (JSONL under
`project/activity/` or a direct table row with blank judgement columns) and the operator or
lead completes it; the validator learns the chosen shape.

## Acceptance
- [ ] Both shapes (hand-written; hook-appended, option b or c) run side by side for a milestone and the process review compares completeness and the cost of completing rows
- [ ] Validator tolerates and checks the new shape; tests added
- [ ] `docs/tailoring.md` journal section updated

## Notes
Not before a process review has read at least one milestone of hand-written rows (D-014).
