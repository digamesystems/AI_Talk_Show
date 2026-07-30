# The Generator on Page 53, Part 1: The Playbook

*(First of a two-part essay. Part 2 continues directly from this one.)*

---

I've been to a lot of diners around college campuses. If a diner has been around for years, there is a pretty common feature you see: custom signs, often handwritten, taped to the wall. "No backpacks on the counter!", "Cash only. (U.S. currency!)", "We reserve the right to refuse service." In an old place there can be quite a few of these signs — sometimes approaching a dozen.

"Why no backpacks on the counter?" I wonder. Well, something happened. There's a story that turned out badly for someone. The backpack turned into a catalyst for a policy decision that turned into regulation. It's the same for every one of the other signs. Something bad happened. We had to make a rule so it doesn't happen again.

Sound familiar?

A lot of diners are like this.

Then there's Mel's Diner.

Mel's has been around forever. So has Mel. There aren't a lot of signs at Mel's. If a backpack lands on the counter, Mel walks by, stares significantly at it, then at the customer and the backpack usually disappears without a comment. No fall back on a written policy, just an understanding of the limits of the system communicated without words by the operator. If you've been to Mel's a couple of times, you quickly get a sense of what the limits are. Why is this? Answer: context — Mel.

Then there's Waffle House.

Not a wall of signs. Not one man's stare. Something else.

Hurricane Hugo hit in 1989, and it didn't leave Waffle House with a plan — it left them with a decision. The response was chaotic enough that the company resolved to systemize whatever came next. What came next was Katrina. In 2005, the storm destroyed seven Waffle House restaurants outright and shut down more than a hundred others along the I-10 corridor. That's the incident that actually produced a written plan.

The plan is specific in a way a sign never is. It covers what you can serve with no electricity. What you can serve with no ice. It has "jump teams" — managers trained and pre-authorized to mobilize the moment a storm shows up on the radar, without waiting for headquarters to sign off on each move. It has a mobile command center watching the weather and shuffling people and supplies to wherever the next location is about to need them. None of this is one person's feel for the room. All of it is written down, and updated every time a new storm teaches the company something the last one didn't.

Waffle House got so good at handling disasters that FEMA — the government agency actually responsible for handling them — sat up and took notice. A former administrator, Craig Fugate, coined an informal metric now called the Waffle House Index: green if a location's open with a full menu, yellow if it's running on a generator with a shortened one, red if it's closed outright. Emergency managers treat it as a real severity gauge in its own right — a fast, on-the-ground read of how bad a disaster actually is, sitting right alongside the official wind-speed scales.

Fugate has since described what's actually running underneath all of it, and he didn't reach for corporate language to do it. It's the OODA loop¹ — observe, orient, decide, act, a decision cycle built decades earlier for fighter pilots by military strategist John Boyd — "minus the Pentagon PowerPoint," he said.

Not a sign, and not a stare. Something written down well enough to survive anyone leaving, built to let real judgment run inside a boundary somebody set in advance.

The diners solved neither problem. Mel solved both — but only because one person carried both the judgment and the authority to act on it, in his own head. Waffle House is what happens when you split the two apart.

---

Here's what Waffle House actually built, stated plainly. Nobody's standing at the counter making a judgment call in the moment, the way Mel does — that dies with him. And nobody wrote a sign for every specific way a hurricane could go wrong — that's the diner's dozen, scaled up to absurdity. What they built instead is a boundary, set once, in advance, wide enough to cover a whole class of disaster rather than one specific storm — and then they trained people to move fast and freely inside it, without checking in every time.

That's the same question [the last essay](https://www.linkedin.com/feed/update/urn:li:activity:7488556546730156033/) ended on, wearing a different coat — who holds the leash on a system trained to act, deciding moment to moment whether that training should be allowed to run. The last essay's answer was one person, in one room, making one call. Waffle House's answer is different, and it's the one that actually scales: the leash gets set once, by someone with the authority to decide what counts as inside the boundary, and then it's handed to trained people who don't have to ask permission for every move underneath it. The policy leash doesn't leave headquarters. It just isn't gripped so tight that it slows down everything happening at the other end of it.

