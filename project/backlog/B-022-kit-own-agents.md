---
id: B-022
title: The kit's own repository carries .claude/agents/, seeded from agents/
milestone: spec
priority: P1
status: done
role: operator
depends_on:
questions: Q-004
owner:
updated: 2026-10-31
---

## Goal
Per Q-004 (D-015), `.claude/agents/` exists in this repository as a copy of `agents/`, so a
cloud session working on the kit has the role agents even though it cannot load the plugin.
The copy is the kit's own tailored instance and may diverge from `agents/` later; until it
is tuned it is verbatim.

## Acceptance
- [x] `.claude/agents/` holds the eight role files, identical to `agents/` at seeding
- [x] Q-004 answered, D-015 recorded, SITREP and README no longer say the kit has no agents in the cloud

## Notes
Tuning the copy to the kit's own workflow (for example an implementer that knows the
validator and scaffold tests) is a later item; each change to a role's model or tools is a
decision row (docs/tailoring.md).
