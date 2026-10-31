---
id: B-024
title: Research existing plugins that implement a development flow, and how the kit wraps one
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
Ed asked that development flows (test-driven development, plan-then-execute and the
like) be optional and pluggable, and that the kit adapt or wrap Claude Code plugins that
already implement one rather than reimplementing them. This item surveys what exists
and how the kit would hand off to it. The output is options with a recommendation in
Q-006, which Ed answers; B-025 then implements what was decided.

## Acceptance
- [ ] A survey of current Claude Code plugins and skill bundles that implement a development flow (Ed named `superpowers` and `gsd` as examples; there are others), each verified from its current repository or documentation with WebSearch and WebFetch, not from memory: what flow it carries, how it is installed, what it assumes about the repository, its licence, how often it changes
- [ ] For each candidate, how a kit project would declare it (for example a `flow` key in `process.toml`) and how the implementer, reviewer and architect agents and the kit's skills call the plugin's skills without duplicating their prose
- [ ] Licensing and update implications stated: what a wrapped plugin's licence permits, what breaks in the kit when the plugin changes, and who notices
- [ ] A fallback described: the kit's own minimal TDD flow (the B-025 text) when no plugin is installed or wanted
- [ ] Options with a recommendation written into Q-006; a journal row

## Notes
Proposed from the source project's M4 review, where the first two refactor items under a
test-driven method surfaced the need for a method the process could enforce, and Ed's
ask that it be pluggable. Stays `idea` until Ed prioritises. The researcher is the lead
session; research uses the network, so this item runs in a session with web access. Start from
`docs/research/prior-art-2026-10-31.md` (B-023), which already covers `superpowers` and the
spec-driven frameworks; this item goes deeper on the flow and the handoff, not the survey.
