---
id: B-017
title: Plugin evals for the skills
milestone: M4
priority: P2
status: idea
role: implementer
depends_on: B-015
questions:
owner:
updated: 2026-10-31
---

## Goal
An eval suite (`claude plugin eval`) with one case per skill that checks the skill produces
the expected file change in a scaffolded project: a valid item, a valid question, a journal
row the validator accepts, a SITREP entry at the top.

## Acceptance
- [ ] Eval cases under `evals/`, runnable locally; CI if the CLI becomes available there
- [ ] Each case asserts with `check.py` rather than by string match where possible

## Notes
Depends on seeing the skills used in B-015 first, so the cases test real failure modes.
