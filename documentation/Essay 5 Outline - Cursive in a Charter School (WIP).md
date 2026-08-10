# Cursive in a Charter School (working title) — Essay 5, Part 1 — DRAFT

*Status: first full draft, unpolished. Title not locked. Written 2026-08-09 from a real Slack
thread (John, Brian Deters, Steve — see note on attribution below) and excerpts from Robert C.
Martin's "We, Programmers," photographed directly from John's purchased Kindle copy.*

---

## Attribution note (not part of the essay)

The Slack thread this essay opens on is real, and two of the three participants (Brian Deters,
"Steve") are named colleagues, not public figures. John is reaching out to confirm they're
comfortable being quoted directly before this locks for publication. Until confirmed, treat any
draft language attributed to them as provisional.

---

## DRAFT TEXT

I'm thinking about how software development has changed during my career, and things are kind
of coming full circle.

When I started writing code around 1980, we were about to work our way out of a paradigm built
on a big upfront specification and a waterfall model: months of design before a line of code got
written, failure discovered only at the end, when it was most expensive to fix.¹ The inability to
respond to change fast enough killed it. Agile replaced it, and eventually accumulated its own
business-driven trappings — scrum masters, certifications, ceremony — that sucked the joy out of
the idea it started from.² Somewhere in that transition, the big upfront spec disappeared
entirely. Teams learned to surf the change instead of planning around it.

Now, working with LLMs, I'm watching the spec come back. These fast, strange collaborators need
an upfront structure to keep from wandering into the weeds, and a skill the ancients had is
getting reborn — like cursive in a charter school.

I put that observation to a couple of colleagues. One answer reframed the whole question.

---

Brian's reply: every one of those transitions also brought more people into coding, and to
whoever was fluent in the layer below, the new arrivals looked exactly like what I'd just called
the LLMs — capable, fast, and missing something real. To someone writing assembly, the
Python-only coder is the idiot savant who barely understands the machine underneath their own
code.

That reframes the whole thing. This isn't waterfall discipline returning because AI is uniquely
untrustworthy. It's the same adjustment the field has made every time an abstraction layer
admitted people — or now, systems — that don't share the tacit knowledge of the layer below. Robert
"Uncle Bob" Martin, who's been writing software since before most of the abstractions in this
essay existed, lists the actual sequence in his own recent history of the field: FORTRAN and
COBOL in the late '50s, ALGOL and SIMULA 67 driving the level up again in the early-to-mid '60s,
structured and object-oriented programming emerging from those, BASIC putting programming in
reach of "almost anyone" by 1964, C and Unix in the late '60s and early '70s — and then, in his
own words, "we were off to the races": mainframe, minicomputer, microcomputer, PC, object-oriented,
internet, Agile, Ruby/Rails, mobile, and now — his own word for it — AI, which "reared up to
threaten everything."³

Each of those was a real disruption, not a metaphorical one, and at least one of them produced a
reaction worth sitting with in detail, because it's the same reaction we're having right now.

---

In the early 1950s, Grace Hopper built the first compiler, a program called A-0, that translated
a kind of pseudocode into the raw numeric instructions a UNIVAC I could actually run. To prove it
worked, she ran a timing comparison: one programmer using A-0 against a team of experienced
programmers writing the raw machine code — called C-10 — by hand, on the same problem. The
hand-coded team took three programmers a little over 14.5 hours, roughly 44 man-hours combined.
The A-0 programmer finished in 48.5 minutes. A factor of over 50.⁴

You'd expect that comparison to end the argument. It didn't, for two reasons that both still
sound familiar. First, an honest technical one: A-0's compiled programs ran about 30% slower than
hand-written C-10, and computer time back then cost roughly ten times what a programmer's time
cost — so raw speed wasn't a minor concern, it was the whole economic picture, and for years
afterward "the advantage was still to the raw machine language programmers."⁵ Second, a fear with
nothing technical about it at all: programmers were afraid a working compiler would put them out
of work. If one person with A-0 could do what fifty people used to do by hand, Martin's account
puts the worry plainly — there were going to be "a lot of hungry programmers out on the
streets."⁶

The clearest resistance, though, didn't come from the programmers worried about their jobs. It
came from a peer. When Hopper's team demonstrated an early algebraic compiler — a program that
translated ordinary mathematical formulas directly into executable code — John Backus was in the
room. Backus is the person who created FORTRAN; he was not a bystander skeptical of things he
didn't understand. He watched the demonstration and, in Martin's account, "equat[ed] the work
with insanity."⁷

That's the friction this essay is actually about. Not ignorance meeting insight. One person who'd
already pushed the field forward, looking at someone else's version of the same kind of leap, and
calling it crazy.

---

None of that resistance was fully wrong, either, which is the part worth being honest about. The
30% performance penalty was real. The job-loss fear wasn't paranoia — compilers genuinely did
collapse the number of people needed to produce the same output, the same way every abstraction
since has. What actually resolved the standoff wasn't someone winning an argument. It was
infrastructure catching up: the Navy's work on core memory, adopted rapidly once it became public,
made computers roughly a hundred times more capable and finally made the compiler's convenience
worth its cost.⁸ The tradeoff was real on both sides. It just took the ground shifting underneath
it before one side's argument stopped being the stronger one.

[SECTION BREAK — Waterfall/Agile arc goes here in more detail if needed, or gets folded upward.
Currently light — may need Boehm's cost-of-change curve cited directly rather than referenced in
passing; not yet independently verified this session, flagging before this locks.]

[SECTION BREAK — closing move: land back on "a lot of hungry programmers out on the streets" as
the line Part 2 opens on. Sound familiar?]

---

## Footnotes (draft — needs full verification pass before publish)

1. General characterization of the waterfall model and its cost-of-change problem — commonly
   attributed to Barry Boehm's cost-of-change curve (*Software Engineering Economics*, 1981).
   **Not yet independently verified this session** — from general knowledge, needs a primary-source
   check before this locks.
2. The Agile Manifesto (agilemanifesto.org, 2001) and the widely-discussed later
   "Agile-industrial-complex" critique (scrum-master certification culture, SAFe, etc.) —
   **general characterization, not yet sourced to a specific citable critique this session.**
3. Robert C. Martin, *We, Programmers: A Chronicle of Coders from Ada to AI* (Addison-Wesley,
   2024) — chronology of language/platform "revolutions," directly excerpted from John's Kindle
   copy. Exact chapter/location TBD (Kindle lacks fixed page numbers).
4–8. Martin, *We, Programmers*, "Languages: 1953–1956" chapter (chapter title confirmed directly
   from excerpt) — Hopper/A-0 timing comparison, the two reasons for resistance, the Backus
   "insanity" reaction, and the core-memory resolution. All directly sourced from John's own
   excerpts. Exact location numbers TBD.