That's authorization at a scale no single handler could manage — and it didn't require inventing anything new.

But authorization is only half of what Waffle House built, and it's worth separating the two cleanly, because they solve different problems. Authorization answers *who gets to act without checking in*. It says nothing about *what they're prepared to act on*. A jump team empowered to move fast is still only as good as what the Playbook tells them to expect — and no one, in 1989, could write a Playbook for a storm that hadn't happened yet.

---

Nobody could have written a sign for Katrina before Katrina happened. That's just true of every system, always — you cannot prepare for a category of disaster that hasn't occurred to anyone yet, because nobody knows to ask about it.

What separates the diner from Waffle House isn't that one of them saw the future and the other didn't. It's what each of them did with the thing that actually happened.

The diner's answer was a sign. One sign, for one backpack, on one counter. If the next problem is a wet umbrella instead of a backpack, the sign is useless — it was never written broadly enough to cover anything except the exact thing that already occurred. A dozen years of incidents produces a dozen narrow patches, each one blind to everything adjacent to it.

Security researchers call the better version of this response variant analysis² — and they've been doing it for decades. When a genuinely new category of vulnerability turns up — a buffer overflow, a SQL injection, whatever the next one turns out to be called — the response isn't just patching the specific exploit that got found. It's using that one exploit as a seed, feeding it to fuzzers and similar tools built to hunt down every other unexploited member of the same family. One incident teaches the shape of an entire category, and the category is what gets defended, not just the instance.

That's what Waffle House actually did. Hugo didn't teach them "close for three days when a hurricane hits the Carolinas." It taught them that closing chaotically, without a plan, was itself the problem — a category, not an instance. Katrina turned that lesson into the actual comprehensive Playbook, covering supplies and coordinated logistics across a hundred locations at once. None of that specifically prevents the next hurricane from happening. All of it is built to handle the next one, and the one after that, regardless of which coastline it hits or how it behaves once it gets there.

Authorization and generalization, working together, are what actually let Waffle House scale. One without the other fails in a specific, predictable way. Generalization without authorization is Mel's own accumulated wisdom, captured on paper at last — a very good document that still requires someone to call headquarters before acting on it, defeating the whole point of writing it down in the first place. Authorization without generalization is delegating real trust to people equipped with nothing but a single dozen-signs' worth of narrow, backward-looking rules — fast, but blind to anything that hasn't happened yet. Waffle House needed both, and built both, and neither one substitutes for the other.

The measure of a good system was never whether it prevented the unimaginable. Nothing does that. The measure is what it builds the moment the unimaginable finally happens once.

---

Waffle House isn't a novelty act. It's one instance of a shape that keeps reappearing wherever an industry has decided "hope it doesn't happen again" isn't good enough.

Aviation runs on the same shape. In 1976, NASA and the FAA set up the Aviation Safety Reporting System³ — a way for pilots, controllers, and crew to report close calls and near-misses, no names attached, no punishment attached, specifically so people would actually report the thing they got away with instead of quietly filing it away as a story for the crew lounge. Fifty years and more than two million reports later, it's issued thousands of safety alerts built from exactly the pattern Waffle House uses: one incident, generalized into a category, distributed to everyone who might face the same one next.

Nuclear power did something even more direct. After Three Mile Island in 1979, the industry didn't wait for Washington to write new rules and hand them down. It built its own — the Institute of Nuclear Power Operations⁴, a body the utilities themselves fund, staff, and submit to, which rates every plant in the country and makes those ratings matter. Every U.S. utility with a nuclear plant has been a continuous member since. Self-policing, done seriously enough that a sitting NRC chair can point to it this year and mean it as praise, not as a euphemism for "we let them off easy."

Three completely different industries — short-order breakfast, commercial aviation, nuclear power — landed on the same architecture out of three different disasters, because the alternative in all three cases was someone from outside deciding the industry couldn't be trusted to run itself.

That's not one company's clever idea, borrowed around. That's independent convergence — three separate fields solving the same problem the same way, without copying each other, under nothing but their own pressure to survive.

