---
id: B-018
title: Distribution path per Q-002
milestone: M4
priority: P1
status: ready
role: implementer
depends_on:
questions: Q-002
owner:
updated: 2026-10-31
---

## Goal
Q-002 is answered (D-013): the plugin from the in-repo marketplace carries behaviour, the scaffold
copies the customisable assets into the project, and the kit must be able to update and tune those
copies. This item builds the update half: a version tag and `version` bump discipline, and a
`process-kit:update` skill that diffs a project's copied validator, agents, templates and workflow
against the plugin's and offers each change for the project to take or keep. Directory submission
is not decided; it would need an icon (the one remaining `claude plugin validate` warning).

## Acceptance
- [ ] `process-kit:update` skill: diff per copied path, never overwrites, reports what the project has changed
- [ ] README install section updated
- [ ] A tagged release the marketplace entry can pin

## Notes
ADR-0001 consequences name the update path as the open cost of the copy approach.
