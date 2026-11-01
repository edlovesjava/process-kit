---
id: B-014
title: Adopt the kit in the source project
milestone: M3
priority: P1
status: blocked
role: planner
depends_on: B-011, B-012, B-030, B-033
questions:
owner:
updated: 2026-11-01
---

## Goal
The project the kit was extracted from adopts it: its validator is replaced by the kit's
copy with a `process.toml` carrying its existing roles and milestones, `program-manager`
and `activity.md` are added, the journal is backfilled from item notes, SITREP entries and
PR history (rows marked `reconstructed`), and its first process review is written. Any
friction becomes a kit item.

## Acceptance
- [ ] Source project's `check.py` passes with the kit's validator and zero errors; INDEX identical apart from the generator line
- [ ] `program-manager` agent present; `activity.md` backfilled; first process review written before its next code milestone starts
- [ ] Every gap found in the kit while adopting is a `B-` item here

## Notes
This is the source project's own activity-journal item, carried out with the kit. The
planner writes the items on both sides; the operator does the mechanical copy.
