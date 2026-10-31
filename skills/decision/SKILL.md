---
name: decision
description: Append a row to the decision log (project/decisions.md) for a process, scope or tooling decision the approver has made, including any change to process.toml. Use when the approver decides something that is not an ADR, or when asked to "record a decision".
argument-hint: "[one-sentence decision]"
allowed-tools: Bash, Read, Edit
---
Record a decision. The log is append-only: a changed mind is a new row that supersedes
the old one, never an edit.

1. Confirm the decision was actually made by the approver (their words in this session,
   a merged PR comment, or an answered question). Agents propose; they do not record
   their own proposals as decisions. If it was not decided, raise a question instead.
2. Next id: highest `D-NNN` in `project/decisions.md` plus one.
3. Append a row:

   ```
   | D-NNN | <today> | $0 | decided | <approver, and the role that proposed it> | <D-MMM it supersedes, or empty> | <question it answers, ADR it affects, items it starts> |
   ```

4. If it supersedes an earlier row, change that row's Status to `superseded` and nothing
   else in it.
5. If the decision changes `project/process.toml` (a role, a model, a milestone, a status,
   the stale period, issue mirroring), make the config change in the same commit and name
   the key in the Notes column.
6. If it changes `WORKFLOW.md`, edit the workflow in the same commit and cite `D-NNN` there.
7. Add a journal row: role `human`, model `human`, item `D-NNN`, outcome `decided`, human
   turns as counted.

Architecture decisions do not go here; they are ADRs (adr skill), linked from here only.
