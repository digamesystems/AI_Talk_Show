# Cursive in a Charter School (working title) — Essay 5, Part 1 — DRAFT

*Status: second draft pass, unpolished. Title not locked. Written 2026-08-09 from a real Slack
thread (John, Brian Deters, Steve — see note on attribution below), excerpts from Robert C.
Martin's "We, Programmers" photographed directly from John's purchased Kindle copy, and Joel
Spolsky's "My First BillG Review" (verified directly via WebFetch). Opening reworked to lead with
the Gates/Spolsky scene instead of John's own reflection, per the "open on a concrete scene"
convention the rest of this series follows — the reflection now lands as the pivot into Brian's
reframe instead of as the essay's own opening.*

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

---

## Attribution note (not part of the essay)

The Slack thread this essay opens on is real, and two of the three participants (Brian Deters,
"Steve") are named colleagues, not public figures. John is reaching out to confirm they're
comfortable being quoted directly before this locks for publication. Until confirmed, treat any
draft language attributed to them as provisional.

**Status as of 2026-08-11:** John sent both a request in the original Slack thread (2026-08-09),
framed around what each contributed, with an explicit offer to send a draft before anything goes
out. Steve responded with a thumbs-up. John has since sent both Brian and Steve an earlier draft
of the essay and is waiting on their comments. Note this is still short of final sign-off — an
earlier draft was sent, not the current text, and neither has confirmed the actual language yet.
Don't treat either attribution as locked until they've responded to the draft itself.

---

## Verification notes, Part 1 (not part of the essay — moved out of the footnotes 2026-08-11)

Working record of what's been checked, kept separate from the publication-format footnotes below.

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

## DRAFT TEXT

In 1992, Joel Spolsky was a program manager on Microsoft's Excel team, finishing the most detailed document he'd ever written: a specification for a new Basic-based programming language for Excel that would eventually become Visual Basic for Applications. It had grown to roughly 500 pages — about a ream of laser-printed paper — headed for something Microsoft called a BillG review, where major features were personally reviewed by Bill Gates.¹

Spolsky sent the spec to Gates's office less than 24 hours before the meeting. He assumed nobody could read the whole thing that fast, let alone think carefully about it. Then Gates walked into the room with the spec already in his hand.

He'd read every page. There were notes in the margin of the first page. Then the second. Then, Spolsky realized, every single page in the stack: five hundred pages of handwritten annotation, produced overnight. And as the questions got harder, Gates eventually zeroed in on a specific technical detail: whether Excel's many date and time functions would behave the same way in Basic. Spolsky already knew the answer. There was an exception for January and February 1900 — the legacy behavior Excel had to preserve for compatibility with Lotus 1-2-3.

A real compatibility landmine, buried in a five-hundred-page specification, had become the subject of the hardest question Gates could think to ask — and Spolsky had an answer because he'd already worked through it himself the day before.

That's what a specification could do, in the right hands, before computer time got cheap enough that mistakes were survivable: not paperwork nobody read, but a document detailed enough that reading it carefully was itself a form of engineering.

It didn't last.

---

By the time I started writing code, in the early 1980s, that same upfront-everything model was already collapsing under its own weight. Months of design before a line of code got written. Failure discovered only at the end, when it was most expensive to fix.² The industry couldn't respond to change fast enough, and Agile was the answer: stop pretending we could know everything in advance, build something, learn from it, change it. I watched it work, then watched it calcify — scrum masters, certifications, ceremony piling onto something that had started as a rejection of exactly that kind of overhead. Somewhere along the way, the big upfront specification disappeared almost entirely. We learned to surf the change instead of planning around it.

Now, working with LLMs, I'm watching something that looks, at first glance, like a spec-writing
"renaissance." Prompt engineering was becoming a sequence of mini-specs — one for every task,
rewritten until the model got it right. My first reaction was that our fast, strange new
collaborators simply needed more structure up front to keep them from "wandering off into the
weeds." A skill from an ancient era was being reborn — like cursive being taught again, to a new
generation, in a charter school.

