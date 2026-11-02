# Questions register

Every open question in one place. Anyone (human or agent) adds one; only Ed or an
accepted ADR closes one. Keep the format exactly: `check.py` reads the `## Q-NNN`
headings and the `Status` line.

Statuses: `open`, `answered`, `superseded` (see `process.toml`). Tags: `process`,
`scope`, `plugin`, `legal`.

Format:

```
## Q-NNN Short question
- **Status:** answered
- **Tags:** process
- **Raised:** 2026-10-31 by researcher, in docs/... section
- **Blocks:** B-001
- **Why it matters:** one or two sentences
- **Options:** (optional) a, b, c with the recommendation marked
- **Answer:** (when answered) what was decided, by whom, where recorded
```

Progress on an open question goes in dated `- **Progress (date):**` lines between
Options and Answer, so the history stays with the question.

---

## Q-001 Which licence does the kit carry?
- **Status:** answered
- **Tags:** legal
- **Raised:** 2026-10-31 by researcher, while building the kit (the brief said not to add a LICENSE file)
- **Blocks:** B-019
- **Why it matters:** The repository is public. Without a licence nobody else may legally use or adapt the kit, and `claude plugin validate` reports the missing licence as a directory warning. The plugin manifest's `license` field (an SPDX id) is where Claude Code reads it.
- **Options:** (a) MIT: shortest, permissive, usual for tooling, recommended if the intent is "use it freely". (b) Apache-2.0: permissive with an explicit patent grant and a NOTICE mechanism; usual for larger projects. (c) CC-BY-4.0 for the prose plus MIT for the code: precise but two licences for one repository. (d) No licence: all rights reserved; fine while the kit is only Ed's.
- **Answer:** MIT (option a). Decided by Ed on 2026-10-31 in the session chat; recorded as D-012. `LICENSE` at the root and `license` in `.claude-plugin/plugin.json` added under B-019.

## Q-002 How is the kit distributed to a project?
- **Status:** answered
- **Tags:** plugin, process
- **Raised:** 2026-10-31 by researcher, from the plugin documentation read while building the kit
- **Blocks:** B-018
- **Why it matters:** A cloud session (claude.ai/code) does not load project-scope plugins, so the plugin alone does not reach the sessions the source project runs. The scaffold already copies the agents into `.claude/agents/` for that reason (D-006). The question is what the plugin adds and how a project installs it.
- **Options:** (a) The repository is its own marketplace (`.claude-plugin/marketplace.json` lists the plugin with source `./`), so `claude plugin marketplace add edlovesjava/process-kit` then `claude plugin install process-kit@process-kit --scope project` works for local and desktop sessions; cloud sessions rely on the copied agents and the project's own `tools/check.py`; recommended, already in place (D-011). (b) A separate marketplace repository listing this one; only worth it with a second plugin. (c) Upload to the claude.ai organisation library so cloud sessions get it; needs a claude.ai organisation plan and verification that it serves Claude Code cloud sessions (verify). (d) Submit to Anthropic's directory; needs a licence (Q-001), an icon and a review.
- **Answer:** Option (a), made permanent, plus the copy half: the kit installs as a plugin from its own in-repo marketplace for behaviour, and the scaffold copies the assets a project customises (tracking templates, workflow, agents, validator) into the project, which owns them. The kit is to be configurable to update and tune those copies after the first scaffold. Decided by Ed on 2026-10-31 in the session chat; recorded as D-013 (supersedes the interim D-011). B-018 carries the update path and version tagging and is now `ready`.

## Q-003 Are journal rows written by hand, or appended by hooks?
- **Status:** answered
- **Tags:** process, plugin
- **Raised:** 2026-10-31 by researcher, from the source project's item on the activity journal
- **Blocks:** B-016
- **Why it matters:** The journal is only as good as its completeness. Hand-written rows depend on the lead remembering (the validator warns when a status change has no row, which catches the two statuses that matter most, not every dispatch). Hooks would catch every subagent run but produce rows without the judgement columns (runs, outcome, problem, resolution), so a human or the operator still has to summarise.
- **Options:** (a) Hand-written rows via the `journal` skill, with the validator's warning as the safety net; revisit when a process review shows rows being missed; recommended as the start, matching the source project's own proposal. (b) A `SubagentStop` hook appends a JSONL line per dispatch under `project/activity/`, and the operator summarises into the table at session end; complete but two formats to keep. (c) A `SubagentStop` hook writes the table row directly with `outcome` blank for the lead to fill; one format, but a half-filled row the validator must tolerate.
- **Answer:** Hand-written rows (option a) for the early, proof-of-concept phase. Later, hand-written and hook-appended rows (options b and c) are to be tried side by side in a competitive design and compared. Decided by Ed on 2026-10-31 in the session chat; recorded as D-014. B-016 moves from `blocked` to `idea` and waits for that comparison.

