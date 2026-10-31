---
id: B-029
title: Multi-repository projects with one repository for the common project state
milestone: later
priority: P2
status: idea
role: researcher
depends_on: B-028
questions:
owner:
updated: 2026-10-31
---

## Goal
The process assumes one repository holds code, docs and tracking. Some projects span
several: libraries spun out of a project, or a brown-field estate already split into
many repositories. Ed's direction: spawned libraries stay in the mono-repository by
default, but the kit must be able to run a project whose code lives in several
repositories with one repository holding the common project state (backlog, questions,
decisions, journal, SITREP). This item writes the options for how the kit does that.

## Acceptance
- [ ] Options for where tracking lives when code spans repositories (a tracking repository; the primary code repository; one per repository with a roll-up), with the validator's reach and the hook's trigger considered for each
- [ ] How an item names the repositories it touches and how one item becomes one PR per repository that still reads as one review, including the order of merges and the journal row
- [ ] How a session gets the repositories it needs (clone list, read-only versus push, what a cloud session can attach) and how the one-orchestrator rule for `project/` (B-027, B-028) holds across repositories
- [ ] The mono-repository default stated, with the brown-field exception and what a project writes down when it takes it
- [ ] Options with a recommendation for Ed in a question or ADR draft; a journal row

## Notes
From Ed's note of 2026-10-31. The scaffold already copies the validator and the agents
into the adopting repository, which is the single-repository case; this item asks what
changes when there are several. Depends on B-028 for the branch and commit rules it
extends.
