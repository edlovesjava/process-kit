---
id: B-019
title: Add the licence Ed chooses
milestone: spec
priority: P1
status: done
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
- [x] `LICENSE` present; `plugin.json` `license` set; `claude plugin validate .` no longer reports the licence note
- [x] README mentions the licence in one line

## Notes
The brief said not to add a licence file without Ed's choice. Ed chose MIT on 2026-10-31 (Q-001, D-012).
`claude plugin validate .` (CLI 2.1.316) no longer mentions the licence; its two remaining warnings are the kit's own
`CLAUDE.md` at the plugin root (expected) and no icon, which matters only for directory submission (see B-018).
