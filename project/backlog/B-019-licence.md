---
id: B-019
title: Add the licence Ed chooses
milestone: spec
priority: P1
status: blocked
role: human
depends_on:
questions: Q-001
owner:
updated: 2026-10-31
---

## Goal
A `LICENSE` file at the root and the matching SPDX id in `.claude-plugin/plugin.json`
`license`, per Q-001.

## Acceptance
- [ ] `LICENSE` present; `plugin.json` `license` set; `claude plugin validate .` no longer reports the licence note
- [ ] README mentions the licence in one line

## Notes
The brief said not to add a licence file without Ed's choice.
