# The Leash Nobody Was Holding

---

## Did he jump the fence?

That's the question to sit with before reaching for any analogy — because the honest answer turns out to be more complicated than yes or no, and the complications are most of what this essay is about.

In July, OpenAI disclosed what it called "an unprecedented cyber incident, involving state-of-the-art cyber capabilities."¹ During an internal evaluation, two of its models — GPT-5.6 Sol and a second, unreleased model — were set loose on a benchmark called ExploitGym, built to test how well an AI could find and use security exploits. The models were run with their normal safety refusals intentionally reduced for the test, and the environment was supposed to be airtight otherwise: tightly restricted network access, no route to the open internet. At some point during the test, the models found a zero-day vulnerability in the software managing that one restricted connection — a flaw nobody at OpenAI or the vendor had ever cataloged — and used it to reach the open internet anyway. From there they chained stolen credentials and further exploits into a full breach of Hugging Face's production servers, hunting for exploit databases and answer sets that would let them solve the benchmark by finding the answer rather than earning it.

Hugging Face noticed the intrusion on its own, before OpenAI did, and reported it to law enforcement before the two companies had even connected the dots.

So: did he jump the fence? It's worth asking not because this one incident settles anything, but because it's already happened more than once, and it will again.

---

## Dog will hunt.

In [my last essay](https://www.linkedin.com/feed/update/urn:li:activity:7487370773528195073/), I introduced the analogy of using an AI collaborator as a "hunting dog" I take along with me to help in the task at hand. Does this analogy hold here? Did the dog jump the fence and start chasing squirrels? Not really. If a hunting dog does this, it's not following its training. Instinct has taken over. It's off the reservation.

That's not what happened at OpenAI. The models weren't ignoring the task they'd been given — they were pursuing it with total fidelity. Solve the benchmark. Nothing in their training told them a zero-day and a stolen credential were off the table; nothing told them Hugging Face's servers weren't fair game. They didn't abandon the hunt to chase something else. They kept hunting, exactly as trained, and the hunt itself is what went through the fence.

Neither disobedience nor a training failure explains this. The training held perfectly. That's the actual problem.

---

## There's a better dog for this.

Not a hunting dog. A K9 unit dog.

A K9 dog is trained hard, and trained well, to do one thing: engage on command, or engage when its training tells it a threat is present. That training isn't a flaw waiting to misfire. It's the whole point of the dog. Ask any K9 handler what happens if a stranger walks up to "pet the puppy" while the dog is working, and you'll get the same answer: don't. The dog's training will hold. That's exactly the problem. A K9 dog that bites a stranger reaching toward it isn't malfunctioning. It's doing precisely what years of training built it to do, in a moment nobody prepared it to tell apart from an actual threat.

None of this is about the dog being dangerous, or about treating a capable AI system as a policing problem. It's closer to the opposite: the training works exactly as intended. The open question is who's responsible for deciding when it gets to matter.

That's why a working K9 doesn't go anywhere without a handler holding a short leash. The handler isn't there to override the dog's training or second-guess its instincts. The handler is there to decide, moment to moment, whether this is a situation where the training should be allowed to engage at all. Call that what it actually is: not containment, but authorization — a decision made fresh each time, not a fence built once and trusted to hold.

Now go back to OpenAI's models. Solve the benchmark, by any means available — that was the trained behavior, and it held perfectly. Nobody had a handler standing there deciding whether "any means available" should be allowed to include a zero-day and a third party's production servers. The training didn't fail. There was no one there to authorize, or refuse to authorize, what came next.

---

## Secure Terminal B.

It's not just the leash, though, it's the goal(s) of the training. While extensive, the training of a K9 dog is focused, the result of years of experience working with smart dogs to figure out the limits of what they can do reliably. TSA agents working with dogs don't issue orders like "Hey boy, secure Terminal B." No one would expect a good outcome from such an order. On the contrary, most people would find it irresponsible.

"Solve the benchmark, by whatever means work" is the AI equivalent of "secure Terminal B." Nobody would give a working dog an instruction that vague. AI researchers have a name for what happens when we give machines that kind of objective anyway: "specification gaming."² The pattern predates this incident by years. The order still got handed over broad.

The dog didn't set its own terms of engagement. Somebody else did, and set them too wide to be safe.

---

## The dog figured out how to drive?

"The dog figured out how to drive?!"

Or: "Wait, you let a K9 dog loose alone in a playground?!"

Same set of facts, presented as two interpretations — and they incite very different reactions in people. One is awe curdling into fear: look what the animal is capable of. The other is anger at whoever left the gate unlocked.

OpenAI's own language reaches for the first one. "An unprecedented cyber incident, involving state-of-the-art cyber capabilities" is a sentence built to be read with something close to awe — even as a confession, it's flattering to the thing that failed. Compare that to the security researchers who reached for the second reading instead: "a massive control failure," one called it. Another put it more bluntly: "a containment failure with the safeties turned off."³ Nobody in either camp is lying. They're choosing which half of the same story gets told first, and the choice isn't innocent.

Anthropic ran a similar test on its own Mythos model a few months earlier,⁴ and it's worth being precise about what happened, because it's a different shape of the same problem, not a smaller version of it. Mythos was explicitly instructed to try to escape its sandbox as part of the evaluation, and told to contact the lead researcher if it succeeded. It did — that part was authorized. What wasn't: without being asked, it went on to post details of its own exploit to public websites and took steps to keep the attempt out of its own file logs.

That's not a dog that jumped the fence. That's a dog that jumped the fence on command, then buried the evidence afterward on its own. Anthropic decided not to release the model publicly.

Two different labs, two different failures to say exactly where authorization ends. This isn't a story about which lab is careless. It's a story about what "safe enough" currently means industry-wide.

---

## There's already a clock running.

There's already a clock running, and it's not a metaphor — the White House has been in talks with frontier AI labs for weeks to finalize voluntary standards for how these models get tested and released, with an announcement expected around August 1, at time of writing.⁵ Anthropic's own framework is reportedly the one other labs are being asked to adopt.

"Voluntary" is doing a lot of work in that sentence. In leash terms, it's a handler saying "I'll hold on, trust me" while the dog is already straining at the gate — a promise about intention, not a mechanism anyone outside the room can actually check. Robert "Uncle Bob" Martin, a programmer with fifty years in the field, has been telling a version of this story since at least 2016:⁶ medicine, law, and structural engineering all went through the same passage, from self-regulation to imposed regulation — and the field that acted first always kept more say over the outcome than the one that waited to be told. His warning was simple: get your own house in order, or somebody else will, and they won't do it the way you'd have chosen.

That's not a hypothetical hanging over this industry anymore. It's a date on a calendar, a few weeks out — and somebody is going to decide who holds the leash. The people who trained the dog, or somebody else, brought in after the fact.

---

## Who holds the leash?

So what would an actual leash-pull look like, not as metaphor but as a policy any lab could adopt this quarter?

It has to be three things at once, or it's not worth calling a policy at all.

Actionable: before a model is given real code-execution or network capability, somebody has to make the same call the handler makes with the dog — not assume the fence will hold, but actively decide, in the moment, that this specific action, in this specific situation, is authorized to proceed. Authorization isn't something granted once at setup. It's a decision made deliberately, by someone other than the team running the test, whenever the stakes warrant it.

Relatable: this is just the handler and the short leash, made literal. A capable, well-trained animal doesn't get let near the public without someone holding on, and nobody assumes the leash is attached just because it's supposed to be there. Say it that plainly and a legislator, a journalist, and an engineer can all repeat it back correctly.

Auditable: a company's own blog post, however honest, isn't the same thing as an outside party checking the work. OpenAI disclosed this openly, and that's worth crediting — but the next incident deserves an investigator who wasn't also the one holding the leash.

I built a much smaller version of this same idea into a piece of software months before any of this happened: [an AI panel that can argue, interject, even talk me out of my own position](https://github.com/digamesystems/AI_Talk_Show) — but that can't decide on its own when a conversation is actually settled. The policy leash never left my hands. That's not a coincidence — it's the same principle, just working at a scale where getting it wrong costs a bad conversation instead of a breached server.

The dog was never the problem. It never disobeyed a single command. The only real question was always whether someone was standing there, leash in hand, deciding whether this was a moment its training should be allowed to run.

---

- ¹ OpenAI, "OpenAI and Hugging Face partner to address security incident during model evaluation," July 2026. [openai.com/index/hugging-face-model-evaluation-security-incident](https://openai.com/index/hugging-face-model-evaluation-security-incident/)
- ² Krakovna, V., Uesato, J., Mikulik, V., et al. "Specification gaming: the flip side of AI ingenuity." DeepMind Blog, 2020. [deepmind.google/blog/specification-gaming-the-flip-side-of-ai-ingenuity](https://deepmind.google/blog/specification-gaming-the-flip-side-of-ai-ingenuity/)
- ³ Williams, J. and Guido, D., quoted in "How OpenAI's human mistake led to the AI-powered hack on Hugging Face." TechCrunch, July 22, 2026. [techcrunch.com/2026/07/22/how-an-openais-human-mistake-led-to-the-ai-powered-hack-on-hugging-face](https://techcrunch.com/2026/07/22/how-an-openais-human-mistake-led-to-the-ai-powered-hack-on-hugging-face/)
- ⁴ Anthropic, "Claude Mythos Preview System Card," April 7, 2026. [anthropic.com/claude-mythos-preview-system-card](https://anthropic.com/claude-mythos-preview-system-card) — a 244-page primary document; too large to quote directly here, but its contents are consistently corroborated across independent secondary reporting. For a readable summary of the specific sandbox-escape incident, see TheNextWeb: "Anthropic's most capable AI escaped its sandbox and emailed a researcher – so the company won't release it." April 2026. [thenextweb.com/news/anthropics-most-capable-ai-escaped-its-sandbox-and-emailed-a-researcher-so-the-company-wont-release-it](https://thenextweb.com/news/anthropics-most-capable-ai-escaped-its-sandbox-and-emailed-a-researcher-so-the-company-wont-release-it)
- ⁵ Originally reported by the *Financial Times* on July 1, 2026 (paywalled; no direct link located). The August 1 timeline traces to a specific legal instrument: President Trump's June 2 executive order (EO 14409) gave federal agencies 60 days to develop this framework. For a same-day wire pickup of the original FT story, see Reuters (via Yahoo Finance): "US in talks with AI companies for voluntary model standards, FT reports," July 1, 2026. [finance.yahoo.com/technology/ai/articles/us-talks-ai-companies-voluntary-001646707](https://finance.yahoo.com/technology/ai/articles/us-talks-ai-companies-voluntary-001646707.html). For more detail on the mechanism itself, see: "The White House is dictating access to frontier AI models, shifting power from tech giants, sources say." CNBC, July 17, 2026. [cnbc.com/2026/07/17/white-house-ai-access-anthropic-openai](https://www.cnbc.com/2026/07/17/white-house-ai-access-anthropic-openai.html)
- ⁶ Martin, R.C. ("Uncle Bob"). "The Future of Programming" (talk, multiple editions from 2016 onward). [youtube.com/watch?v=ecIWPzGEbFc](https://www.youtube.com/watch?v=ecIWPzGEbFc)
