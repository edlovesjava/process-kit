---
id: B-008
title: Templates for every tracking and docs file
milestone: M2
priority: P0
status: done
role: implementer
depends_on:
questions:
owner:
updated: 2026-10-31
---

## Goal
`templates/` mirrors the paths the scaffold writes: `CLAUDE.md` process sections with an
invariants placeholder, `project/` (WORKFLOW, process.toml, SITREP, questions, decisions,
milestones, activity, backlog README and B-001), `docs/adr/` (README, template with
Amendments), `docs/arch/` and `docs/process/` (README, review template), `docs/design/nfrs.md`
with its "How to change this register" section, and the tracking CI workflow.

## Acceptance
- [x] Every file the brief lists exists and uses only `{{PROJECT_NAME}}`, `{{APPROVER}}`, `{{DATE}}`
- [x] Examples use a neutral placeholder; no source-project noun (CI job `no-project-nouns`)
- [x] `activity.md` documents the nine columns and carries one `decided` row for the adoption
- [x] WORKFLOW.md pairs the architect and program-manager reviews at every boundary and carries the push-the-branch-first rule

## Notes
Built in the bootstrap session (D-002).
