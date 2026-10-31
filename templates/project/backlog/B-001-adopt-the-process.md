---
id: B-001
title: Adopt the process: invariants, roles, milestones, first SITREP
milestone: spec
priority: P0
status: ready
role: human
depends_on:
questions:
owner:
updated: {{DATE}}
---

## Goal
The scaffold has written the process files; this item makes them true for
{{PROJECT_NAME}}. When it is done, a fresh agent session can read `CLAUDE.md` and
`project/` and start work without asking what the rules are.

## Acceptance
- [ ] `CLAUDE.md` invariants replaced with the project's own; layout lists the code directories
- [ ] `project/process.toml` milestones match `project/milestones.md`; roles and models confirmed or changed with a decision row
- [ ] `docs/design/nfrs.md` has at least the architecture goals, even with every NFR still `gap`
- [ ] `project/SITREP.md` has a first entry saying where the project stands
- [ ] `python3 -I project/tools/check.py` passes with zero errors
- [ ] This item set to `done` with a journal row the same day

## Notes
Written by the process-kit scaffold. See process-kit `docs/tailoring.md` for what to change
and `docs/assumptions.md` for what the process takes for granted.
