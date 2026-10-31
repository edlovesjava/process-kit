---
id: B-028
title: Repository, branch and commit rules for sessions and subagents
milestone: later
priority: P1
status: idea
role: researcher
depends_on:
questions:
owner:
updated: 2026-10-31
---

## Goal
The process says one item per PR and push the branch first, and nothing else about how
sessions and subagents share a repository. Ed's defaults, stated 2026-10-31: all work
happens in workspaces (worktrees or equivalent isolated checkouts), never on a shared
working tree; every session has its own branch; subagents may share a session's branch
or stack a branch on it when that is safe, and otherwise take their own; commits follow
the Conventional Commits convention. This item turns those defaults into a guide in the
WORKFLOW template, agent duties and, where a rule is checkable, a validator or CI check.

## Acceptance
- [ ] A repository-and-branches section in `templates/project/WORKFLOW.md` (and the kit's own): workspaces by default, one branch per session, naming, when a subagent shares, stacks or branches off, who rebases what, how a stacked PR is retargeted, what happens when two sessions touch `project/` (ties to B-027's one-orchestrator rule)
- [ ] Commit rules: Conventional Commits types and scopes the kit uses, how an item id appears in the message, `refactor:` commits behaviour-neutral (ties to B-025); the implementer and reviewer agents and the `merge-sync` skill state them
- [ ] "Safe to share or stack" defined: disjoint files, no concurrent edits under `project/`, the base branch pushed and unmerged or merged, with examples
- [ ] A checkable rule where one exists (a commit-message lint in CI, or a validator warning on a branch that edits another item's file), with a test
- [ ] `docs/assumptions.md` and `docs/tailoring.md` updated; adopting the rules in the kit's own `process.toml` or `WORKFLOW.md` gets a decision row

## Notes
From Ed's note after two kit sessions ran in parallel on 2026-10-31 and both minted B-022
and B-023; the collision was found only at merge time (SITREP, PR #1 and #2). The kit's
own commits so far are not Conventional; adopting the convention is a decision row and
applies from that date.
