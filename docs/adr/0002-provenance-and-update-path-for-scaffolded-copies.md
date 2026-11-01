# ADR-0002: Provenance and update path for scaffolded copies

- **Status:** Proposed
- **Date:** 2026-11-01
- **Deciders:** Ed
- **Questions:** Q-007 (how a project extends its validator)
- **Supersedes:** none; refines the "Harder" consequence of ADR-0001

## Context

ADR-0001 copies the validator, the agents, the tracking templates and the workflow into
the adopting project, which then owns them. Its consequence says updates arrive "by
`scaffold --force` on chosen paths, or a diff", and D-013 makes updating and tuning those
copies a requirement. The M2 architecture review (`docs/arch/review-M2-2026-11-01.md`,
B1 and S3) found that neither exists: the scaffold records nothing about what it wrote,
`--force` has no path filter and would rewrite every file including `activity.md`,
`decisions.md` and `questions.md`, and the only way to add a project check is to edit the
copy, which forks it. M3 creates the first two adoptions, so the decision is needed now.

## Options

### Option A: leave it to a diff
No record at scaffold time; an update skill diffs the project's copies against the
plugin's. Cheap now. A two-way diff cannot tell "the project changed this" from "the kit
changed this", so every update is a hand merge, and the two M3 adoptions are re-baselined
by hand later.

### Option B: a lock file as the merge base, targeted force, a local-checks seam
The scaffold writes `project/process-kit.lock` (TOML; kit `version` from `plugin.json`,
the kit commit when available, a sha256 per copied path). `scaffold --only PATH`
(repeatable) limits `--force` to chosen paths, and `--force` without `--only` is refused
once a lock exists. A later update skill reports a three-way comparison (lock, project,
kit) and never overwrites a file whose hash differs from the lock. Project-specific checks
go in an optional `project/tools/check_local.py` that `check.py` loads when present and
the scaffold never writes, so the copy of the validator stays updatable.

### Option C: no copies to update
Move the validator and agents back into the plugin. Rejected by ADR-0001: cloud sessions
and CI need the files in the repository.

## Decision

Proposed: Option B. The lock costs one small file per project and makes every later update
mechanical; without it, D-013 cannot be met for the projects adopted in M3.

## Consequences

- Easier: B-018 (distribution and update) has a merge base; the `session-start` or
  `check` skill can report a copy whose hash differs from both the lock and the plugin
  (review O4); a project extends its validator without forking it.
- Harder: one more file in `project/`; the scaffold and its tests grow; the lock must be
  regenerated when the update skill writes a file.
- Work created: B-030 (lock and `--only`), B-033 (`check_local.py` seam, after Q-007);
  B-014, B-015 and B-018 depend on B-030. A18 in `docs/assumptions.md` and
  `docs/tailoring.md` say the lock exists and what `--only` does.
- Revisit if cloud sessions load project-scope plugins (ADR-0001's own revisit clause).

## Amendments

None.
