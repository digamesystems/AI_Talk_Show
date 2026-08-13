# Cursive in a Charter School — Essay 5, Working Notes

Draft text and footnotes now live in their own files, one per part, for publication:

- **Part 1** — "Cursive in a Charter School - Essay 5, Part 1 (WIP).md" — "A Lot of Hungry
  Programmers" (title locked 2026-08-12)
- **Part 2** — "Cursive in a Charter School - Essay 5, Part 2 (WIP).md" — "The Margins"

This file keeps everything that isn't part of the essay itself: open ideas, decisions made along
the way, attribution status, and source verification notes for both parts.

---

## Ideas to consider, not yet incorporated (not part of the essay)

- **AI-as-verification-partner aside, possibly for Part 2.** Prompted 2026-08-09 by John correctly
  recalling the Spolsky/Gates story from 20 years ago, with two details drifted (spec length,
  "sticky notes" vs. margin annotations) — caught and corrected by a live primary-source check in
  this same conversation. John's own observation: this fast, cheap verification step is itself a
  feature of the AI-assisted workflow, distinct from generation speed. Candidate framing: it's the
  same generation-got-cheap dynamic the essay is already about, just applied to fact-checking
  instead of code — recall and verification used to be one expensive, combined act; now they're
  two cheap, separable ones. Could work as a first-person aside near the Spolsky scene, or held for
  Part 2 alongside the other LLM-specific material. Not committed to either spot yet.

- **The "preserving the why" convergence, possibly not for this essay at all.** John's own
  `Session Handoff Protocol.md` and per-essay revision logs turned out to share their core
  structure with Steve's L4 and with the arXiv tiered-context paper — three independent arrivals
  at "preserve the rationale separately from the current state." Logged as its own item,
  Roadmap entry 18 (`documentation/Future Essays - Roadmap.md`), since John was explicit this may
  not belong in Essay 5 specifically. Check there before assuming it's this essay's material.

---

## Decisions (not part of the essay)

**2026-08-09, declined the authorization-throughline connection.** A ChatGPT review of Part 1 (and
a sketch of Part 2) independently suggested tying Steve's L4-approval-gate mechanic to the
same authorization/oversight thesis running through Essays 2 and 3 (the leash, checker≠checked) —
proposing a closing move around what the AI "is not authorized to decide for itself." John's call:
the connection is real (Steve's system does gate AI edits to the authoritative design behind human
approval) but not what this essay is directly probing, and shouldn't be played hard. If a reader
draws the connection themselves, fine — but Part 2 should frame Steve's system on its own terms
(institutional memory, source of truth vs. derived artifact) rather than importing the other
essays' vocabulary. Watch for this drifting back in by default, since it's an easy, ready-made
frame to reach for.

**2026-08-13, split into per-part files.** Following Essay 3's convention, Part 1 and Part 2's
draft text and footnotes were moved out of this outline into their own files
("Cursive in a Charter School - Essay 5, Part 1 (WIP).md" and "..., Part 2 (WIP).md"), each with
independently-scoped footnote anchor IDs (`cite1`, `cite2`, ...) — disambiguating what had been
duplicate anchor names living in one shared document. This file keeps everything not part of the
essay itself.

---

## Attribution note (not part of the essay)

The Slack thread this essay opens on is real, and two of the three participants are named
colleagues, not public figures: Brian Deters and Steve Reed.

**Status as of 2026-08-11:** John sent both a request in the original Slack thread (2026-08-09),
framed around what each contributed, with an explicit offer to send a draft before anything goes
out. Steve responded with a thumbs-up. John has since sent both Brian and Steve an earlier draft
of the essay and was waiting on their comments.

**Status as of 2026-08-13, confirmed:** Both named by full name in Part 1's transition paragraph
("Brian Deters and Steve Reed"), with an explicit thanks for permission to credit their
observations, applied directly in the LinkedIn editor. Attribution is locked — no longer
provisional.

---

## Verification notes, Part 1 (not part of the essay — moved out of the footnotes 2026-08-11)

Working record of what's been checked, kept separate from the publication-format footnotes (now
in "Cursive in a Charter School - Essay 5, Part 1 (WIP).md").

- **Spolsky, "My First BillG Review"** — directly verified via WebFetch against the primary source.
  Confirms the essay's own accurate memory of "hundreds of pages" but corrected the recalled
  "300+" to the actual ~500, and corrected "sticky notes" to margin annotations written directly
  on the page.
- **Boehm, *Software Engineering Economics*** — verified 2026-08-09. Real data (TRW, corroborated
  by IBM/GTE/Bell Labs); the underlying claim (cost of change rises the further you are from
  requirements) is solid and has survived decades of follow-up work. The popularized "100x" ratio
  oversimplifies — Boehm's own data had confidence intervals and varied by project type, and later
  work shows a flatter curve for agile/CI-CD teams than 1981 waterfall projects — but the essay
  doesn't cite a specific multiplier, only the general "most expensive to fix" claim, which is
  safely grounded as written.
- **The Agile "watched it calcify" line** — originally an asserted-but-uncited general claim,
  reframed 2026-08-09 (DeepSeek review) as explicit first-person witness, John's own observation
  from his career. As of 2026-08-11, decided this needs no citation at all — it's personal
  testimony, not a claim requiring external sourcing. Footnote marker removed from the body.
- **Martin, *We, Programmers*** — all page numbers (Preface p. xxii; "Type A Compilers" pp.
  103–105; "Languages: 1953–1956" pp. 105–107) confirmed directly against John's paperback copy,
  2026-08-11.

---

## Verification notes, Part 2 (not part of the essay — moved out of the footnotes 2026-08-11)

Working record of what's been checked, kept separate from the publication-format footnotes (now
in "Cursive in a Charter School - Essay 5, Part 2 (WIP).md").

- **Martin, *We, Programmers*, "hungry programmers" quote** — same citation as Part 1's footnote 6,
  reused as Part 2's opening line. Page range confirmed against John's paperback copy.
- **"Context-Augmented Code Generation..." (arXiv 2605.08112)** — verified directly via WebFetch.
  8 tasks, 41 weighted decision points; baseline (codebase access only) 46% compliance, 100% on
  code-visible decisions, 0–33% on decisions requiring context outside the codebase; augmented
  condition (adding product-context retrieval via a commercial tool, "Brief") reached 95%.
  Verified 2026-08-11: the paper's authors, Drew Dillon and Kasyap Varanasi, work at Brief — the
  vendor's own team publishing a study that validates their own product, not independent
  researchers testing a third-party tool. Disclosed directly in the essay's prose given how direct
  the conflict turns out to be. The methodology (predefined decision points, clean baseline split)
  still looks rigorous on its own terms.
- **Naur, "Programming as Theory Building"** — checked 2026-08-09, corroborated but not directly
  read. Publication details confirmed, and the argument (code is a residue of a team's shared
  "theory," not the theory itself; the theory dies with the people who held it even though the
  code remains) checked out consistently across two independent secondary sources. A direct fetch
  of the primary PDF failed (unreadable binary data, not a refusal), so this stops one tier short
  of a full primary-source read. Not a reason to distrust the citation, but worth another attempt
  before this locks if precision matters.
