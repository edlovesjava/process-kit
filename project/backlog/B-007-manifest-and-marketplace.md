---
id: B-007
title: Plugin manifest and in-repo marketplace
milestone: M1
priority: P0
status: done
role: implementer
depends_on:
questions:
owner:
updated: 2026-10-31
---

## Goal
`.claude-plugin/plugin.json` names the plugin `process-kit` with version, description,
author and repository, verified against the current manifest reference.
`.claude-plugin/marketplace.json` lists the plugin once with source `./` so the repository
can be added as a marketplace directly.

## Acceptance
- [x] Layout verified against the plugin, manifest, components and marketplace references on 2026-10-31
- [x] `claude plugin validate .` reports `Validation passed with warnings`; the warnings are the missing licence (Q-001) and `CLAUDE.md` at the plugin root, which is deliberate: the repository is both the plugin and a project with its own instructions (the file is not loaded as plugin context, and nothing in it needs to be)
- [x] No `license` field until Q-001 is answered

## Notes
Built in the bootstrap session (D-002). D-011.
