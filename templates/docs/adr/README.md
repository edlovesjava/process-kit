# Architecture decision records

One file per decision, `NNNN-short-title.md`, from `0000-template.md`. Statuses:
`Proposed` (drafted by the researcher, awaiting {{APPROVER}}), `Accepted`, `Rejected`,
`Superseded by ADR-MMMM`. Records are append-only; a changed mind is a new ADR. One
exception: while no code yet depends on it, an Accepted ADR may take a dated entry in an
**Amendments** section instead, so a same-week correction does not need a superseding
record. Once code depends on the ADR, amendments stop and a new ADR supersedes.

Where an ADR and the spec or design document disagree, the ADR wins and the other
document gets a one-line pointer to it.

| ADR | Title | Status | Answers |
| --- | --- | --- | --- |