I put that observation to a couple of colleagues. One answer reframed the whole question.

---

Brian's reply was essentially this: every one of those transitions also brought more people into coding, and to whoever was fluent in the layer below, the new arrivals looked exactly like what I'd just called the LLMs — capable, fast, and missing something real. To someone writing assembly, the Python-only coder is the idiot savant who barely understands the machine underneath their own code.

That reframes the whole thing. This isn't spec discipline returning because AI is uniquely untrustworthy. It's the same adjustment the field has made every time an abstraction layer admitted people — or now, systems — that don't share the tacit knowledge of the layer below. Robert "Uncle Bob" Martin, in his recent history of the field, traces that progression from FORTRAN and COBOL through ALGOL, BASIC, C, Unix, object-oriented programming, the internet, Agile, mobile, and finally AI. As he puts it, "we were off to the races."³

Each of those was a real disruption, not a metaphorical one. And one of them produced a reaction that looks a lot like the one happening right now.

---

In the early 1950s, Grace Hopper built the first compiler, a program called A-0, that translated a kind of pseudocode into the raw numeric instructions a UNIVAC I could actually run. To prove it worked, she ran a timing comparison: one programmer using A-0 against a team of experienced programmers writing the raw machine code — called C-10 — by hand, on the same problem. The hand-coded team took three programmers a little over 14.5 hours, roughly 44 man-hours combined. The A-0 programmer finished in 48.5 minutes. A factor of over 50.⁴

You'd expect that comparison to end the argument. It didn't, for two reasons that both still sound familiar. First, an honest technical one: A-0's compiled programs ran about 30% slower than hand-written C-10, and computer time back then cost roughly ten times what a programmer's time cost. Raw speed wasn't a minor concern. It was the whole economic picture, and for years afterward, "the advantage was still to the raw machine language programmers."⁵ Second, a fear with nothing technical about it at all: programmers were afraid a working compiler would put them out of work. If one person with A-0 could do what fifty people used to do by hand, Martin's account puts the worry plainly: there were going to be "a lot of hungry programmers out on the streets."⁶

The clearest resistance, though, didn't come from the programmers worried about their jobs. It came from a peer. When Hopper's team demonstrated an early algebraic compiler — a program that translated ordinary mathematical formulas directly into executable code — John Backus was in the room. Backus is the person who created FORTRAN; he was not a bystander skeptical of things he didn't understand. He watched the demonstration and, in Martin's account, "equat[ed] the work with insanity."⁷

That's the friction this essay is actually about. Not ignorance meeting insight. One person who'd already pushed the field forward, looking at someone else's version of the same kind of leap, and calling it crazy.

None of that resistance was fully wrong, either. The 30% performance penalty was real. The job-loss fear wasn't paranoia: compilers genuinely reduced the number of people needed to produce the same output. What eventually resolved the standoff wasn't someone winning an argument. It was infrastructure catching up: the Navy's work on core memory, adopted rapidly once it became public, made computers roughly a hundred times more capable and finally made the compiler's convenience worth its cost.⁸

The tradeoff was real on both sides. It just took the ground shifting underneath it before one side's argument stopped being the stronger one.

There were going to be "a lot of hungry programmers out on the streets."⁶

Sound familiar?


---

## Footnotes

