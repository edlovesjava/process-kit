---
id: B-033
title: Optional project/tools/check_local.py loaded by the validator
milestone: M3
priority: P1
status: blocked
role: implementer
depends_on:
questions: Q-007
owner:
updated: 2026-11-01
---

## Goal
A project adds its own checks without editing its copy of `check.py`. `run()` loads
`project/tools/check_local.py` when present (`importlib.util.spec_from_file_location`,
standard library, works under `-I`) and calls `check(root, cfg, result)`. The scaffold
never writes the file. Review S3; ADR-0002.

## Acceptance
- [ ] `check.py` loads the local module when present and ignores its absence; an exception in it is reported as an error naming the file, not a traceback
- [ ] Test with a local check that adds one error and one that adds a warning
- [ ] `docs/tailoring.md` Validator section says to extend there, not in the copy; the backlog README template does not need to change
- [ ] The kit's own `project/` carries no `check_local.py` unless it needs one

## Notes
From `docs/arch/review-M2-2026-11-01.md` S3. Blocked on Q-007. B-014 depends on this item
because the source project has checks the kit lacks.
