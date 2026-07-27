# Session Handoff Protocol

For any future AI session (Claude or otherwise) picking this project back up, and for John, as a checklist for starting a new conversation cleanly.

## 1. Entry point — always the same

Start at `documentation/README.md` in the repo. Don't rely on a prior conversation's summary of what's current — files get edited, reorganized, and archived outside of any single conversation (they already have been once). The README, not memory, is the source of truth for "what exists and what matters right now."

## 2. Verify, don't assume

Before treating any file as current: check it actually exists where expected. GitHub is the canonical location; Dropbox is John's local working copy and should not be treated as authoritative if the two ever disagree.

Practical note: GitHub's unauthenticated API (`api.github.com`) rate-limits quickly and unpredictably. If it starts returning rate-limit errors, `git clone --depth 1` the repo instead — it sidesteps the API entirely and has worked reliably every time it's been tried.

## 3. Don't reconstruct from memory what can be re-fetched

Citations, URLs, and quoted transcript excerpts should always be pulled fresh from the actual files, never regenerated from a remembered summary of them. This project has already had to catch several small drift errors this way (a mis-dated citation, a misquoted title). A confident-sounding reconstruction from memory is a real failure mode, not a hypothetical one — verify against source before repeating anything as fact, including things this very document says.

## 4. Use git history as a resource, not just the current file state

The repo is version-controlled. `git log` and `git log -p "documentation/Why I Built a Talk Show (revised draft).md"` on a cloned copy show the actual evolution of the essay — more reliable than any narrative summary of "how the argument changed," including this one.

## 5. The decision log matters as much as the files

`Future Essays - Roadmap.md` captures *what* was deferred and where the material lives. It doesn't fully capture *why* certain close calls were resolved the way they were. Key ones worth knowing before re-litigating them:

- **Otto stays, as a postscript, not the ending.** Multiple AI reviewers (independently) suggested cutting it for a tighter close on the hunting-dog line. The counter-argument that held: Otto is the thing that made John quit eating octopus — real personal stake, not decoration — and the fix was bridging it back to the panel's own argument rather than removing it.
- **"Complementary pressure" was considered and set aside** as an anchoring phrase for being ambiguous between two different claims (a property of the interaction vs. a goal being pursued). "I won't turn until you tell me to. Tell me when we get there." — composed in John's father's voice, not a verbatim memory — replaced it as the rhetorical anchor instead.
- **The essay was deliberately split** into a lean, single-thesis Essay 1 and a full master-draft archive after a review caught that the fuller version had accreted too many theses through iterative addition-only editing. The lesson embedded in that: default to *replacing* material when incorporating new feedback, not just appending to it, or the same accretion problem recurs.
- **Cross-model claims are explicitly unproven.** All current AI Talk Show panelists run on one model family (Claude) with different personas. Any claim that richness comes from genuine model diversity, rather than persona-diversity-on-one-model, is not yet supported — this has been flagged multiple times and should keep being flagged until the cross-model experiment (`GeminiPanelist`/`OpenAIPanelist`) actually exists.

When in doubt about whether a past call is still settled or open to reconsideration, treat it as settled unless John reopens it — don't silently re-decide something that was already argued through.

## 6. A caveat about Claude's memory feature

At the time of writing, this account does not have Claude's cross-conversation memory feature enabled. If it's enabled later, anything surfaced as a "memory" of this project should be treated as a hint to go check, not as a verified fact — the same rule as everything else in this document. Memory summaries compress and can misstate; the files don't.

## 7. Bootstrap prompt

The following is meant to be pasted as the first message in a new conversation, verbatim or adapted:

> Continuing the AI Talk Show essay project. Start by reading `documentation/README.md` and `documentation/Future Essays - Roadmap.md` at github.com/digamesystems/AI_Talk_Show, and `documentation/Session Handoff Protocol.md` in the same folder. Don't assume any prior conversation's context is accurate — verify current file state before proceeding, and treat anything you "remember" about this project as unverified until you've checked it against these files.
