# Independent review of process-kit, 2026-11-14

Requested by Ed through the source project's lead session. Reviewed: `main` at 51319af (PRs #1
to #8 all merged, CI run 21 green). Written by a fresh session with no part in building the
kit; every statement in the SITREP, item Notes, decisions, README and the two M2 reviews was
treated as a claim to check. This file is a snapshot. It has no backlog item and no journal
row, because the brief was to change nothing else; folding it in is the lead's.

**How findings are marked.** *verified* means I ran it or read the line on 2026-11-14 (Linux,
Python 3.13.18, Claude Code CLI 2.1.325). *inferred* means reasoned, not exercised. **Known**
means the kit already tracks it (item or question named); everything else is new. Plugin facts
were checked against the current documentation at code.claude.com (manifest reference,
components, marketplace reference, skills, settings), not memory.

**What I ran.** The unit suite (32 tests, OK); `tools/check.py` on the kit (38 items, 0 errors,
0 warnings, INDEX unchanged); `claude plugin validate .` (passes, two warnings; `--strict`
exits 1); the three CI jobs by hand; five scaffolds into scratch directories (fresh, rerun,
existing `CLAUDE.md` + `project/` + `.claude/agents/`, quotes in names, `--dry-run` and
`--force`); about thirty planted inputs against a scaffolded validator; nine hook payloads;
`claude plugin marketplace add` and `install --scope project` against an isolated config
directory; and one live `claude -p --plugin-dir` session in a scaffolded project.

## Verdict

The mechanics are sound and better tested than most first versions: the scaffold is
idempotent, the validator is small and readable, the plugin layout is valid against the
current documentation, and in a live session the hook fired and reported a planted error
back to the model. An adopter following the README gets a working project in two commands.

The weak side is the record and the reach. The validator's central promise (nothing moves
while something it depends on is open) holds for one status only. The journal rule adopted
to fix the last review's first blocking finding is broken by the commit that adopted it and
by every row since. The behaviour half of the kit (thirteen skills, the hook) does not exist
in cloud sessions, which is where the kit and its first adopter are actually run. And after
the bootstrap day the loop the kit sells has still not run once: no reviewer dispatch, no
implementer on its prescribed model, seventeen new items about the process against five
delivered. None of this needs a redesign. Fix the three blocking findings, settle about
thirty queued decisions in one sitting, then let B-015 run the loop for real before adding
any more process.

## Blocking

**B1. The dependency gate only guards `ready`; an item can be `in-progress`, `review` or
`done` with an open question and an unmet dependency.** *verified, new.*
`tools/check.py:316-324`. Planted B-011 `in-progress`, B-012 `review`, B-013 `done`, each
with `depends_on` an `idea` item and `questions:` an open question: 0 errors. The README
("a validator refuses an item marked `ready` while anything it depends on is open") is
literally true and practically hollow: skip `ready` and nothing objects. The process review
measured that 0 of 12 done items ever passed through `ready`. No test pins it either way.
*Fix:* error when `in-progress` or `review` has an unmet dependency or open question; warn
on `done`; state it in the backlog README; one test each.

**B2. D-017 (journal time read from the clock, never estimated) is not being kept, starting
with the commit that adopted it.** *verified, new.* Every row added since the process
review's B1 carries a time later than the commit that contains it: 21:14 in 416a363
(committed 21:12 UTC), 21:32 in 9983692 (21:16), five rows at 13:05 in 1be898a (12:50, the
B-037 commit itself), 16:33 in 0eade41 (16:27). A row cannot be written after its own
commit. So the M3 review would again measure invented times, which is what B1 was raised to
prevent, and B-037's ticked box for it is evidence of prose changed, not behaviour.
*Fix:* a prose rule did not hold; make it checkable. A CI step (git-aware, outside
`check.py`) that fails when an added row's time is later than its commit time.

