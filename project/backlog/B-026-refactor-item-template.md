---
id: B-026
title: Refactor item template with the byte-identical acceptance line
milestone: later
priority: P2
status: idea
role: implementer
depends_on: B-025
questions:
owner:
updated: 2026-10-31
---

## Goal
A refactor is an item whose acceptance test is that nothing observable changed. The kit
ships a `refactor` item template that carries the line "No behaviour change: golden
files, fitness tests and CLI contract byte-identical", the validator requires that line
on any item with `kind: refactor` (a warning for items older than the check), and the
tailoring docs say how a project proves it: golden fixtures, fitness tests, a recorded
CLI contract, whichever the project has.

## Acceptance
- [ ] `templates/project/backlog/` gains a refactor item template with the acceptance line, and `project/backlog/README.md` (template and the kit's own) names it
- [ ] `tools/check.py`: an item with `kind: refactor` and no byte-identical acceptance line is an error when `updated` is on or after the check's introduction, a warning before; tests for both; the rule is stated in the template it checks
- [ ] `docs/tailoring.md` gains a note on proving "no behaviour change" (golden fixtures, fitness tests, CLI contract) and how the architect's XS, S, M sizing of refactor findings is used
- [ ] The `backlog-item` skill mentions the `kind` key and the refactor template
- [ ] Scaffold smoke test covers the new template; `check.py` passes on the kit's own `project/`

## Notes
From the source project's first two refactor items under its development method:
moving composition into the framework configuration so command classes carry no
persistence imports, and domain-first packages with ports and adapters behind an ADR.
Both proved "no behaviour change" with golden fixtures and fitness tests. Depends on
B-025 for the `kind` key.
