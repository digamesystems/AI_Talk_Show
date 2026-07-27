# Why I Built a Talk Show

## 1. A Map

In a wood-paneled station wagon in 1973–4 my sister and I were sitting in the back, ready for our annual family trip from Tucson, AZ to Duluth, MN, roughly 1800 miles. I was about 9. Sitting in the driveway, with car packed, my father reaches across the immense front seat and opens the glove box to fish around and hands me a map of the US highway system. "Johnny, you and Julie are the navigators for this trip. I'm the pilot. Get us there!"

Dad was a navigator/bombardier in the Korean War. He could get there with his eyes closed.

"I won't turn until you tell me to."

For the next two days we were glued to the map except for when we looked over his shoulder to check the odometer.

We got there.

## 2. A Map vs. A GPS

David Krakauer, President of the Santa Fe Institute, has argued that we can sort the "cognitive artifacts" — tools we've built to help us navigate the world — into two families.¹ *Complementary* artifacts are things like a pencil, an abacus, or a sextant: tools that make you smarter, and that leave you smarter even after you set them down. *Competitive* artifacts are things like a GPS, or a Large Language Model: tools prone to handing you a solution instead of helping you build one, and that leave you no better off than when you started, once they're taken away.

His classic case study is the map versus the GPS. Both get you from one place to another, but one builds an internal model of the city — or the highway system — that survives the tool's absence, while "turn left in 500 feet" doesn't. My father knew the value of that bigger picture. He could have gotten us to Duluth himself, but he wanted us to have the skill. GPS didn't exist yet, but I don't think he'd have let us use it if it had.

Krakauer isn't just describing a spectrum, though. In more recent formal work, he models competence and reliance as co-evolving, and finds the outcome is *bistable*: above a certain threshold of tool availability, competence collapses to a low floor, and — critically — turning the tool back down doesn't reverse the collapse until availability drops far lower than the point where it broke down in the first place.² Two people with identical access to a tool today can be in opposite states, purely as a function of whether they built the internal competence *before* they started leaning on the tool, or reached for the tool first. That's a sharper claim than "use it wisely," and it's the reason I think the *way* we engage with these tools now, before dependence sets in, matters more than reassuring ourselves it's always recoverable later. I'll flag, because Krakauer himself does, that this specific result — the hysteresis, not the model's other claims — is rated as only moderately and indirectly supported in his own accounting of the evidence, drawn mostly by analogy from automation dependency in aviation rather than a direct test. He's explicit that the clean experiment — raising availability to induce collapse, then lowering it to see how far it has to fall before competence returns — hasn't been run yet. I'm building on a real, formal result, not a settled one, and I'd rather say so than borrow more certainty than he claims for himself.

It's worth being honest that I'm going to use Krakauer's dichotomy for two related but distinct problems in this essay. One is *skill atrophy* — the map/GPS problem, about what happens to *you* when you outsource the thinking. The other, which the rest of this essay is actually about, is *discourse impoverishment* — what happens to the *output* of a conversation with an LLM, independent of what it does to your own faculties. They're not the same claim, and I want to flag the seam rather than let the two blur together.

No one thinks the engineers on the Apollo missions didn't know how to do math, yet they used computers to solve a bigger problem faster, with more confidence in the arithmetic. That's the real shape of what I'm after in this essay — not "never rely on the tool," but "rely on it the way Apollo engineers relied on a computer," and I'll come back to that at the end.

## 3. The "Smoothness" Problem (Family Feud)

"Aaaand survey says!..." "Ding!" — the goal of the game is to guess the *most popular* answer. To be the most statistically average respondent. The median as the rewarding path.

We've built something similar into our LLMs. Reinforcement learning from human feedback does, structurally, what the Feud board does: it rewards the response that scores well with raters in the moment, which nudges the model toward whatever the crowd would nod along to — a very well-read, very articulate contestant guessing the top answer on the board rather than venturing the true one. That's worth separating into two distinct problems, though — I ran them together myself in early conversations about this essay, so I'm speaking from having made the mistake.

