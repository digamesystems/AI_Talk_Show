# Cursive in a Charter School, Part 1: A Lot of Hungry Programmers

---

In 1992, Joel Spolsky was a program manager on Microsoft's Excel team, finishing the most detailed document he'd ever written: a specification for a new Basic-based programming language for Excel that would eventually become Visual Basic for Applications. It had grown to roughly 500 pages — about a ream of laser-printed paper — headed for something Microsoft called a BillG review, where major features were personally reviewed by Bill Gates.<a id="cite1"></a>[¹](https://www.joelonsoftware.com/2006/06/16/my-first-billg-review/)

Spolsky sent the spec to Gates's office less than 24 hours before the meeting. He assumed nobody could read the whole thing that fast, let alone think carefully about it. Then Gates walked into the room with the spec already in his hand.

He'd read every page. There were notes in the margin of the first page. Then the second. Then, Spolsky realized, every single page in the stack: five hundred pages of handwritten annotation, produced overnight. And as the questions got harder, Gates eventually zeroed in on a specific technical detail: whether Excel's many date and time functions would behave the same way in Basic. Spolsky already knew the answer. There was an exception for January and February 1900 — the legacy behavior Excel had to preserve for compatibility with Lotus 1-2-3.

A real compatibility landmine, buried in a five-hundred-page specification, had become the subject of the hardest question Gates could think to ask — and Spolsky had an answer because he'd already worked through it himself the day before.

That's what a specification could do, in the right hands, before computer time got cheap enough that mistakes were survivable: not paperwork nobody read, but a document detailed enough that reading it carefully was itself a form of engineering.

It didn't last.

---

By the time I started writing code, in the early 1980s, that same upfront-everything model was already collapsing under its own weight. Months of design before a line of code got written. Failure discovered only at the end, when it was most expensive to fix.<a id="cite2"></a>² The industry couldn't respond to change fast enough, and Agile was the answer: stop pretending we could know everything in advance, build something, learn from it, change it. I watched it work, then watched it calcify — scrum masters, certifications, ceremony piling onto something that had started as a rejection of exactly that kind of overhead. Somewhere along the way, the big upfront specification disappeared almost entirely. We learned to surf the change instead of planning around it.

Now, working with LLMs, I'm watching something that looks, at first glance, like a spec-writing
"renaissance." Prompt engineering was becoming a sequence of mini-specs — one for every task,
rewritten until the model got it right. My first reaction was that our fast, strange new
collaborators simply needed more structure up front to keep them from "wandering off into the
weeds." A skill from an ancient era was being reborn — like cursive being taught again, to a new
generation, in a charter school.

I put that observation to a couple of colleagues; Brian Deters and Steve Reed. (Thanks to them for allowing me to credit their observations.) Both of their answers refined my thinking.

---

Brian's reply was essentially this: every technology / language advancement in our field also brought more people into coding, and to whoever was fluent in the layer below, the new arrivals looked exactly like what I'd just called the LLMs — capable, fast, and missing something real. To someone writing assembly, the Python-only coder is the idiot savant who barely understands the machine underneath their own code.

That reframes the whole thing. This isn't spec discipline returning because AI is uniquely untrustworthy. It's the same adjustment the field has made every time an abstraction layer admitted people — or now, systems — that don't share the tacit knowledge of the layer below. Robert "Uncle Bob" Martin, in his recent history of the field, traces that progression from FORTRAN and COBOL through ALGOL, BASIC, C, Unix, object-oriented programming, the internet, Agile, mobile, and finally AI. As he puts it, "we were off to the races."<a id="cite3"></a>³

Each of those was a real disruption, not a metaphorical one. And one of them produced a reaction that looks a lot like the one happening right now.

---

In the early 1950s, Grace Hopper built the first compiler, a program called A-0, that translated a kind of pseudocode into the raw numeric instructions a UNIVAC I could actually run. To prove it worked, she ran a timing comparison: one programmer using A-0 against a team of experienced programmers writing the raw machine code — called C-10 — by hand, on the same problem. The hand-coded team took three programmers a little over 14.5 hours, roughly 44 man-hours combined. The A-0 programmer finished in 48.5 minutes. A factor of over 50.<a id="cite4"></a>⁴

You'd expect that comparison to end the argument. It didn't, for two reasons that both still sound familiar. First, an honest technical one: A-0's compiled programs ran about 30% slower than hand-written C-10, and computer time back then cost roughly ten times what a programmer's time cost. Raw speed wasn't a minor concern. It was the whole economic picture, and for years afterward, "the advantage was still to the raw machine language programmers."<a id="cite5"></a>⁵ Second, a fear with nothing technical about it at all: programmers were afraid a working compiler would put them out of work. If one person with A-0 could do what fifty people used to do by hand, Martin's account puts the worry plainly: there were going to be "a lot of hungry programmers out on the streets."<a id="cite6a"></a>⁶

The clearest resistance, though, didn't come from the programmers worried about their jobs. It came from a peer. When Hopper's team demonstrated an early algebraic compiler — a program that translated ordinary mathematical formulas directly into executable code — John Backus was in the room. Backus is the person who created FORTRAN; he was not a bystander skeptical of things he didn't understand. He watched the demonstration and, in Martin's account, "equat[ed] the work with insanity."<a id="cite7"></a>⁷

That's the friction this essay is actually about. Not ignorance meeting insight. One person who'd already pushed the field forward, looking at someone else's version of the same kind of leap, and calling it crazy.

None of that resistance was fully wrong, either. The 30% performance penalty was real. The job-loss fear wasn't paranoia: compilers genuinely reduced the number of people needed to produce the same output. What eventually resolved the standoff wasn't someone winning an argument. It was infrastructure catching up: the Navy's work on core memory, adopted rapidly once it became public, made computers roughly a hundred times more capable and finally made the compiler's convenience worth its cost.<a id="cite8"></a>⁸

The tradeoff was real on both sides. It just took the ground shifting underneath it before one side's argument stopped being the stronger one.

There were going to be "a lot of hungry programmers out on the streets."<a id="cite6b"></a>⁶

Sound familiar?

---

## Footnotes

1. [↩](#cite1) Joel Spolsky, "My First BillG Review," *Joel on Software*, June 16, 2006.
   [joelonsoftware.com/2006/06/16/my-first-billg-review](https://www.joelonsoftware.com/2006/06/16/my-first-billg-review/)
2. [↩](#cite2) Barry Boehm, *Software Engineering Economics* (1981).
3. [↩](#cite3) Robert C. Martin, *We, Programmers: A Chronicle of Coders from Ada to AI*, 1st ed. (Boston:
   Addison-Wesley Professional, November 30, 2024), ISBN 978-0135344262, Preface, p. xxii.
4–6. [↩ timing](#cite4) [↩ economics](#cite5) [↩ streets](#cite6a) [↩ echo](#cite6b) Martin, *We, Programmers*,
   "Type A Compilers" section, pp. 103–105.
7–8. [↩ Backus](#cite7) [↩ core memory](#cite8) Martin, *We, Programmers*, "Languages: 1953–1956" section,
   pp. 105–107.
