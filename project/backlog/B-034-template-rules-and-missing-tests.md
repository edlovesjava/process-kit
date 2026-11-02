---
id: B-034
title: State every validator rule in its template; add the missing tests, stdlib and 3.11 checks
milestone: M3
priority: P1
status: blocked
role: implementer
depends_on:
questions: Q-009
owner:
updated: 2026-11-01
---

## Goal
Invariant 5 holds again: five validator rules the backlog README and journal template do
not state are added as Rules lines (id matches file name and is unique; `depends_on` and
`questions` name existing records; `updated` is `YYYY-MM-DD`; stale items warn; Runs and
Human turns are whole numbers and a row has nine cells), the `superseded` wording follows
Q-009, and the validator's coverage becomes measurable. Review S4, S5, S6, O3, O5.

## Acceptance
- [ ] Rules lines added to `templates/project/backlog/README.md` and `templates/project/activity.md`, mirrored in the kit's own `project/`
- [ ] The eight missing tests (five config messages, three scaffold CLI paths) plus a meta-test that parses `check.py` with `ast` and fails when an `errors`, `warnings` or `problems` message fragment appears in no test; N-004 to `met`
- [ ] `test_stdlib_only` walks `tools/` and `scripts/` with `ast` and asserts every import is in `sys.stdlib_module_names` or a sibling module; CI unit job runs on 3.11 and 3.13 as well; `templates/.github/workflows/tracking.yml` pinned to 3.11; N-001 to `met`
- [ ] `check.py` uses argparse (`--root` with no value no longer raises) and normalises CRLF front matter; tests for both
- [ ] CI noun grep covers `scripts/`, `hooks/`, `.claude-plugin/` and reads its word list from one file under `tools/tests/`

## Notes
From `docs/arch/review-M2-2026-11-01.md` S4 to S6, O3, O5. Blocked on Q-009 only for the
`superseded` sentence; the rest may start once Ed says so.