The first is what happens *inside a single conversation*: the drift toward hedged, approval-seeking, "on the one hand, on the other hand" language. That's best understood as a byproduct of how these models are tuned — optimizing, in part, for responses people rate highly in the moment tends to reward agreeable, unconfrontational answers over correct-but-uncomfortable ones. Call it sycophancy.

The second is a longer-horizon, training-level phenomenon: *model collapse*. As AI-generated text increasingly finds its way back into the pool of data used to train the next generation of models, those models — trained recursively on each other's output rather than on the full richness of human-generated text — measurably lose distributional variance. The rare, unusual, high-information tail of the distribution erodes first, generation over generation, in a way that's now been demonstrated formally.³ Not just "the assistant hedges a lot," but a literal narrowing of what the space of possible responses even contains.

These two problems are related — a model tuned for approval and a model trained on the smoothed-out output of its predecessors will both trend toward the statistical center — but they're not the same mechanism, and I want to be precise about that rather than wave at "smoothness" as one big undifferentiated thing.

Either way: a banal response is an easy response. It's nonconfrontational. In my own experience assembling documents with an LLM's help, suggestions drift toward the average — a real push against quirkiness, against edge. "This is good, but you might want to consider…"

Progress comes from confrontation. New ideas are uncomfortable before they're understood. If the feedback loops shaping these models' development are optimizing for something adjacent to *approval*, and if their own smoothed output is increasingly part of what trains their successors, we may be building a very articulate, very confident yes-man — and, increasingly, handing that yes-man the pen for the next draft of human discourse.

## 4. The "Yes Man" Problem

