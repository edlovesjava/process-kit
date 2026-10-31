---
name: adr
description: Draft a new architecture decision record in docs/adr/ from the template, with status Proposed, or add a dated amendment to an Accepted one. Use when a question has architectural options, when a review proposes an ADR, or when asked to "write an ADR".
argument-hint: "[title]"
allowed-tools: Bash, Read, Write, Edit
---
Draft an ADR. ADRs beat the spec: when they disagree, the ADR wins and the spec gets a
pointer. Only the approver moves an ADR from Proposed to Accepted or Rejected.

To draft a new record:

1. Next number: highest `NNNN` in `docs/adr/` plus one (the template is `0000`).
2. Copy `docs/adr/0000-template.md` to `docs/adr/NNNN-short-title.md`. Fill every field:
   Status `Proposed`, today's date, the approver as decider, the `Q-NNN` entries it
   answers, what it supersedes (a spec section, an earlier ADR, or none).
3. Context in two or three paragraphs with links to the finding or question. Two or more
   Options, each with consequences good and bad. Decision in one sentence plus the
   reasoning. Consequences: easier, harder, work created (link items), what would make us
   revisit.
4. Add a row to the table in `docs/adr/README.md` with Status `Proposed`.
5. Add a backlog item for the approver to accept or reject it if none exists (role
   `human`, milestone `spec`), and link the ADR from the question's Options line.

To amend an Accepted record (allowed only while no code depends on it):

1. Add a dated bullet under `## Amendments`: what changed, which finding or question
   raised it, "awaiting <approver>" until accepted, then "accepted by <approver> <date>".
2. Note the amendment in the README row's Status column, e.g. `Accepted (amended
   YYYY-MM-DD: topic)`.
3. Once code depends on the ADR, stop amending: a changed mind is a new ADR that
   supersedes the old (Status `Superseded by ADR-MMMM` on the old one).

Never write application code from an ADR that is still Proposed.
