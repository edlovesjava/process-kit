---
id: B-030
title: Scaffold writes a lock file with per-path hashes and gains --only for targeted --force
milestone: M3
priority: P0
status: blocked
role: implementer
depends_on: B-031
questions:
owner:
updated: 2026-11-01
---

## Goal
Every scaffolded copy is recorded, so a later update can tell what the project changed
from what the kit changed. The scaffold writes `project/process-kit.lock` (TOML: kit
`version` from `plugin.json`, the kit commit when available, a sha256 per copied path),
`--only PATH` (repeatable) limits `--force` to chosen paths, and `--force` without
`--only` is refused once a lock exists. ADR-0002 option B; review B1.

## Acceptance
- [ ] `tools/scaffold.py` writes the lock on a fresh scaffold and updates the hashes of the paths it writes under `--force --only`
- [ ] `--force` with no `--only` is refused when a lock exists, with a message naming `--only`; `--dry-run` shows what `--only` would write
- [ ] Tests `test_scaffold_writes_lock_with_hashes`, `test_force_only_limits_paths`, `test_force_without_only_refused_when_locked`
- [ ] `docs/assumptions.md` A18 and `docs/tailoring.md` say the lock exists and how `--only` is used; the scaffold smoke test in CI checks the lock is written
- [ ] The kit's own `project/` gets a lock for the files it copied from its templates, or a note why not

## Notes
From `docs/arch/review-M2-2026-11-01.md` B1. Blocked on Ed accepting ADR-0002 (B-031).
B-014, B-015 and B-018 depend on this item.
