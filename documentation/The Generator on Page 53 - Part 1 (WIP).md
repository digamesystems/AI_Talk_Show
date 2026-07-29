# The Generator on Page 53, Part 1: The Playbook

*(First of a two-part essay. Part 2 continues directly from this one. Footnotes not yet added; sources are logged in the outline file.)*

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

---

Here's what Waffle House actually built, stated plainly. Nobody's standing at the counter making a judgment call in the moment, the way Mel does — that dies with him. And nobody wrote a sign for every specific way a hurricane could go wrong — that's the diner's dozen, scaled up to absurdity. What they built instead is a boundary, set once, in advance, wide enough to cover a whole class of disaster rather than one specific storm — and then they trained people to move fast and freely inside it, without checking in every time.

That's the same question the last essay ended on, wearing a different coat. Who holds the leash? The last essay's answer was one person, in one room, making one call. Waffle House's answer is different, and it's the one that actually scales: the leash gets set once, by someone with the authority to decide what counts as inside the boundary, and then it's handed to trained people who don't have to ask permission for every move underneath it. The policy leash doesn't leave headquarters. It just isn't gripped so tight that it slows down everything happening at the other end of it.

That's authorization at a scale no single handler could manage — and it didn't require inventing anything new.

---

Nobody could have written a sign for Katrina before Katrina happened. That's just true of every system, always — you cannot prepare for a category of disaster that hasn't occurred to anyone yet, because nobody knows to ask about it.

What separates the diner from Waffle House isn't that one of them saw the future and the other didn't. It's what each of them did with the thing that actually happened.

The diner's answer was a sign. One sign, for one backpack, on one counter. If the next problem is a wet umbrella instead of a backpack, the sign is useless — it was never written broadly enough to cover anything except the exact thing that already occurred. A dozen years of incidents produces a dozen narrow patches, each one blind to everything adjacent to it.

Security researchers call the better version of this response variant analysis² — it's the actual, established term, not a phrase invented for this essay — and they've been doing it for decades. When a genuinely new category of vulnerability turns up — a buffer overflow, a SQL injection, whatever the next one turns out to be called — the response isn't just patching the specific exploit that got found. It's using that one exploit as a seed, feeding it to fuzzers and similar tools built to hunt down every other unexploited member of the same family. One incident teaches the shape of an entire category, and the category is what gets defended, not just the instance.

That's what Waffle House actually did. Hugo didn't teach them "close for three days when a hurricane hits the Carolinas." It taught them that closing chaotically, without a plan, was itself the problem — a category, not an instance. Katrina produced the actual comprehensive playbook: what to serve without power, what to serve without ice, how to move people and supplies across a hundred locations at once. None of that specifically prevents the next hurricane from happening. All of it is built to handle the next one, and the one after that, regardless of which coastline it hits or how it behaves once it gets there.

The measure of a good system was never whether it prevented the unimaginable. Nothing does that. The measure is what it builds the moment the unimaginable finally happens once.

---

So what does a restaurant chain have to do with AI? A lot, it turns out — starting with a sandbox that wasn't as sealed as anyone thought. We will explore this in part 2.
