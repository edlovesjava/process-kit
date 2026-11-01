---
id: B-020
title: Run claude plugin validate --strict in CI
milestone: M4
priority: P2
status: idea
role: operator
depends_on:
questions: Q-008
owner:
updated: 2026-11-01
---

## Goal
CI installs the Claude Code CLI (npm) and runs `claude plugin validate . --strict` so a
manifest, agent or skill regression fails the PR, closing NFR N-005.

## Acceptance
- [ ] A fourth CI job; passes on main
- [ ] N-005 moved to `met` with the job as evidence

## Notes
Check whether the CLI runs validation without authentication in CI before committing to it.
Amended 2026-11-01 from the M2 architecture review (S2): `--strict` always fails on the
kit's own root `CLAUDE.md`; build this per Q-008 (`--json` with a one-entry allowlist is the
recommendation), never by weakening the check.
