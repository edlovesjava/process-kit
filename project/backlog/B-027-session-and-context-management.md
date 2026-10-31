---
id: B-027
title: Session and context management as part of the process
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
The process assumes sessions that end, hand off and restart, but says little about how.
The source project's lead session ran out of context and handed off by writing a SITREP
entry by hand; a child session went idle and could not be messaged, so a fresh one was
spawned with a standalone brief; a PR subscription and a scheduled check-in died with
the old session; teleport needed the branch pushed first. This item writes the options
for making session and context management a stated part of the process. Options, not
decisions; Ed chooses, and the planner then cuts implementation items.

## Acceptance
- [ ] Options for the handoff skills: extend `sitrep` to gather the live state (branch, open PRs and their CI, items in flight with owners, decisions made this session, open questions, subscriptions and scheduled check-ins that die with the session, next steps) and extend `session-start` to re-subscribe to the PRs the entry names, re-arm check-ins and ask the project manager for status; or new skills alongside them
- [ ] Session topology: when to start another session (parallel implementers, a research spike, a second repository); a standalone brief template (goal, read-first list, decisions already made, constraints, repository availability, report-back target); how results join back (child reports to the parent and to the SITREP; the parent records the child's session id); the rule that one orchestrator session owns `project/` at a time, so two sessions never edit tracking concurrently
- [ ] Context management: when the lead hands off (a context budget threshold it watches), what must be written down first (anything not in the repository dies with the session), what a check-in or subscription needs to survive (the new session re-creates it from the SITREP)
- [ ] The activity journal gets a row per session start, handoff and spawn, so the process review can measure handoffs and lost context; the journal template and `docs/assumptions.md` updated accordingly
- [ ] Options with a recommendation in a question or an ADR draft for Ed; a journal row

## Notes
Proposed by Ed through the source project's lead session on 2026-10-31. Sits alongside
B-024 to B-026 as a process proposal. The existing `sitrep` and `session-start` skills
and A7 (push the branch first) are the starting point; the gap is the live state a
handoff loses (subscriptions, check-ins, child sessions) and the rules for more than
one session at a time.
