# Questions register

Every open question in one place. Anyone (human or agent) adds one; only Ed or an
accepted ADR closes one. Keep the format exactly: `check.py` reads the `## Q-NNN`
headings and the `Status` line.

Statuses: `open`, `answered`, `superseded` (see `process.toml`). Tags: `process`,
`scope`, `plugin`, `legal`.

Format:

```
## Q-NNN Short question
- **Status:** open
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
- **Status:** open
- **Tags:** legal
- **Raised:** 2026-10-31 by researcher, while building the kit (the brief said not to add a LICENSE file)
- **Blocks:** B-019
- **Why it matters:** The repository is public. Without a licence nobody else may legally use or adapt the kit, and `claude plugin validate` reports the missing licence as a directory warning. The plugin manifest's `license` field (an SPDX id) is where Claude Code reads it.
- **Options:** (a) MIT: shortest, permissive, usual for tooling, recommended if the intent is "use it freely". (b) Apache-2.0: permissive with an explicit patent grant and a NOTICE mechanism; usual for larger projects. (c) CC-BY-4.0 for the prose plus MIT for the code: precise but two licences for one repository. (d) No licence: all rights reserved; fine while the kit is only Ed's.
- **Answer:**

## Q-002 How is the kit distributed to a project?
- **Status:** open
- **Tags:** plugin, process
- **Raised:** 2026-10-31 by researcher, from the plugin documentation read while building the kit
- **Blocks:** B-018
- **Why it matters:** A cloud session (claude.ai/code) does not load project-scope plugins, so the plugin alone does not reach the sessions the source project runs. The scaffold already copies the agents into `.claude/agents/` for that reason (D-006). The question is what the plugin adds and how a project installs it.
- **Options:** (a) The repository is its own marketplace (`.claude-plugin/marketplace.json` lists the plugin with source `./`), so `claude plugin marketplace add edlovesjava/process-kit` then `claude plugin install process-kit@process-kit --scope project` works for local and desktop sessions; cloud sessions rely on the copied agents and the project's own `tools/check.py`; recommended, already in place (D-011). (b) A separate marketplace repository listing this one; only worth it with a second plugin. (c) Upload to the claude.ai organisation library so cloud sessions get it; needs a claude.ai organisation plan and verification that it serves Claude Code cloud sessions (verify). (d) Submit to Anthropic's directory; needs a licence (Q-001), an icon and a review.
- **Answer:**

## Q-003 Are journal rows written by hand, or appended by hooks?
- **Status:** open
- **Tags:** process, plugin
- **Raised:** 2026-10-31 by researcher, from the source project's item on the activity journal
- **Blocks:** B-016
- **Why it matters:** The journal is only as good as its completeness. Hand-written rows depend on the lead remembering (the validator warns when a status change has no row, which catches the two statuses that matter most, not every dispatch). Hooks would catch every subagent run but produce rows without the judgement columns (runs, outcome, problem, resolution), so a human or the operator still has to summarise.
- **Options:** (a) Hand-written rows via the `journal` skill, with the validator's warning as the safety net; revisit when a process review shows rows being missed; recommended as the start, matching the source project's own proposal. (b) A `SubagentStop` hook appends a JSONL line per dispatch under `project/activity/`, and the operator summarises into the table at session end; complete but two formats to keep. (c) A `SubagentStop` hook writes the table row directly with `outcome` blank for the lead to fill; one format, but a half-filled row the validator must tolerate.
- **Answer:**

## Q-004 Should the kit's own repository also carry `.claude/agents/`?
- **Status:** open
- **Tags:** plugin, scope
- **Raised:** 2026-10-31 by researcher, when scaffolding the kit with itself
- **Blocks:**
- **Why it matters:** A session working on the kit in the cloud has no plugin loading and therefore no role agents unless `.claude/agents/` exists. But copying `agents/` into `.claude/agents/` inside the kit duplicates eight files that must stay identical.
- **Options:** (a) No copy; sessions on the kit use `claude --plugin-dir .` locally and work without role agents in the cloud; the kit's work is mostly prose; recommended. (b) Copy, with a CI check that the two directories are identical. (c) Symlinks, which Claude Code may not follow and which break on Windows.
- **Answer:**

## Q-005 Is `process-kit` the name?
- **Status:** open
- **Tags:** plugin
- **Raised:** 2026-10-31 by researcher, from the brief ("naming" listed as open for Ed)
- **Blocks:**
- **Why it matters:** The name is the plugin namespace (`/process-kit:check`, `process-kit:reviewer`), the marketplace name and the repository. Renaming after a project adopts it changes every skill invocation.
- **Options:** (a) Keep `process-kit`: plain, kebab-case, passes the reserved-name checks, recommended. (b) Something more specific to the agent-and-human loop (`loop-kit`, `delivery-kit`). Rename before the first adopting project either way.
- **Answer:**