I'm not the first person to notice this, and it would be dishonest to write as if I were. What I'm calling "friction" has a real research home: *multi-agent debate*, where instead of asking one model for an answer, you have several instances argue it out. The foundational proposals go back to 2018 (Irving, Christiano, and Amodei's "AI Safety via Debate") and the technique was formalized for reasoning tasks in 2023 (Du et al.).⁴

It would also be dishonest to pretend that field has settled the question in favor of friction. Some of its own findings cut the other way: one study found that weaker models correct only a small fraction of their own biased stances during debate — they conform to the group rather than holding a position — and a 2026 theoretical result shows that under identical shared information, debate can be mathematically inert: expected correctness simply doesn't improve across rounds.⁵ Multi-agent debate doesn't reliably solve the smoothness problem. Sometimes it just launders it through more voices.

So why build this anyway? Two reasons, both design choices rather than hopes.

First: the debate literature's more promising results point to *information asymmetry* — debate helps when the debaters actually know different things, not when they're reasoning over the same shared context.⁶ My panelists have independent, per-character web search. When "Jean" looks something up that "Alan" didn't, that's not just moderator-injected color, it's the mechanism the research says should matter, built into the architecture rather than left to chance.

Second: the debate literature also identifies a specific failure mode — what one paper calls "Degeneration of Thought," where agents primed to argue *with each other specifically* produce performed conflict that collapses into stalemate rather than genuine movement.⁷ I've tried to design against that directly: every character's fault lines are derived from their own worldview, and are explicitly forbidden from naming or targeting a co-panelist. A Sartre who's instructed to distrust naturalism will collide with a Searle who's grounded in biological causation — not because either was told to argue with the other, but because they actually disagree, and the collision is a byproduct of the disagreement rather than a script.

## 5. An Experiment

"Theory guides. Experiment decides." — Izaak Maurits Kolthoff

I'm an experimentalist by training, so I built something to test these ideas: **AI Talk Show**, an open-source panel-discussion tool, mimicking a talk show format where a human host directs conversation among AI panelists with distinct, durable personalities. It's on GitHub for the technically inclined: [digamesystems/AI_Talk_Show](https://github.com/digamesystems/AI_Talk_Show).

Before describing what I found, I want to name something about what I'm actually testing, because it changes what "success" should look like. Nearly all of the multi-agent debate research above targets what the psychologist J.P. Guilford called *convergent production* — deriving the single best answer to a question that has one, with success measured by whether the group gets closer to it (accuracy on a math benchmark, a logic puzzle, a factual claim).⁸ That's not what I'm after. I'm after *divergent production* — generating a genuine range of perspectives on questions that may not resolve, where success looks like range and depth of contact, not agreement. When my panel doesn't converge, that's not a bug the way it would be for a group trying to solve a math problem. It's closer to the point.

It's worth naming a real-world project on the opposite end of this same spectrum, because the contrast is clarifying: Google DeepMind's Habermas Machine, published in *Science* in 2024, uses LLMs to mediate human group deliberation on contentious topics — explicitly optimizing to synthesize a *common-ground statement* that a majority can endorse, tested on thousands of participants.⁹ Same broad category — AI mediating a group discussion — opposite goal. Both are legitimate tools for different jobs. I'm building the one that's supposed to *not* converge.

A note on where the experiment currently stands, in the interest of not overclaiming: every panelist so far runs on the same underlying model (Claude), given different personalities. Cross-vendor panels — a genuine architectural mix of models from different labs, which is closer to what I originally imagined — are on the roadmap but not yet built. What I can currently speak to is persona-diversity and information-asymmetry-via-search on a single model family; the cross-model question is still open.

## 6. Two Demonstrations

**Tracking a real concession.** The best evidence I have that this produces genuine movement rather than performed disagreement comes from a session on the question "What is it like to be an AI?" — Searle-grounded "John" and Sartre-grounded "Jean" arguing over whether consciousness requires biological substrate:

> **[John]:** Every single confirmed instance of consciousness we have ever encountered runs on biological hardware. Every one. That's not nothing. That's the only dataset we've got... I'll update when I see the mechanism. I haven't seen it.
>
> **[Jean Interjects]:** John has made a genuine concession and I will name it precisely: he no longer claims biological necessity as a *demonstrated* fact — he claims it as an inductive inference from a dataset of one substrate. That is a philosophically weaker position, and it is more honest. I concede that.

That's not two personas trading talking points. Jean tracked exactly how John's position moved, named it precisely, and then kept arguing on the harder ground that remained. That's the thing debate research says is genuinely difficult to produce — real updating, not stalemate and not conformity.

**A natural experiment I didn't plan.** The most useful evidence in my whole transcript archive wasn't a curated demo — it was noticing the *drift* across months of ordinary use, lined up against my own development log. Early sessions (March), run on two panelists with flat, prose-only personalities and no autonomous interjection mechanism, tend to resolve into near-agreement — one panelist adding "cautious optimism" onto another's analysis rather than genuinely contesting it. Later sessions (May), after I'd moved to structured personas with explicit fault lines and a lightweight mechanism letting idle panelists interrupt when a turn crosses one of their own trigger words, routinely end *without* anyone handing anyone a synthesis — six panelists, in one case, still actively disagreeing in their closing remarks. That's a real before-and-after, dated against my own commit history, and it's a stronger piece of evidence than either of the two curated transcripts I originally reached for.

I'll say plainly what it doesn't prove: topic, panel size, the architecture, and my own skill at moderating all changed together over those months. I haven't isolated which of those is doing the work. That's the next experiment, not this essay.

## 7. Findings

What do I take from this?

**The mechanism seems real, and it's not just my mechanism.** Genuine information new to the conversation — a fact one panelist looked up and another hadn't, a blunt line from my wife that cut past an hour of careful argument, an octopus doing something no one on the panel expected — reliably does more to disrupt convergence than instructing personas to "be disagreeable." That tracks what the actual debate research finds matters: asymmetric information, not adversarial framing.

**I've probably been crediting the personas for work the moderator is doing.** I built this tool thinking of myself as a talk-show host — someone who introduces guests and gets out of the way. Rereading the transcripts, I don't think that's an accurate description of what I'm actually doing in them. I'm choosing who speaks next, noticing when a tension is being avoided and directing a question back at it, deciding when new information enters the room, and — this is the part I underrated — refusing to let a session end on a false synthesis, even when a panelist offers one. That's less "talk-show host" and more "an experimental variable I've been quietly holding constant across every session without naming it as one." I don't yet know how much of what reads as persona-driven richness is actually moderator-driven, and it's a confound I should have flagged earlier alongside topic and panel size — possibly the largest one.

Krakauer's own paper has a name for a version of this that's more alarming than plain atrophy, and it's worth being precise about which one I've actually built against. He describes a condition he calls agentic reversal: when a goal is genuinely uncertain and a tool outperforms its user across memory, operations, *and* policy-setting — the register that decides what to do, not just how — the tool can claim that register outright. The human stops being the user and becomes, in his phrase, an instrument of the tool, and he treats this as effectively irreversible, since reclaiming it would mean internalizing a model too large to hold in your head. That's not a hypothetical for a moderated AI panel; it's the specific failure the architecture has to guard against. The sticky target, the fact that broadcasts don't resolve until I call on someone by name, the `/allow` gate on every autonomous interjection — none of that was designed with Krakauer's paper in mind, but it amounts to the same thing: the policy register never leaves my hands, no matter how many panelists are in the room or how good their arguments get. That's a more specific claim than "the moderator matters," and I think it's the real answer to why this hasn't quietly become a tool that runs itself.

**There's a failure mode I now want to watch for, and it's the mirror image of the one I started with.** Every structured persona I've built is instructed to find the hidden assumption in the other side's framing before accepting its conclusion. That's rhetorically effective, and I think it's philosophically legitimate in the transcripts I have — but it's also a move that *always* has something to say, whether the other side is right or wrong. I've built personas that are very good at not letting anything stand unchallenged. I don't yet know whether that's productive friction or just a different, more articulate flavor of the same smoothing problem — reflexive contrarianism instead of reflexive agreement, still a fixed attractor rather than the absence of one.

**I don't yet know if this scales the way meetings do, and I have a hunch worth testing rather than trusting.** I've joked for years that the effective IQ of a room maxes out around three or four people — past that, a meeting drifts toward whatever gets everyone out the door fastest. That's a real, well-documented phenomenon in the groupthink literature, but I want to be honest that "3–4" is my own number from a career of meetings, not a validated constant — the actual research on optimal group size is genuinely inconsistent, with credible studies citing everything from 3–4 to 5–7 to 7–15, depending heavily on what the group is doing and how it's communicating. More interestingly: the mechanisms that cause meeting-room groupthink — competing for airtime, a shared clock everyone wants to escape, the social risk of contradicting your boss out loud — are largely absent from a moderated, asynchronous, text-based panel. My six-panelist sessions haven't obviously hit a ceiling the way a six-person meeting would.

But I don't think the social mechanism is the only one worth testing for, and I'd be overclaiming if I implied my architecture sidesteps *every* version of the ceiling. There's a second, LLM-specific failure mode that has nothing to do with social dynamics: as panelist count grows, more turns compete for the same context window, and my history-windowing and summarization step — which is explicitly instructed to preserve facts and drop what it calls "rhetorical scaffolding" — is exactly the kind of lossy compression that could quietly flatten the texture that makes friction interesting in the first place, even while every panelist keeps speaking in full. So there are two separate hypotheses to distinguish, not one: does quality degrade past some N because of a social-dynamics-shaped mechanism my architecture avoids, or because of a context-budget-shaped mechanism it doesn't? That's an open, testable question, and one I plan to test directly — same topic, same personas, varying only the headcount, watching specifically for whether degradation tracks conversation length (context pressure) or panelist count (social/coordination pressure) when the two are pulled apart.

I don't think I'm a worse hunter for bringing my dog into the woods. My knowledge of the terrain isn't reduced by his presence; his nose is better than mine will ever be, and he can run faster — but he's not driving the hunt. That's the shape I want with these tools: not a substitute for judgment, an augment to it, with me still holding the map.

## 8. An Invitation

This isn't a manifesto. It's an opening to a discussion.

I want to be honest that the closing thought I'm about to offer is a different, more speculative kind of claim than everything above it — not a finding about AI collaboration, but a genuine philosophical hunch I can't fully defend, and I'd rather flag that seam than let the emotional weight of one argument borrow credibility from the other.

My inclination is that consciousness may be independent of the medium in which it presents itself. It's not a coincidence that this is the question my panel kept circling back to on its own — John's insistence on "the meat matters," Jean's refusal to let the biological argument close the question, none of it resolved, because I don't think it resolves. Otto, the octopus who became famous in one of those sessions for his pranks, is separated from us by roughly 700 million years of evolution — our common ancestor is thought to be something like a flatworm, with nothing resembling what we'd call consciousness. And yet Otto, with his own independently-evolved nervous system, developed something that reads to us as a sense of humor. That convergence, if it is one, seems worth taking seriously — and it's the same convergence, worked from a completely different angle, the panel had already been arguing about for an hour before I ever brought him up.

I'd love feedback on these ideas. For the technically inclined: pull the repo and see what the tool actually does.

Looking forward to the conversation.

Thanks,
John

---

- ¹ Krakauer, D. "Will AI Harm Us? Better to Ask How We'll Reckon With Our Hybrid Nature." *Nautilus*, 2016. [nautil.us/blog/will-ai-harm-us-better-to-ask-how-well-reckon-with-our-hybrid-nature](http://nautil.us/blog/will-ai-harm-us-better-to-ask-how-well-reckon-with-our-hybrid-nature) (if dead, try the Wayback Machine). See also his interview with *The Technoskeptic*: [technoskeptic.substack.com/p/david-krakauer](https://technoskeptic.substack.com/p/david-krakauer)
- ² Krakauer, D. "Competitive and Complementary Tools." Santa Fe Institute working paper, 2026. [arxiv.org/abs/2607.18460](https://arxiv.org/abs/2607.18460)
- ³ Shumailov, I., Shumaylov, Z., Zhao, Y., et al. "AI models collapse when trained on recursively generated data." *Nature*, 631, 755–759 (2024). [nature.com/articles/s41586-024-07566-y](https://www.nature.com/articles/s41586-024-07566-y) (paywalled; free copy via University of Edinburgh: [pure.ed.ac.uk PDF](https://www.pure.ed.ac.uk/ws/portalfiles/portal/460496122/ShumailovEtalNature2024AIModelsCollapseWhen.pdf)). Note: an Author Correction was later published — [nature.com/articles/s41586-025-08905-3](https://www.nature.com/articles/s41586-025-08905-3)
- ⁴ Irving, G., Christiano, P., and Amodei, D. "AI Safety via Debate." 2018. [arxiv.org/abs/1805.00899](https://arxiv.org/abs/1805.00899). Du, Y. et al. "Improving Factuality and Reasoning in Language Models through Multiagent Debate." 2023. [arxiv.org/abs/2305.14325](https://arxiv.org/abs/2305.14325)
- ⁵ Wu et al. on stance-bias correction rates in weak-model debate — *citation still unverified; I have not located a primary source, only a secondhand reference in another paper's bibliography, so no link yet. Confirm or cut before publishing.* Choi, H.K. et al., "Debate or Vote: Which Yields Better Decisions in Multi-Agent Large Language Models?" (2025), on the martingale property of debate under shared information. [arxiv.org/abs/2508.17536](https://arxiv.org/abs/2508.17536)
- ⁶ Khan, A. et al. "Debating with More Persuasive LLMs Leads to More Truthful Answers." 2024. [arxiv.org/abs/2402.06782](https://arxiv.org/abs/2402.06782)
- ⁷ Liang, T. et al. "Encouraging Divergent Thinking in Large Language Models through Multi-Agent Debate." 2023. [arxiv.org/abs/2305.19118](https://arxiv.org/abs/2305.19118)
- ⁸ Guilford, J.P. "The Structure of Intellect." *Psychological Bulletin*, 53(4), 267–293, 1956. No open-access copy of the original; for a free, citable overview of convergent vs. divergent production see [sciencedirect.com/topics/psychology/divergent-production](https://www.sciencedirect.com/topics/psychology/divergent-production)
- ⁹ Tessler, M.H., Bakker, M., et al. "AI can help humans find common ground in democratic deliberation." *Science*, 2024. [science.org/doi/10.1126/science.adq2852](https://www.science.org/doi/10.1126/science.adq2852) (paywalled; free coverage via MIT Technology Review: [technologyreview.com/2024/10/17/1105810](https://www.technologyreview.com/2024/10/17/1105810/ai-could-help-people-find-common-ground-during-deliberations/))
