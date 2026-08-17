# Cursive in a Charter School, Part 2: The Margins

*(Second of a two-part essay. Continues directly from
[Part 1, "A Lot of Hungry Programmers"](https://www.linkedin.com/feed/update/urn:li:ugcPost:7493709876209057792/).
Working notes, decisions, and source verification for both parts live in
"Essay 5 Outline - Cursive in a Charter School (WIP).md". Footnote numbering restarts at 1,
matching Essay 3's convention of independent numbering per part.)*

---

There were going to be "a lot of hungry programmers out on the streets."<a id="cite1"></a>¹

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

That's not a hypothetical question anymore. A 2026 study measured it directly.<a id="cite2"></a>[²](https://arxiv.org/pdf/2605.08112)

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
the way it did.<a id="cite3"></a>[³](https://doi.org/10.1016/0165-6074(85)90032-8) The code was just a residue of that theory, readable proof that it had once
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
— five hundred pages, annotated overnight, by someone who'd read closely enough to ask the one
question that actually mattered.

But the discipline isn't lost. It's being redirected toward a different kind of reader: one with
no institutional context of its own — capable and fast on everything visible in the code, and
exactly as unreliable as the study above on everything that wasn't.

We're not going back to Spolsky's 500-page specification. We're figuring out how to hand a reader
with no history of its own the thing Gates already had: the margins.

---

## Footnotes

1. [↩](#cite1) Robert C. Martin, *We, Programmers: A Chronicle of Coders from Ada to AI*, 1st ed. (Boston:
   Addison-Wesley Professional, November 30, 2024), ISBN 978-0135344262, "Type A Compilers"
   section, pp. 103–105.
2. [↩](#cite2) "Context-Augmented Code Generation: How Product Context Improves AI Coding Agent Decision
   Compliance by 49%," arXiv 2605.08112, April 2026.
   [arxiv.org/pdf/2605.08112](https://arxiv.org/pdf/2605.08112)
3. [↩](#cite3) Peter Naur, "Programming as Theory Building," *Microprocessing and Microprogramming*, May 1985
   (DOI: 10.1016/0165-6074(85)90032-8).

---

## LinkedIn post copy (not part of the essay itself)

**Blurb saved 2026-08-13, for use when publishing:**

> An AI coding agent got 100% of the decisions right when the answer was visible in the code.
>
> On the decisions that weren't written down anywhere — the ones that lived in a Slack thread, a meeting, someone's memory — it got as low as zero.
>
> A colleague of mine had already built an answer to it, without calling it AI safety, or context engineering, or anything else with a name.
>
> He just wrote down the part that used to live only in people's heads.
