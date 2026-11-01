---
id: B-015
title: Scaffold a fresh project and run one full item loop
milestone: M3
priority: P1
status: blocked
role: implementer
depends_on: B-011, B-012, B-013, B-030, B-032
questions:
owner:
updated: 2026-11-01
---

## Goal
A new, small repository adopts the kit from scratch with the `scaffold` skill, fills B-001
(adopt the process), then takes one real item through `ready`, `in-progress`, `review` and
`done` with the role agents, a PR, `merge-sync` and journal rows. The point is to find what
the templates and skills assume that a fresh project does not have.

## Acceptance
- [ ] `check.py` passes in the new project at every step; the hook reported at least one error during the loop or the reason it did not is recorded
- [ ] Every friction point is a kit item or a tailoring-doc change
- [ ] The adopting project's time from scaffold to first merged item is in the journal

## Notes
Pick a project with no existing process files so the CLAUDE.md path is exercised, and one
with an existing CLAUDE.md for the merge-sections path if a second candidate exists.
