---
id: B-006
title: PostToolUse hook runs the validator after edits under project/
milestone: M1
priority: P1
status: done
role: implementer
depends_on: B-001
questions:
owner:
updated: 2026-10-31
---

## Goal
`hooks/hooks.json` registers one `PostToolUse` hook on Write and Edit that runs
`scripts/check_hook.py`. The script reads the hook payload, and when the edited file is
under `<cwd>/project/` and `process.toml` exists, runs the project's validator with
`--no-write`; on errors it exits 2 so the output reaches Claude. Anything else exits 0.

## Acceptance
- [x] No-op outside kit projects; never raises (catch-all)
- [x] Prefers the project's `project/tools/check.py`, falls back to the kit's
- [x] `claude plugin validate .` passes
- [ ] Unit test feeding the script payloads for the three cases (N-007 gap; follow-up item welcome)

## Notes
Built in the bootstrap session (D-002). D-008. Journal hooks are Q-003 / B-016.
