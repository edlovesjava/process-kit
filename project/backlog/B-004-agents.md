---
id: B-004
title: Eight role agents, generalised, with program-manager
milestone: M1
priority: P0
status: done
role: implementer
depends_on:
questions:
owner:
updated: 2026-10-31
---

## Goal
`agents/` holds researcher, planner, project-manager, program-manager, implementer,
reviewer, architect and operator, each with frontmatter `name`, `description`, `tools`,
`model` and a body that says what it reads first, what it writes, and what it never does.
Every source-project reference is gone; the role contracts are intact.

## Acceptance
- [x] Seven source roles generalised: no product, system, build tool, fixture or person named
- [x] `program-manager` per the source proposal: owns `WORKFLOW.md` and the journal, reviews the process at each milestone boundary alongside the architect, proposes, never decides, never edits code; Opus; tools Read, Grep, Glob, Bash, Write
- [x] Models match `templates/project/process.toml` `[roles]`
- [x] `claude plugin validate .` passes with the agents loaded
- [x] Each agent ends by reporting what the lead needs for a journal row

## Notes
Built in the bootstrap session (D-002). Model mapping is D-009.