## Q-004 Should the kit's own repository also carry `.claude/agents/`?
- **Status:** answered
- **Tags:** plugin, scope
- **Raised:** 2026-10-31 by researcher, when scaffolding the kit with itself
- **Blocks:**
- **Why it matters:** A session working on the kit in the cloud has no plugin loading and therefore no role agents unless `.claude/agents/` exists. But copying `agents/` into `.claude/agents/` inside the kit duplicates eight files that must stay identical.
- **Options:** (a) No copy; sessions on the kit use `claude --plugin-dir .` locally and work without role agents in the cloud; the kit's work is mostly prose; recommended. (b) Copy, with a CI check that the two directories are identical. (c) Symlinks, which Claude Code may not follow and which break on Windows.
- **Answer:** Yes, carry the copy (option b without the identity check). The kit is itself a project run by a customised instance of its own process, which that instance can configure and update; `.claude/agents/` is seeded as a verbatim copy of `agents/` and later tuned to the workflow the kit wants for itself, so the two directories need not stay identical. Decided by Ed on 2026-10-31 in the session chat; recorded as D-015; the copy landed under B-022.

## Q-005 Is `process-kit` the name?
- **Status:** answered
- **Tags:** plugin
- **Raised:** 2026-10-31 by researcher, from the brief ("naming" listed as open for Ed)
- **Blocks:**
- **Why it matters:** The name is the plugin namespace (`/process-kit:check`, `process-kit:reviewer`), the marketplace name and the repository. Renaming after a project adopts it changes every skill invocation.
- **Options:** (a) Keep `process-kit`: plain, kebab-case, passes the reserved-name checks, recommended. (b) Something more specific to the agent-and-human loop (`loop-kit`, `delivery-kit`). Rename before the first adopting project either way.
- **Answer:** Keep `process-kit` (option a): generic, but good enough for now. Decided by Ed on 2026-10-31 in the session chat; recorded as D-016.

## Q-006 Which development flows does the kit offer, and does it wrap existing plugins or carry its own?
- **Status:** open
- **Tags:** process, plugin, scope
- **Raised:** 2026-10-31 by planner, from the source project's M4 review and Ed's ask that flows be optional and pluggable
- **Blocks:** B-025
- **Why it matters:** The process says what gets reviewed and when, not how code is written between gates. The source project found it needed a development method (test first inside a task, refactor findings landed before the next milestone's code) that the agents and the validator could hold to. Ed wants that method optional and declared per project, and wants the kit to adapt or wrap Claude Code plugins that already implement a flow rather than carrying its own copy. B-024 surveys the plugins and writes the options here.
- **Options:** to be filled by B-024. The shape expected: (a) the kit carries a minimal `tdd` flow as prose and `none` as default, wrapping nothing; (b) the kit declares a flow by plugin name and its agents call that plugin's skills, with the kit's prose as fallback; (c) both, with the wrapped plugin preferred when installed. Each with licensing and update implications.
- **Answer:**


## Q-007 How does a project extend its validator without forking it?
- **Status:** open
- **Tags:** plugin, process
- **Raised:** 2026-11-01 by architect, in docs/arch/review-M2-2026-11-01.md S3
- **Blocks:** B-033
- **Why it matters:** The only way to add a check today is to edit `project/tools/check.py`, which turns the copy into a fork that no update can merge cleanly (D-013). The source project will have checks the kit lacks on its first day of adoption (B-014).
- **Options:** (a) edit the copy, as today; forks it. (b) an optional `project/tools/check_local.py` exposing `check(root, cfg, result)`, loaded by `check.py` with `importlib` when present, never written by the scaffold; recommended, and part of ADR-0002. (c) a separate project script run in CI; two validators, two outputs.
- **Answer:**

## Q-008 How does CI cover plugin validation when `--strict` always fails on the kit's own `CLAUDE.md`?
- **Status:** open
- **Tags:** plugin
- **Raised:** 2026-11-01 by architect, in docs/arch/review-M2-2026-11-01.md S2
- **Blocks:** B-020
- **Why it matters:** `claude plugin validate . --strict` exits 1 on the permanent warning that `CLAUDE.md` sits at the plugin root; the file is the kit's own project instructions and stays. B-020 as written would be red on main or weakened (N-005).
- **Options:** (a) `claude plugin validate . --json`, fail on any error or on any warning other than that one, matched by its message; recommended. (b) move the plugin into a subdirectory; breaks `${CLAUDE_PLUGIN_ROOT}` paths and every path in the docs. (c) non-strict only; misses new warnings. Confirm first that the CLI validates without authentication on a CI runner.
- **Answer:**

## Q-009 Does a `superseded` question unblock `ready`?
- **Status:** open
- **Tags:** process
- **Raised:** 2026-11-01 by architect, in docs/arch/review-M2-2026-11-01.md S4
- **Blocks:** B-034
- **Why it matters:** The backlog README says `ready` needs every linked question `answered`; `check.py` blocks only on `open`, so a `superseded` question passes. Prose and code must agree (invariant 5).
- **Options:** (a) yes, a superseded question is closed; keep the code and state it in the template; recommended. (b) only `answered` unblocks; change the validator and add a test.
- **Answer:**
