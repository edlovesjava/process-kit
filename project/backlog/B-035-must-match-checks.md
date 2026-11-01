---
id: B-035
title: Validator warns when a "must match" stated in a template is broken
milestone: M4
priority: P2
status: idea
role: implementer
depends_on:
questions:
owner:
updated: 2026-11-01
---

## Goal
`process.toml` says `[roles]` must match the agents' `model` fields and `milestones.md`
says the milestones table must match the config, and nothing checks either. The validator
warns when `.claude/agents/<role>.md` gives a different model or when the table and the
config disagree. Candidate N-011 (review O1).

## Acceptance
- [ ] Warning per mismatch, stated in the templates that carry the "must match" sentence
- [ ] Tests for both; N-011 accepted by Ed as a register row or dropped

## Notes
From `docs/arch/review-M2-2026-11-01.md` O1. Catches the most likely tailoring slip:
changing a model in one place only.
