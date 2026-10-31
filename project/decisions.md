# Decision log

Non-architectural decisions: process, scope, tooling. Architecture decisions go in
`docs/adr/` and are only linked from here. Append-only: a changed mind is a new entry
that supersedes the old one (fill the Supersedes column and set the old row's status to
`superseded`). Any change to `project/process.toml` gets a row here.

Rows marked `By: researcher` were made by the session that built the kit and stand until
Ed confirms or overrules them; Ed's confirmation is a note in the Notes column, not a new row.

| ID | Date | Decision | Status | By | Supersedes | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| D-001 | 2026-10-31 | The kit tracks its own work with its own templates and validator (`project/`, `tools/check.py`), so every kit change is dogfooded | decided | Ed (brief), researcher | | The kit runs `tools/check.py` from the root rather than a copy under `project/tools/`, to keep one validator in the repository. |
| D-002 | 2026-10-31 | Bootstrap exception: M0 to M2 were built by the lead session in one pass, without the role split, reviews or per-item PRs, before the kit's process could exist. From M3 the kit follows its own process; the M0 to M2 boundary reviews are owed together at the M2 boundary (B-011, B-012) | decided | researcher | | Journal rows for the bootstrap carry `bootstrap` in the Problem column. |
| D-003 | 2026-10-31 | The validator's vocabulary (statuses, priorities, milestones, roles and models, question statuses, journal models and outcomes, stale period, approver, issue mirroring) lives in `project/process.toml`, read with `tomllib` | decided | researcher | | TOML over JSON: comments are allowed (every key is annotated in place), the file is hand-edited by humans, and `tomllib` is standard library from Python 3.11. Read-only is enough because the scaffold writes it once from a template. |
| D-004 | 2026-10-31 | `ready`, `blocked`, `in-progress`, `review`, `done` and `dropped` are semantic statuses the validator reasons about and may not be removed from the config; other statuses may be added | decided | researcher | | Keeps the transition checks meaningful while leaving room for `parked` and the like. |
| D-005 | 2026-10-31 | The adopting project owns a copy of the validator at `project/tools/check.py`, written by the scaffold; the kit does not run it from the plugin directory | decided | researcher | | CI and cloud sessions then need nothing installed; the project may extend its copy; kit updates merge by hand. ADR-0001. |
| D-006 | 2026-10-31 | The scaffold copies `agents/` into the project's `.claude/agents/` by default (`--no-agents` to skip) | decided | researcher | | Cloud sessions do not load project-scope plugins (verified in the plugin documentation); the source project runs in cloud sessions. ADR-0001. |
| D-007 | 2026-10-31 | Recurring motions are skills (`skills/<name>/SKILL.md`), not commands; `commands/` is not used | decided | researcher | | The plugin documentation calls commands the older format and says to prefer skills. |
| D-008 | 2026-10-31 | One hook ships: `PostToolUse` on Write and Edit runs the validator with `--no-write` when the edited file is under `project/`, reporting errors back; it exits 0 for any project without `process.toml`. No journal hook until Q-003 is answered | decided | researcher | | Hooks fire in every session where the plugin is enabled, so the hook is a no-op outside kit projects. |
| D-009 | 2026-10-31 | Default role-to-model mapping carried from the source project: research on the lead model (`inherit`), planning, project and program management, review and architecture on Opus, implementation on Sonnet, operations on Haiku | decided | researcher | | Source decisions D-003 and D-007 there. Tailorable per `docs/tailoring.md`. |
| D-010 | 2026-10-31 | The program-manager role and the activity journal are part of the kit from the start, as the source project's B-027 proposed | decided | Ed (brief), researcher | | Journal format: one `##` per UTC day, nine columns, newest at the bottom; see `templates/project/activity.md`. |
| D-011 | 2026-10-31 | The repository is its own plugin marketplace (`.claude-plugin/marketplace.json`, one entry, source `./`) until Q-002 is answered | decided | researcher | | Lets `claude plugin marketplace add edlovesjava/process-kit` work today without a second repository. |
