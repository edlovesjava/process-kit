---
name: scaffold
description: Set up the process-kit delivery process in a project repository: project/ tracking files, process.toml, docs/adr, docs/arch, docs/process, the NFR register, CLAUDE.md process sections, tracking CI and the role agents. Use when a project adopts the process or asks to "add process-kit".
argument-hint: "[project-name] [approver]"
disable-model-invocation: true
allowed-tools: Bash, Read, Edit
---
Scaffold the process into the current repository. Nothing here needs judgement beyond
the two names; everything else is a copy the project then tailors.

1. From the repository root, run the scaffold with the project's name and the one human
   who decides (the approver). The script never overwrites a file that exists:

   ```
   python3 -I "${CLAUDE_PLUGIN_ROOT}/tools/scaffold.py" --target . --name "$0" --approver "$1"
   ```

   If `$0` or `$1` is empty, ask for them, or use the repository name and "the approver".
   Add `--no-agents` only if the user said the plugin will be enabled at project scope and
   no cloud session will work on the repository (cloud sessions do not load project
   plugins, so the copied `.claude/agents/` is what makes the roles available there).

2. Read the script's output. If it printed `note: CLAUDE.md exists`, open
   `project/CLAUDE-process-sections.md`, merge its Invariants placeholder, Layout, How
   work flows and Conventions sections into the existing `CLAUDE.md`, then delete the copy.

3. Run the validator and confirm zero errors:

   ```
   python3 -I project/tools/check.py
   ```

4. Tell the user what was written and what B-001 (adopt the process) asks them to fill
   in: invariants, roles and models, milestones, the first SITREP entry. Point them at
   `docs/tailoring.md` and `docs/assumptions.md` in the kit for what may change and what
   may not. Do not fill in the invariants yourself; they are the project's.

By hand: copy `templates/` over the repository, replace `{{PROJECT_NAME}}`,
`{{APPROVER}}` and `{{DATE}}`, copy `tools/check.py` to `project/tools/`, copy
`agents/` to `.claude/agents/`, run `check.py`.
