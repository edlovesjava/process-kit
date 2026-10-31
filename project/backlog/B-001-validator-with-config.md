---
id: B-001
title: Validator reads its vocabulary from process.toml and checks the journal
milestone: M0
priority: P0
status: done
role: implementer
depends_on:
questions:
owner:
updated: 2026-10-31
---

## Goal
`tools/check.py` carries every check of the source project's validator with the hard-coded
sets (statuses, roles, milestones, priorities, stale days) moved to `project/process.toml`,
and adds the activity-journal checks: dated headings, known roles and models, fixed
outcomes, integer counts, and a warning when an item reaches `review` or `done` with no
journal row that day. Standard library only, `python3 -I`, Python 3.11 or newer.

## Acceptance
- [x] Config loaded with `tomllib`; a missing file, a malformed file, an unknown section, a bad type or a removed semantic status is an error naming the key
- [x] Every source check present: required keys, id matches file name, unique ids, unknown references, `ready` versus unmet dependencies and open questions, `blocked` needs a blocker, owner on `in-progress` and `review`, stale warning, question statuses, INDEX generation only when error-free
- [x] Journal checks per the source project's proposal; `journal.enabled = false` turns them off
- [x] `run(root, write, today)` is importable and pure apart from `INDEX.md`; `main` prints `warning:` and `error:` lines and a `key=value` summary; exit 1 on errors
- [x] Unit tests for every check (`tools/tests/test_check.py`, 31 cases with the scaffold's) pass under `python3 -I -m unittest`

## Notes
Built in the bootstrap session (D-002). TOML chosen over JSON for comments and hand-editing
(D-003). The documentation table at the top of `activity.md` is skipped because it precedes
the first `##` heading; a table under a non-date heading is an error.
