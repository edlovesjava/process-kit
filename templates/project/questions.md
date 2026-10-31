# Questions register

Every open question in one place. Anyone (human or agent) adds one; only {{APPROVER}} or
an accepted ADR closes one. Keep the format exactly: `check.py` reads the `## Q-NNN`
headings and the `Status` line.

Statuses: `open`, `answered`, `superseded` (see `process.toml`). Tags are free text; the
usual set is `arch`, `process`, `scope`, plus one per external system.

Format:

```
## Q-NNN Short question
- **Status:** open
- **Tags:** arch
- **Raised:** {{DATE}} by researcher, in docs/... section
- **Blocks:** B-001
- **Why it matters:** one or two sentences
- **Options:** (optional) a, b, c with the recommendation marked
- **Answer:** (when answered) what was decided, by whom, where recorded
```

Progress on an open question goes in dated `- **Progress (date):**` lines between
Options and Answer, so the history stays with the question.

---