That's worth sitting with before AI ever enters this essay. This isn't a hypothetical shape borrowed for the occasion. It's a shape multiple high-stakes industries have already built, under real pressure, and it's held.

---

AI doesn't have one of these yet. Not really — not one built by the labs themselves, running long enough and seriously enough for an outside regulator to point to the way the NRC points to INPO. And the field is still young enough that a small number of public failures could do to it what a small number of failures can always do to something this new: decide, for everyone, that self-regulation was never a serious offer to begin with.⁵

So: what does a restaurant chain, a fifty-year-old aviation reporting system, and a nuclear industry's own internal watchdog actually have to teach a technology moving faster than any of them ever did? Part 2 finds out.

---

- ¹ Fugate, Craig. LinkedIn post, "The Waffle House Plan: Show up after a hurricane..." 2026. [linkedin.com/posts/craigfugateconsultingllc_the-waffle-house-plan-show-up-after-a-hurricane-activity-7364664681640194049-SQCC](https://www.linkedin.com/posts/craigfugateconsultingllc_the-waffle-house-plan-show-up-after-a-hurricane-activity-7364664681640194049-SQCC?utm_source=share&utm_medium=member_desktop&rcm=ACoAAAdp4aEBvvNLC5ZB2KEhvAf2BL9TQsHyx2M). For a secondary write-up quoting the same post in full, see: Abraham, Jeanny. "The Waffle House Effect: How They Impacted How Storms are Measured While Keeping Hot Meals Ready." *Automotive Fleet*, April 30, 2026. [automotive-fleet.com/articles/the-waffle-house-effect-how-they-impacted-how-storms-are-measured-while-keeping-hot-meals-ready](https://www.automotive-fleet.com/articles/the-waffle-house-effect-how-they-impacted-how-storms-are-measured-while-keeping-hot-meals-ready)
- ² "Variant Analysis." *DZone Refcards*. [dzone.com/refcardz/variant-analysis-1](https://dzone.com/refcardz/variant-analysis-1) — defines variant analysis as "the process of taking a known problem, such as a crashing bug or security vulnerability, and finding other occurrences (or 'variants') of that problem in a codebase."
- ³ NASA, "Aviation Safety Reporting System." [nasa.gov/human-systems-integration-division/aviation-safety-reporting-system-overview](https://www.nasa.gov/human-systems-integration-division/aviation-safety-reporting-system-overview) — established 1976 as a joint NASA/FAA program; voluntary, confidential, non-punitive; over 2 million reports collected to date. See also NASA, "40 Years of Safer Aviation Through Reporting" (over 6,200 safety alerts issued from the program). [nasa.gov/aeronautics/40-years-of-safer-aviation-through-reporting](https://www.nasa.gov/aeronautics/40-years-of-safer-aviation-through-reporting/)
- ⁴ World Nuclear Association, "Cooperation in Nuclear Power." [world-nuclear.org/information-library/current-and-future-generation/cooperation-in-nuclear-power](https://world-nuclear.org/information-library/current-and-future-generation/cooperation-in-nuclear-power) — INPO established 1979 following Three Mile Island; self-regulation and safety enhancement through peer review, funded and staffed by member utilities. For a current (2026) statement from a sitting regulator: Ho Nieh, chair of the U.S. Nuclear Regulatory Commission, quoted in "A critical moment for the nuclear safety policeman," *E&E News/POLITICO*, April 10, 2026: "The high levels of safety and performance and reliability that exist today are possible because of what INPO does." [eenews.net/articles/a-critical-moment-for-the-nuclear-safety-policeman](https://www.eenews.net/articles/a-critical-moment-for-the-nuclear-safety-policeman/)
- ⁵ Martin, R.C. ("Uncle Bob"). "The Future of Programming" (talk, multiple editions from 2016 onward). [youtube.com/watch?v=ecIWPzGEbFc](https://www.youtube.com/watch?v=ecIWPzGEbFc) — the same self-regulate-or-be-regulated warning cited at length in [the last essay](https://www.linkedin.com/feed/update/urn:li:activity:7488556546730156033/).