**B3. In a cloud session the kit is half a kit, and the kit's own copies point at a path
that does not exist.** *verified.* This session (cloud) loaded the eight `.claude/agents/`
and no `process-kit:` skill and no hook, as the documentation says it will ("the
marketplaces and plugins those two keys declare still don't load in a cloud session").
Every journal row to date was written in a cloud session, so the thirteen skills and the
hook have never run in the kit's own work; B-011 and B-012 Notes say "Run with the
`arch-review` skill", which a cloud session cannot have done. Worse, 4 of the 8 copied
agents and 11 of 13 skills run `python3 -I project/tools/check.py`; in the kit that file
does not exist (`ls project/tools`: no such directory; D-001 keeps the validator at
`tools/check.py`). The process review saw this (O4) and wrote "no new item", so it is on no
register. M3's B-014 adopts the kit in a project that runs in cloud sessions. *Fix:* decide
before B-014 whether the scaffold also copies skills to `.claude/skills/` and the hook to
`.claude/settings.json` (the settings page says a single-repository cloud session reads
the committed `.claude/settings.json`; skills loading there is *not verified*); tune the
kit's own agent copies to `tools/check.py` now (D-015 already allows it).

## Should fix

**S1. `main`'s tracking is untrue after today's merges, and the process has no answer for a
merge made when no session is alive.** *verified.* B-037 is `review` with owner "lead
session (PR for B-037)" though PR #7 merged at 16:39 UTC (`project/backlog/B-037-*.md:6`);
`project/SITREP.md:16-17` says "PRs #6 and #7 are still open and still gate everything";
`README.md:86-100` says the boundary reviews are owed and counts 31 tests;
`project/milestones.md:13-16` shows M0 and M1 as "reviews owed" and M3 `not-started` with
B-037 merged; no journal row for the three merges. WORKFLOW step 6 says "same session as
the merge, never next time", but Ed merges in GitHub and all three sessions were gone.
*Fix:* one tracking PR now; then pick one: a scheduled or PR-event session that runs the
merge-sync, or change the rule to "first act of the next session" and have `check.py` warn
on `review` items whose branch is merged (git-aware CI script).

**S2. Two skills still set `done` themselves.** *verified, new.*
`skills/arch-review/SKILL.md:26` and `skills/process-review/SKILL.md:29` say "Set the
review's item `done`", against D-019 and `skills/merge-sync/SKILL.md:14-15` ("the only
place `done` is ever set"). B-037's fourth box is ticked on that claim. Also
`merge-sync` step 4 sets dependents `ready`, which `agents/operator.md:17` forbids the
operator to do. *Fix:* both reviews end at `review`; say who flips dependents.

**S3. Skill arguments: `$0` is the first word, not the title.** *verified against the skills
page.* "Indexed arguments use shell-style quoting"; `backlog-item` (`title: $0`, hint
`[short title]`), `decision`, `question` and `adr` all take a multi-word argument through
`$0`. `/process-kit:decision use the MIT licence` records "use". *Fix:* `$ARGUMENTS` where
one free-text argument is meant.

**S4. `version` is pinned at 0.1.0 while the plugin half has changed.** *verified.*
`.claude-plugin/plugin.json:4`; the manifest reference says setting it "keeps users on that
version until you change it". Ten files under `agents/`, `skills/`, `tools/`, `templates/`
have changed since 2026-10-31 (B-037 among them). Anyone who installed keeps the old behaviour.
*Fix:* bump on every plugin-affecting merge, or drop the field until B-018.

**S5. The hook.** *verified with payloads unless marked.*
(a) It runs the repository's own `project/tools/check.py` with no permission prompt
(`scripts/check_hook.py:36-42`): a planted script wrote a file and its stdout was fed to the
model as hook feedback. With the plugin enabled at user scope this is true in any repository
that has `project/process.toml`. Workspace trust probably covers it in interactive use
(*inferred*), but the README should say so in one sentence.
(b) Any non-zero exit is reported as "validator found errors" (`:43-45`): an import failure
(what Python older than 3.11 gives on `tomllib`; stock macOS `python3` is older, *not
verified on a Mac*) arrives after every edit as a validation failure.
(c) A slow validator blocks each edit for 15 s, then passes silently (`:41`, `except` at
`:47`). (d) Subdirectory cwd skips silently (**known**, B-032, `ready` P0, untouched for 13
days though it needs no decision). (e) Edits made through Bash are never checked; the 11-14
session edited tracking by script. *Fix:* distinguish crash from findings by the summary
line; document (a) and (e); do B-032.

**S6. The scaffold.** *verified.*
(a) `--name` or `--approver` containing `"` or `\` writes an unparseable `process.toml`
(`tools/scaffold.py:48-49`); the scaffold exits 0, then `check.py` gives four cascading
errors. (b) `--force` rewrites all 27 files including the journal, decisions and questions
(**known**, B-030). (c) On a rerun with an existing `CLAUDE.md` the note says the sections
"were written" when the file was skipped (`:84-88`). (d) The templates seed a `human |
decided` row at `00:00` and a D-001 "decided" by the approver
(`templates/project/activity.md:29`, `templates/project/decisions.md:10`): the first two
records of every adopter break D-017 and record a decision nobody made. (e) It adds
`.github/workflows/tracking.yml`; `README.md:43-55` does not mention a CI workflow.
*Fix:* escape or reject; correct the note; seed the row as `done` by `operator`, or no row.

**S7. Validator: silent holes found with planted inputs.** *verified, new unless marked.*
- Dependency cycles, self-dependency and a dependency on a `dropped` item: no error; the
  items sit `blocked` for ever (`check.py:307-322`).
- A `#` in a title truncates it ("Fix issue #12 in parser" indexes as "Fix issue"); a `|`
  breaks the INDEX row (`:172`, `:383`).
- Unknown keys inside known sections are ignored: `stale_day = 1` and `flow = "tdd"` pass;
  `enabled = "false"` leaves the journal on (`:88-90`, `:147`). B-025's `flow` key would be
  silently ignored by every older copy.
- A `## Q-1000` heading is not recognised and its Status line overwrites the previous
  question's status (`:187-194`). Any non-question `##` heading with a Status line does it.
- A journal row with a date and no time passes; the first row under a heading with no header
  row is swallowed without a word; two headings for the same day pass (`:249-251`, `:260`).
- `--root` with no value raises (**known**, B-034); any mistyped flag is ignored.
- **A prior "verified" finding does not reproduce:** CRLF front matter parses correctly
  (`read_text` translates newlines). Drop that half of B-034's fourth box.

**S8. "Tailorable without editing the kit" is true for config and agents, not for skills or
cadence.** *verified by reading.* `docs/tailoring.md:57-62` says cadence changes live in
`WORKFLOW.md` "and the `arch-review` and `process-review` skills", which exist only inside
the plugin; `:28-29` offers "the plugin's `agents/` if you maintain a fork". Skills hardcode
the PR flow, the check path and the step lists. Also the milestones template says `Spec`
where the config says `spec` (`templates/project/milestones.md:11`, `process.toml:16`), and
no "must match" is checked (**known**, B-035). *Fix:* say plainly which half is tailorable
today; B3's copy decision would make the rest so.

**S9. The six proposal items overlap and in places contradict.** *verified by reading.*
- Commit granularity is specified twice, in B-025 (Goal and box 4) and B-028 (box 3). B-025
  uses `test:`/`fix:`/`refactor:` prefixes, which presuppose the convention B-028 has not
  yet proposed for decision; neither depends on the other.
- B-025 bundles three separable things: the `flow` key, the `kind` front-matter key with an
  INDEX column and validator rule, and a change to the milestone gate (should-fix findings
  land before the next milestone "by default"), which alters WORKFLOW step 7 for everyone,
  not only under `tdd`. B-026 needs only `kind`.
- B-025 has the architect size findings XS, S or M; the review template says XS / S / M / L.
- B-026 makes the validator require the English phrase "No behaviour change": a project
  that spells it "behavior" fails, and nothing says where the adoption date lives.
- B-027's journal column `Branch`, "which B-028's naming makes the session's id", contradicts
  B-028, which names branches for items precisely so they are not session names.
- B-028 and B-027 carry `role: researcher` but B-028's boxes include CI checks, a validator
  warning and tests. The one piece with measured damage (the id-collision guard, W6) sits
  inside a seven-box `later` idea while parallel sessions continue.
- B-025 cites "its D-020" (the source project's); the kit has its own D-020 on another topic.
*Fix:* split `kind` out; one home for commit rules; lift the id guard into its own small
item; decide Q-006 before more text lands in B-025.

**S10. Smaller truths in `project/` and the docs.** *verified.* ADR-0002 has no row in
`docs/adr/README.md` (the `adr` skill's step 4); `milestones.md` Items columns omit B-021,
B-022, B-023, B-031 and the `later` items; B-021 and B-023 are owned by "bootstrap session"
and "second session", which no longer exist, and have sat in `review` for 14 days; B-006 is
`done` with an open box (**known**, B-032, B-038); `CLAUDE.md:46` says `tools/tests/` is a
suite "for both", it is one file with no hook or CLI tests (**known**, B-032, B-034); D-012
to D-016 say "Ed" on the strength of a chat the repository cannot show, which is inherent
but worth one line in `decisions.md`.

**S11. Stale warnings are about to fire for everything that waits on Ed.** *verified by
running `check.run` with later dates.* 6 warnings tomorrow, 21 on 2026-11-17. The `check`
skill's advice is "touch the item", which launders the signal. *Fix:* exempt `blocked` and
human-role `ready` items, or report them as "waiting on the approver since".

## Minor

- `main` is not a protected branch (*verified*, GitHub API). "Every merge is Ed's" is a
  convention; the bootstrap pushed straight to `main`.
- `INDEX.md` is generated and committed, and CI diffs it, so any two branches that touch
  items conflict on it (*inferred*; the SITREP already warns "regenerate, never hand-merge").
  Consider not committing it. Its header names `project/tools/check.py` even in the kit.
- With the plugin enabled and the agents copied, a session has sixteen role agents, eight
  bare and eight `process-kit:` (*verified live*; shadowing is **known**, B-036).
- `install --scope project` writes `enabledPlugins` only (*verified*); a teammate also needs
  the marketplace (`extraKnownMarketplaces`), which the README does not say (*inferred*).
- `agents/architect.md:3` and two skill descriptions contain `: ` in an unquoted YAML value.
  Claude Code parses them (*verified*, this session shows the full description); a strict
  YAML reader would not.
- The reviewer's tools (Read, Grep, Glob, Bash) give it no way to read a PR in a cloud
  session, where there is no `gh` (*inferred*).
- Template leftovers that read as one project's habits, though no denylisted word appears
  (CI noun grep passes; a wider list of my own found nothing in the shipped parts):
  `templates/CLAUDE.md:49-51` (an interface catalogue before any producer merges),
  `templates/docs/design/nfrs.md:18,26` (compiler flags, a dependency-check task, "literate
  code"), the reviewer's golden-fixture paragraph.
- `project/` is hardwired; some build tools own a directory of that name (*inferred*).

## Process soundness

*Measured from `project/activity.md` and git, 2026-11-14.*

- **The loop has not run.** 36 rows: 29 on model `lead`, 1 architect, 1 program manager, 5
  human, 0 reviewer. B-037, the only code change since the bootstrap, was implemented by the
  lead, reviewed by nobody and merged twelve days later. The role routing and the cheaper
  models are still a design, not an observation. B-015 is the test; it is blocked.
- **The process mostly produces process.** Since the bootstrap ended: 17 new items (B-022
  to B-038), all about the kit itself; 5 delivered (B-019, B-022, B-011, B-012, B-037). The
  two boundary reviews together produced nine items, five questions, one ADR and eight
  proposed workflow changes. For a single
  person with agents, two gating reviews per milestone, a nine-column row per dispatch and
  six registers is heavy; I would expect a small team to keep the backlog, questions and
  SITREP, and let the journal and the process review lapse first.
- **One approver, about thirty queued decisions.** ADR-0001 with eight `By: researcher`
  rows, ADR-0002, Q-007 to Q-009, W6 to W8, P1 to P10, B-021, and six ideas to prioritise.
  B-013 has been `ready` for 14 days and everything in M3 traces to it. A21 says the
  approver's time is the scarce resource; the reviews spend it faster than they save it.
  The wait is also for a session: B-032 needs no decision and has not moved, because
  nothing happens until Ed starts one.
- **Where it is silent.** Session handoff beyond a hand-written SITREP (B-027, idea);
  concurrent edits to tracking and id minting (B-028, idea; it has already cost a restack);
  merges made with no session alive (S1); what an agent does when the approver is away for
  two weeks, other than accumulate proposals.

## What is good and should be kept

- The scaffold: idempotent, never overwrites, leaves an existing `CLAUDE.md` and existing
  agents alone, `--dry-run` writes nothing (all *verified*).
- The validator: 450 readable lines, standard library, config-driven vocabulary, clear
  messages with file and line, INDEX written only on a clean run, `-I` everywhere.
- The plugin: valid layout, correct `hooks.json` wrapper and quoting, the hook's catch-all
  means it never breaks a session in a repository that does not use the kit, and it worked
  first time in a live session.
- The questions register with options and a recommendation, and the rule that agents never
  close one. Five questions answered in two turns is the best number in the journal.
- Dated SITREP corrections, the append-only decision log, `By: researcher` rows that admit
  they are unconfirmed, and two M2 reviews that were candid about the kit's own lapses.
- `docs/assumptions.md`: stating which assumptions are fixed, and why, is rare and useful.
- CI that scaffolds a throwaway project and checks the kit's own tracking on every push.

## Not covered

- `docs/whitepaper.md` and `docs/research/prior-art-2026-10-31.md` beyond a leftover grep.
- Windows and macOS; Python 3.11 and 3.12 (I ran 3.13 only; CI covers 3.11 and 3.12).
- `claude plugin marketplace add edlovesjava/process-kit` by GitHub shorthand (I used a local
  path); each skill run end to end (I verified that ten load and are listed, and that the
  three with `disable-model-invocation` are not offered to the model); issue mirroring.
- Whether a cloud session loads `.claude/skills/` from the repository; sessions inside a
  claude.ai project thread, where the documentation suggests even `.claude/agents/` and
  repository hooks may not load.
- PR bodies and review threads (titles, bases and merge times only); the source project.
