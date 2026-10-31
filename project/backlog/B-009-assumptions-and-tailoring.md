---
id: B-009
title: docs/assumptions.md and docs/tailoring.md
milestone: M2
priority: P0
status: done
role: researcher
depends_on:
questions:
owner:
updated: 2026-10-31
---

## Goal
`docs/assumptions.md` lists every assumption the process makes, each marked tailorable or
fixed with the reason. `docs/tailoring.md` says what to change for a new project and where,
and what must not change without a decision row.

## Acceptance
- [x] Assumptions cover at least: one approver, repo Markdown as truth, ADR beats spec, one item per PR, reviews gate milestones, agents propose, push branch first, warning-clean and CI untouched, small commits, interfaces documented before merge
- [x] Tailoring covers roles and models, milestones, invariants, review cadence, issue mirroring, agent persona, and names what is a fork rather than a tailoring

## Notes
Built in the bootstrap session (D-002).
