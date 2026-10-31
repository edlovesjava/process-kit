# Situation report

Short, dated handoff for whoever picks up next: what just happened, what is in flight,
what to do first. Newest entry at the top. Keep each entry under a screen; detail
belongs in the files it links. Any session may add an entry; replace or trim old ones
once their content is reflected in the backlog, questions or notes. A correction to an
earlier entry is a dated note inside it, never a silent edit, so a wrong root cause does
not stand unmarked.

## 2026-10-31 Ed answered Q-001 to Q-005; licence and the kit's own agents landed (second session)

**Why this entry.** Ed answered all five bootstrap questions in chat. This session recorded
them (D-012 to D-016, answers in `project/questions.md`) and did the two things that followed
directly: `LICENSE` (MIT) with `license` in `plugin.json` (B-019 done) and `.claude/agents/`
seeded as a verbatim copy of `agents/` (B-022 done), so a cloud session on the kit now has the
role agents. Branch `claude/upbeat-hypatia-1tpqea`, for Ed to merge.

**Decisions in one line each.** MIT. Plugin for behaviour from the in-repo marketplace, the
scaffold copies the customisable assets, and the kit must be able to update and tune those
copies (B-018 now `ready`, scope rewritten). Journal rows by hand for the proof of concept,
then a competitive design of hand against hook (B-016 to `idea`, scope rewritten). The kit
is a project run by a customised instance of its own process, so it carries its agents copy
and tunes it later. The name stays.

**Still for Ed.** B-013 (ADR-0001 and the `By: researcher` rows); B-021 whitepaper comments.
`claude plugin validate .` no longer mentions the licence; it still warns about the kit's own
`CLAUDE.md` at the plugin root (expected) and now about a missing icon, relevant only if the kit
is ever submitted to the directory.

**What is ready now.** B-011 and B-012, the M2 boundary reviews, unchanged; they still gate
M3. B-018 is ready but belongs to M4. Note on this session's record: Ed's chat numbered the
agents answer "Q-003" and the name answer "Q-004"; they were recorded under Q-004 and Q-005
by their content.

## 2026-10-31 Kit bootstrapped: M0 to M2 built, reviews owed, five questions for Ed (bootstrap session)

**Corrected 2026-10-31, second session.** Q-001 to Q-005 are answered (entry above). The
"Do not add a LICENSE" line and the statement that cloud sessions on the kit have no role
agents no longer apply.

**Why this entry.** One session built the kit end to end from the source project's process
files (D-002, the bootstrap exception). Everything below `project/` was written with the
kit's own templates and validated with its own `tools/check.py`.

**State.** On `main`, pushed to `edlovesjava/process-kit`: validator with `process.toml`
and journal checks (30 unit tests), scaffold, eight agents, thirteen skills, one hook,
manifest and in-repo marketplace, templates for every file, `docs/assumptions.md`,
`docs/tailoring.md`, README, CI (three jobs), ADR-0001 (Proposed). `claude plugin
validate .` passes with two expected warnings (no licence until Q-001; `CLAUDE.md` at the
plugin root, which is the kit's own project instructions and is not plugin context).
`check.py` on this `project/` reports zero errors. CI run 1 on `main` is green
(three jobs). The scaffold was exercised end to end into a temp
directory: fresh scaffold passes, an item flipped `ready` with an open question fails,
`review` without owner fails, `done` without a journal row warns.

**Decisions Ed must make.** Q-001 licence (recommend MIT), Q-002 distribution (recommend
the in-repo marketplace as is), Q-003 journal rows by hand or by hook (recommend by hand
first), Q-004 whether the kit's own repo carries `.claude/agents/` (recommend no), Q-005
the name (recommend keep). B-013: accept, amend or reject ADR-0001 and confirm the
`By: researcher` decision rows D-002 to D-011.

**Added 2026-10-31, end of session.** B-021 (whitepaper proposal for engineers and managers) is
in `review`: draft at `docs/whitepaper.md`, commentable copy as a Claude doc Ed holds, three
questions left there for Ed. Fold Ed's comments in, then decide which copy is the record.
This session closes here; the next one is a dedicated session on this repository.

**What is ready now.** B-011 architecture review and B-012 process review at the M2
boundary (run the `arch-review` and `process-review` skills); B-013 for Ed. M3 (B-014
adopt in the source project, B-015 fresh project loop) is blocked on those reviews, as the
process requires. The source project's own item for the journal and program manager is
B-014 here.

**Conventions a fresh session must keep.** Push the branch first. Run
`python3 -I tools/check.py` (not `project/tools/`; the kit runs the root copy, D-001) after
any edit under `project/`. Run `claude plugin validate .` before touching agents, skills,
hooks or the manifest. Templates and the scaffold smoke test move together. No licence file
until Q-001 is answered. Work on the kit in a cloud session has no role agents loaded
(Q-004); locally use `claude --plugin-dir .`.

**Do not.** Add a LICENSE; name the source project's domain anywhere in the kit (CI greps
for it); edit `INDEX.md` by hand; change `process.toml` without a decision row.
