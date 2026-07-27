# Why I Built a Talk Show

*First in a short series. Later pieces will take up the formal model behind this, the research literature on AI debate, and a few open questions I haven't tested yet.*

## A Map

In a wood-paneled station wagon in 1973–4, my sister and I were sitting in the back, ready for our annual family trip from Tucson, AZ to Duluth, MN — roughly 1800 miles. I was about 9. Car packed, my father reaches across the front seat and hands me a map of the US highway system. "Johnny, you and Julie are the navigators for this trip. I'm the pilot. Get us there!"

Dad was a navigator/bombardier in the Korean War. He could have gotten us there with his eyes closed.

"I won't turn until you tell me to," he said. He never told us when we'd know we'd arrived — that part was always going to be ours to figure out.

We got there.

## Complementary and Competitive

David Krakauer, President of the Santa Fe Institute, has a useful way of sorting the tools we build to help us think.¹ Some — a pencil, an abacus, a map — leave you smarter once you set them down. Call these complementary. Others hand you the answer directly, and the moment you set them down, you're no better off than before you picked them up. Call these competitive. His case study is the map versus the GPS: both get you where you're going, but only one leaves behind an internal model of the terrain that survives the tool's absence. My father could have just told us the route. He handed us the map instead, because he wanted us to have the skill, not just the outcome.

Large language models get sorted into the competitive bucket almost by reflex these days. I don't think that's wrong, exactly. I think it's incomplete. The interesting question isn't whether LLMs are competitive tools. It's whether we can design ways of using them that are complementary — a design question as much as a habit of mind.

## The Best Possible Contestant

Here's where I think Krakauer's frame extends somewhere he didn't take it.

His concern is mostly about what a tool does to your retained skill — whether the thing you outsourced still lives in your head once the tool is gone. I've become interested in a parallel version of the same problem, at the level of a single conversation rather than a single skill: what a tool does to a conversation's honesty while you're still having it.

Family Feud rewards the answer most people would give, not necessarily the true one. "Survey says" isn't asking what's correct — it's asking what the crowd already thinks. Reinforcement learning from human feedback has the same incentive built in: a model gets trained on which responses people rate well in the moment, and agreeable, unconfrontational answers tend to score better than correct-but-uncomfortable ones. The result, at its most articulate, is something like the best possible Family Feud contestant — a very well-read guesser of the top answer on the board, not a venturer of the true one. (There's a related, longer-horizon version of this problem at the level of training data itself, where models increasingly learn from other models' output rather than the full range of human writing — that's a different mechanism, and a piece for another day.)

For a tool you're using to think *with*, rather than just to retrieve an answer *from*, that tendency is the whole ballgame. A collaborator built to please you isn't a complementary tool. It's a competitive one wearing a friendlier voice — because the thing it's quietly doing for you, instead of the arithmetic, is the disagreeing.

## Who Holds the Talking Stick

So I built something to push against that: a moderated panel where a human host directs conversation between several AI "panelists," each holding a distinct, durable position, arguing a topic out loud.

This isn't a new idea — researchers have been testing whether AI instances arguing with each other beats asking one model for an answer since at least 2018.² What I think matters more than the debate itself is who's actually running it. Every panelist in my system can argue sharply, concede a point, interrupt when a topic crosses one of their own fault lines. None of them chooses the next question. None of them decides when a session has actually resolved something, versus just produced a good line. I hold the talking stick. The panel argues; I decide where the argument goes and when — if ever — it's actually settled.

That division of labor is the whole design, more than any particular debate technique. The AIs supply range and pressure. The human supplies judgment about what the range and pressure actually add up to.

## Watching a Position Move

Here's what that produces, at its best. From a session on whether consciousness requires biological substrate — a Searle-grounded panelist ("John") and a Sartre-grounded one ("Jean") arguing it out:

> **John:** Every single confirmed instance of consciousness we have ever encountered runs on biological hardware. Every one. That's not nothing. That's the only dataset we've got... I'll update when I see the mechanism. I haven't seen it.
>
> **Jean:** John has made a genuine concession and I will name it precisely: he no longer claims biological necessity as a *demonstrated* fact — he claims it as an inductive inference from a dataset of one substrate. That is a philosophically weaker position, and it is more honest. I concede that.

That's not two chatbots trading talking points. A position actually narrowed under pressure, and the other side named exactly how, rather than just declaring victory. I've read a lot of AI-generated dialogue that performs disagreement. This is one of the few times I've watched it actually happen.

## What I Was Building, Without Meaning To

I built this thinking of myself as a talk-show host — introduce the guests, get out of the way. Going back through months of transcripts, that's not really what I was doing. I was choosing who spoke next. Noticing when a tension was being dodged and pointing back at it. Deciding when to drop in a piece of information nobody on the panel had. Refusing to let a session end on a synthesis that was really just fatigue dressed up as agreement.

None of that is difficult in the way debugging code is difficult. But it isn't nothing, either. The sessions that have stayed with me longest weren't the ones with a clean answer. They were the ones where nobody in the room was going to settle it for me, and I had to decide, on my own judgment, which position actually held up. Nobody tells me when we've arrived. That's still mine to figure out, same as it was in the back seat in 1973. If Krakauer's right that a real tool leaves you more capable once you set it down, that's the part of this project I'd point to first — not the transcripts, the moderating.

I want to be honest about the limit of all this, though, because it's a real one. Nothing about this architecture can stop a moderator who isn't actually interested in being wrong. No leash-pull mechanism, no refusal of a false synthesis, reaches someone who's already decided what they think and is just enjoying the show. What the friction can do is make that harder to hide from yourself — a smooth, agreeable conversation lets you coast without noticing; an unresolved one, with a position that just moved in front of you, is harder to wave off without at least seeing yourself do it. That's not nothing. It's also not a guarantee.

## The Dog

I don't think I'm a worse hunter for bringing my dog into the woods. My knowledge of the terrain isn't reduced by his presence; his nose is better than mine will ever be, and he can run faster — but he's not driving the hunt. That's the shape I want with these tools: not a substitute for judgment, an augment to it, with me still holding the map.

This isn't a manifesto. It's an opening to a discussion. For the technically inclined, the project is on GitHub: [digamesystems/AI_Talk_Show](https://github.com/digamesystems/AI_Talk_Show).

Thanks,
John

---

- ¹ Krakauer, D. "Will AI Harm Us? Better to Ask How We'll Reckon With Our Hybrid Nature." *Nautilus*, 2016. [nautil.us/blog/will-ai-harm-us-better-to-ask-how-well-reckon-with-our-hybrid-nature](http://nautil.us/blog/will-ai-harm-us-better-to-ask-how-well-reckon-with-our-hybrid-nature) (if dead, try the Wayback Machine).
- ² Irving, G., Christiano, P., and Amodei, D. "AI Safety via Debate." 2018. [arxiv.org/abs/1805.00899](https://arxiv.org/abs/1805.00899)
