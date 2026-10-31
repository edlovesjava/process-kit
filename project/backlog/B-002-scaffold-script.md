---
id: B-002
title: Scaffold script copies the process into a project
milestone: M0
priority: P0
status: done
role: implementer
depends_on: B-001
questions:
owner:
updated: 2026-10-31
---

## Goal
`tools/scaffold.py --target DIR --name NAME [--approver NAME]` copies `templates/` into a
repository with `{{PROJECT_NAME}}`, `{{APPROVER}}` and `{{DATE}}` substituted, copies the
validator to `project/tools/check.py` and the agents to `.claude/agents/`, never overwrites
without `--force`, and leaves an existing `CLAUDE.md` alone by writing the process sections
beside it for merging.

## Acceptance
- [x] Fresh scaffold then `check.py` in the target: zero errors, `INDEX.md` written
- [x] Second run without `--force` writes nothing and lists every skipped path
- [x] Existing `CLAUDE.md` untouched; sections written to `project/CLAUDE-process-sections.md` with a note
- [x] `--no-agents` skips the agent copy and says so; `--dry-run` writes nothing
- [x] Output is `key=value` lines ending with the next command to run

## Notes
Built in the bootstrap session (D-002). Copy rules are D-005 and D-006, reasoning in ADR-0001.
