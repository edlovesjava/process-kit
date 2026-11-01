---
id: B-032
title: Hook finds the project root from the edited file and gets a test suite
milestone: M3
priority: P0
status: ready
role: implementer
depends_on:
questions:
owner:
updated: 2026-11-01
---

## Goal
`scripts/check_hook.py` takes the project root from the session's working directory, so
an edit under `project/` made after the session has moved into a subdirectory is never
validated, silently (review S1, verified). The hook walks up from the edited file to the
first directory holding `project/process.toml`, ignores cwd, and gains
`tools/tests/test_hook.py`. N-007 moves to `met`.

## Acceptance
- [ ] Root found by walking up from the edited file's parents; cwd not consulted
- [ ] `tools/tests/test_hook.py` runs the script as a subprocess with: clean edit, broken item (exit 2), relative path, edit outside `project/`, subdirectory cwd (exit 2), missing `file_path`, non-JSON, empty stdin, `tool_input: null`, a list payload, a repository without `process.toml` (exit 0)
- [ ] `hooks/hooks.json` matcher checked against the file-changing tool names the current CLI offers; widened if needed
- [ ] N-007 in `docs/design/nfrs.md` reworded as the review proposes and set `met` with the test named
- [ ] `claude plugin validate .` still passes

## Notes
From `docs/arch/review-M2-2026-11-01.md` S1; closes the open box left in B-006. B-015
depends on this item because its loop expects the hook to report an error.
