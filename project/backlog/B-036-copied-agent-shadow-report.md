---
id: B-036
title: session-start reports a copied agent whose hash differs from the lock and the plugin
milestone: M4
priority: P2
status: idea
role: implementer
depends_on: B-030
questions:
owner:
updated: 2026-11-01
---

## Goal
With the plugin enabled, a dispatch to a bare role name most likely resolves to the copy
in `.claude/agents/` rather than the plugin's agent, so a stale copy wins without notice
(review O4, inferred). Once the lock exists, `session-start` or `check` reports copies
whose hash differs from both the lock and the plugin.

## Acceptance
- [ ] The shadowing behaviour confirmed or refuted against the current Claude Code documentation, recorded in Notes
- [ ] Report line in the skill, or a validator warning, with a test

## Notes
From `docs/arch/review-M2-2026-11-01.md` O4. Depends on B-030 for the lock.
