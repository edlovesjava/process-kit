---
id: B-013
title: Ed accepts, amends or rejects ADR-0001 and confirms the researcher's decision rows
milestone: spec
priority: P0
status: ready
role: human
depends_on:
questions:
owner:
updated: 2026-10-31
---

## Goal
ADR-0001 (plugin for behaviour, scaffold for files) moves from Proposed to Accepted or
Rejected, and decision rows D-002 to D-009 and D-011, made by the bootstrap session, get
Ed's confirmation or a superseding row.

## Acceptance
- [ ] ADR-0001 status set and README row updated
- [ ] Each `By: researcher` row in `decisions.md` has "confirmed by Ed <date>" in Notes or is superseded
- [ ] Journal row with role `human`, outcome `decided`

## Notes
Together with Q-001 to Q-005 these are the approver's inputs the kit waits on.