1. Joel Spolsky, "My First BillG Review," *Joel on Software*, June 16, 2006.
   [joelonsoftware.com/2006/06/16/my-first-billg-review](https://www.joelonsoftware.com/2006/06/16/my-first-billg-review/)
2. Barry Boehm, *Software Engineering Economics* (1981).
3. Robert C. Martin, *We, Programmers: A Chronicle of Coders from Ada to AI*, 1st ed. (Boston:
   Addison-Wesley Professional, November 30, 2024), ISBN 978-0135344262, Preface, p. xxii.
4–6. Martin, *We, Programmers*, "Type A Compilers" section, pp. 103–105.
7–8. Martin, *We, Programmers*, "Languages: 1953–1956" section, pp. 105–107.

---

# Cursive in a Charter School, Part 2: The Margins — DRAFT

*Status: first full draft, unpolished. Written 2026-08-09, same session as Part 2's outline
negotiation (see decisions above — no authorization-throughline language, ending lands on the
margins image rather than on Naur, revision-log meta-point deliberately excluded per Roadmap
entry 18). Footnote numbering restarts at 1, matching Essay 3's convention of independent
numbering per part.*

---

## Verification notes, Part 2 (not part of the essay — moved out of the footnotes 2026-08-11)

Working record of what's been checked, kept separate from the publication-format footnotes below.

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

---

## DRAFT TEXT — PART 2

There were going to be "a lot of hungry programmers out on the streets."¹

That was the fear in the early 1950s, when Grace Hopper's compiler first threatened to do the
work of fifty programmers with one.

Every abstraction jump since has produced some version of the same feeling: the layer below
getting further away, and someone who understood it worrying that whoever's standing on top of it
now doesn't understand anything at all. That was Brian's point: assembly to FORTRAN, structured
programming to objects, hand-managed memory to garbage collection. Each time, the field adjusted.
Nothing about that pattern requires AI to be uniquely dangerous, or uniquely capable, or uniquely
anything.

But something about this jump is still worth taking seriously on its own terms, not because the
machine is untrustworthy, but because of what got cheap.

A compiler translated what a programmer had already specified. An LLM coding agent works from
something much thinner: a description, a conversation, a half-finished sentence. It produces
working code anyway. That's not evidence the machine is smarter than a compiler. It's evidence
that turning intent into implementation just got radically cheaper, the same way A-0 made turning
pseudocode into machine code radically cheaper in 1952. And every time that particular cost
collapses, whatever holds the intent that isn't in the implementation suddenly matters again: the
same way Gates's margin notes mattered when producing working software was still expensive enough
that someone needed to read five hundred pages before signing off on it.

So: what happens when the cost of implementation collapses, and the intent behind it still isn't
written down anywhere the machine can see?

---

That's not a hypothetical question anymore. A 2026 study measured it directly.²

Researchers gave a coding agent eight realistic engineering tasks, seeded with 41 decision points,
the kind of call a real team makes constantly and rarely writes down: which UI components are
canonical versus deprecated, which middleware is mandatory, which shortcut is fine and which one
quietly violates something nobody remembered to explain. Working from the codebase alone, the
agent got 100% of the decisions that were visible in the code itself. On the decisions that
weren't — the ones living in a product doc, a design conversation, someone's memory of why a thing
was built that way — it got between zero and 33%. Give the same agent access to that missing
context through Brief — a self-study, in effect, since the researchers work for the company that
makes it — and overall compliance jumped from 46% to 95%.

The code was never the problem. The code was fine. What the agent couldn't do was see the parts of
the system that had never been code in the first place.

---

I put this to a colleague, Steve, who's been running an AI-assisted team for a while now. I
expected him to say something about better prompting.

He showed me what he'd actually built instead.

Four layers of documentation, one file per component at each layer, deliberately different in
size and audience. L1 — roughly thirty tokens each — an elevator pitch: what the system is, what
it's built on, how the pieces map out. L2 — roughly two hundred tokens — how the components
actually talk to each other. L3 — roughly five hundred tokens — file-level guidance, specific
enough to work from directly. And L4: a real, human-readable design document, no token budget, no
compression. The kind of writing a person sits down and actually composes.

The first three get regenerated automatically, every pull request. The fourth doesn't move without
a human's permission.

"L1-3 are token dense," Steve told me. "The audience of those is 100% AI, so they're maintained to
get all the info to the AI quickly and not have human language fluff." That's a genuinely strange
sentence. Documentation has been written for human readers for as long as documentation has
existed. This is documentation written for a reader that isn't one: stripped, on purpose, of the
very qualities that make writing pleasant for a person, because the intended reader doesn't need
them and the token budget doesn't have room for them anyway.

L4 is different, and its difference is the point. When Steve's team needs to change something real
about the system's design, they don't touch L1 through L3 directly. They go to L4, work through
the change with the AI's help, and only once a human approves it does the AI regenerate the
compressed layers underneath. Proposing and committing are two different acts, done in sequence,
not because the AI can't be trusted with ideas, but because the record of *why* the system looks
the way it does isn't allowed to change until someone actually decides it should.

That record turns out to matter in a way Steve might not have fully anticipated when he built it. "The fact
that it can see the design evolution in the L4 docs has helped in a lot of cases," he said,
"especially on bugs, when I can see why system X has a bug now based on system Y changing a month
ago and we missed one interaction point when changing that." Not just a description of what the
system currently does. A history of why it became that way, kept specifically so a bug six weeks
later can be traced back to the decision that caused it.

---

There's an old idea hiding underneath what Steve built, forty years old, from before any of this
existed. In 1985 the computer scientist Peter Naur argued that the real product of programming was
never the code itself: it was the theory a team held in their heads about why the program worked
the way it did.³ The code was just a residue of that theory, readable proof that it had once
existed. Lose the people who held it: they leave, memory fades, six months pass. The code doesn't
get worse. It just becomes much harder to change correctly, because the reasoning that made it
safe to change is gone, even though every line still compiles.

Naur was writing about human turnover — the people who built the system, leaving and taking their
knowledge with them. He had no reason to imagine a collaborator that shows up with zero theory of
the system by default, every single session, unless someone hands it one. But
that's exactly the gap Steve's L4 is built to close. Not documentation in the old sense, a
description of what exists, but an externalized version of the thing Naur said actually mattered:
the theory, kept in a form durable enough to survive whoever, or whatever, is asking about it next.

---

None of this is Waterfall coming back, whatever it might look like from a distance. Waterfall
tried to know everything before a line of code got written, and the industry broke itself trying
to keep that pretense alive. Agile's answer was honest: nobody can actually know everything in
advance, so stop pretending, and build a process that survives being wrong. What Steve's system
does is neither. It doesn't freeze the design, and it doesn't let the reasoning disappear when the
design changes. It lets the implementation move as fast as Agile ever wanted, while keeping the one thing the big upfront spec
used to protect, and Agile never meant to throw away along with it: a place where the reasoning
survives the people who had it in their heads.

---

Gates filled the margins of Spolsky's specification with everything he knew that the document
itself couldn't say: decades of industry knowledge, brought to bear on someone else's writing, in
his own hand. It's tempting to read that as the high-water mark of a discipline we've since lost
— five hundred pages, annotated overnight, by someone who understood what he was reading closely
enough to catch a bug no one else had found.

But the discipline isn't lost. It's being redirected toward a different kind of reader: one with
no institutional context of its own — capable and fast on everything visible in the code, and
exactly as unreliable as the study above on everything that wasn't.

We're not going back to Spolsky's 500-page specification. We're figuring out how to hand a reader
with no history of its own the thing Gates already had: the margins.

---

## Footnotes

1. Robert C. Martin, *We, Programmers: A Chronicle of Coders from Ada to AI*, 1st ed. (Boston:
   Addison-Wesley Professional, November 30, 2024), ISBN 978-0135344262, "Type A Compilers"
   section, pp. 103–105.
2. "Context-Augmented Code Generation: How Product Context Improves AI Coding Agent Decision
   Compliance by 49%," arXiv 2605.08112, April 2026.
   [arxiv.org/pdf/2605.08112](https://arxiv.org/pdf/2605.08112)
3. Peter Naur, "Programming as Theory Building," *Microprocessing and Microprogramming*, May 1985
   (DOI: 10.1016/0165-6074(85)90032-8).
