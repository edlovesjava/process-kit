# Decision log

Non-architectural decisions: process, scope, tooling. Architecture decisions go in
`docs/adr/` and are only linked from here. Append-only: a changed mind is a new entry
that supersedes the old one (fill the Supersedes column and set the old row's status to
`superseded`). Any change to `project/process.toml` gets a row here.

| ID | Date | Decision | Status | By | Supersedes | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| D-001 | {{DATE}} | Work tracking lives in `project/` as Markdown, one file per backlog item, validated by `project/tools/check.py` against `process.toml`; adopted from process-kit | decided | {{APPROVER}} | | Roles, models and milestones as scaffolded until changed by a later row. |
