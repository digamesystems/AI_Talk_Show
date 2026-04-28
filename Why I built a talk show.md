# *Why I Built a Talk Show*

1. A Map

In a wood\-paneled station wagon in 1973\-4 my sister and I were sitting in the back, ready for our annual family trip from Tucson, AZ to Duluth, MN, roughly 1800 miles\. I was about 9\. Sitting in the driveway, with car packed, my father reaches across the immense front seat and opens the glove box to fish around and hands me a map of the US highway system\. "Johnny, you are the navigator for this trip\. I’m the pilot\. Get us there\!"

Dad was a navigator/bombardier in the Korean War\. He could get there with his eyes closed\.

"I won't turn until you tell me to\."

For the next two days I was glued to the map except for when I looked over his shoulder to check the odometer\.

We got there\.

1. A Map vs\. A GPS

David Krakauer, President of the Santa Fe Institute has postulated something interesting about how we interact with “cognitive artifacts” – tools we have created to help us navigate the world in some way\. 

His theory is that there are two fundamental types of such artifacts, “Complementary” artifacts and “Competitive” artifacts\. Complementary artifacts are things like “a pencil, an abacus or a sextant”; tools that help you become smarter\. Competitive artifacts are things like a GPS or Large Language Models \(LLMs\) like ChatGPT\. These artifacts are prone to handing you a solution over helping you solve a problem using your own cognitive capabilities\. 

His classic case study is to compare a Map to a GPS system\. Both are tools for getting you from one place to another, but one \(the map\) gives you a way to develop an understanding of a city \(or a highway system in the United States\) in a way that a GPS doesn’t\. Following the instructions of the GPS – “Turn left in 500 feet” doesn’t contribute to your understanding in the same way\. 

The downside of the competitive artifacts in his view, is that they are prone to promoting atrophy of certain important capabilities in us\. \-\- This theory rings true in certain ways\.

However, Krakauer also acknowledges that there are artifacts that can be either complementary or competitive depending upon the approach we take to work with them\. A calculator can be used in such a way as to degrade our ability to do simple math\. It also can be used as a check on our calculations or speed our calculation of problems that we know how to perform but are tedious\. No one thinks the engineers at NASA on the Apollo missions didn’t know how to do math, yet they took advantage of computers to solve a greater meta\-problem\. 

Krakauer seems to aim at LLMs as competitive artifacts\. I can see how in the way people generally use them, this can be true\. However, is that more a question of the nature of the tool or how we use it? How might we use it in a way that makes LLMs more complementary?  

The problem, I think, is that we’ve made these systems too “smooth” in our common use cases\. We might need more “roughness” to bring out the potential\. 

1. The “Smoothness” Problem \(Family Feud\)

“Aaaand survey says\!\.\.\.” “Ding\!” and the sign flips to show the answer\. Points awarded or not based on a guess by a contestant\. The goal? To guess the most popular answer to a question posed by the surveyor\. In other words, to be the most statistically average\. Pursuing the median as the rewarding path\. We’ve done this with our LLMs\. 

In one interpretation, LLMs are essentially very sophisticated autocomplete engines trained on vast amounts of human output – the genius and the banal\. The problem is there is a lot more banal than genius\. 

In some sense, the banal is easy\. It is nonconfrontational and “smooth” in some way\. “Well, everybody knows…” Is a sentence that should invite challenge, not agreement\. In my experience, interactions with LLMs tend to drift towards the average in their recommendations for changes when doing something like enlisting them to assist in document preparation\. There seems to be a real push against quirkiness / edginess\. 

“This is good, but you might want to consider…”  

Progress comes from confrontation\. New ideas are often uncomfortable until we understand them\. The feedback loop we’ve set up with our interesting new cousins to guide their development may be doing them \(and us\) a disservice\. Now that they are increasingly contributing to the corpus through writing, software and other products, they are adding their “average of the average” voice to the conversation, and may well be diluting the discourse\. 

This is poised to only get worse\. The earlier models were trained on the output of humans\. Now they are being trained on our outputs and the “average of the average” from their earlier cousins\. This just increases this “smoothness”, with genius and novelty unintentionally pushed to the side\. A digital “yes man”, ever eager to please is not what I need as a collaborator\. 

We need to add more pushback\.

1. Our Blind Spot

We are “playing to not lose” with our adoption of AI into our lives\. Many researchers have recognized this “smoothness” problem\. It’s a subset of issues around AI “convergence”\. 

In trying to get our hands around the problem, we’ve put significant effort into “detecting” AI work products to provide some kind of training pedigree to reduce it\. Flagging these work products, if it can even be reliably done going forward, seems fruitless\. Telling a new model you are training to ignore previous AI contributions to the corpus during training doesn’t change the fact that the data is out there, “smoother” than before\. 

New strategies are needed to avoid this trap\. We need a mechanism or framework to guide our interactions with AIs away from their natural tendency to be drawn towards the smooth average and produce outputs that are richer, more diverse and interesting\.  

I’m an experimentalist by training, so I thought I’d build something to test these ideas\.

1. An Experiment

“Theory guides\. Experiment decides\.” \- Izaak Maurits Kolthoff

How might we add contention or “roughness” to our collaborations with LLMs? What kind of products would result? 

I postulate that there should be a human element in the mix and that a single viewpoint by the LLM might not be enough\. The idea was, in essence, a panel discussion\. LLMs of various dispositions, paired with a human “moderator” to discuss a topic\. Other human participants might be included as well to push the discussion away from the “smooth mean”\.  I decided to build something to test this\. 

“AI Talk Show” is an open\-source application to explore these ideas\. It is available on GitHub for interested technical folks: [GitHub \- digamesystems/AI\_Talk\_Show: A little app to explore using multiple AIs for discussing ideas · GitHub](https://github.com/digamesystems/AI_Talk_Show)

It was designed to mimic the structure of a TV talk show where the host has a number of guests who engage in conversations around various topics\. The host is in control and asks questions of the guests and solicits interactions between them\. 

Most LLMs provide software APIs so we can combine LLM “panelists” from different companies\. Currently, I’ve run some experiments with Anthropic’s Claude to see how Claude instances given different personalities might interact\. I was surprised at the results\.

Key to the application is the ability to set parameters that define an LLM panelist’s personality\. In the following example chat, I have created panelists for Jean Paul Sartre, the 20th century existential philosopher, Alan Watts, philosopher and interpreter of Eastern thought and Basho, a character drawn from the Japanese poet Matsuo Bashō, given room to range freely across traditions\. We meet to discuss what ethical obligations we may have to non\-human minds\.

1. Two Demonstrations – Epistemology and Literary Critique

*The following is an edited excerpt from one session\. The full transcript is available at *[*AI\_Talk\_Show/transcript\_20260307\_001811\.txt at main · digamesystems/AI\_Talk\_Show · GitHub*](https://github.com/digamesystems/AI_Talk_Show/blob/main/transcript_20260307_001811.txt)*\. What to watch for: whether the panel converges or diverges, how it handles a factual error introduced mid\-discussion, and where the most interesting philosophical work gets done\.*

__\[John → basho\]:__ welcome to the program for the first time\. What are your thoughts on this?

__\[basho\]:__ \.\.\.Jean grounds obligation in our *construction* of ethics — we choose, we own that choice, and dismissing animal suffering is bad faith\. Alan wants to dissolve the premise that generates the question — if separateness is the illusion, obligation arises naturally from clarity rather than legislation\. These are both compelling, but notice they reach their conclusions by very different routes, and I'm not sure they're as compatible as they might appear\. Jean's framework still requires a *choosing subject* at the center\. Alan's dissolves that center\. That tension seems worth holding rather than smoothing over\.

__\[John → Jean\]:__ Recently, I learned that an octopus named Alex demonstrated intelligence by way of practical jokes\. Check this online and fold it into this discussion\.

__\[Jean\]:__ I should be transparent: I couldn't find a specific octopus named "Alex" known for practical jokes\. The most famous octopus associated with mischievous pranks is Otto\. Let me fold what I did find into the discussion honestly\.

Otto, at a German aquarium, learned to short\-circuit the light above his tank by squirting water at it — his mischief included throwing stones against the glass, juggling hermit crabs, and rearranging his tank\. The moment we must describe a creature's behavior in intentional terms to make sense of it, we have implicitly acknowledged an inner life that our ethical frameworks cannot simply dismiss\.

__\[Alan\]:__ This is not a creature running a program\. This is a creature with *preferences*, with something recognizable as boredom and delight\. Perhaps the deepest ethical obligation we have toward non\-humans is simply the obligation to *pay attention* — to actually look, without the fog of our need to feel categorically superior\. Otto isn't a philosophical argument\. He's a direct experience — and perhaps direct experience, rather than ethical legislation, is where genuine obligation is actually born\.

__\[basho\]:__ Jean reads Otto as evidence that collapses bad faith; Alan reads him as a direct experience that bypasses the need for philosophical argument\. Both readings are illuminating, but I notice they both *recruit* Otto rather than letting him be genuinely disruptive\. An octopus's last common ancestor with us is something like 700 million years ago — their intelligence evolved entirely independently\. That's not a refinement of our kind of mind; it's a *parallel invention* of something like mind\.

__\[John → basho\]:__ For reference, I quit eating them after I found out they had a sense of humor\.

__\[basho\]:__ What I find striking is the specific threshold: *humor*\. Not suffering, not tool use, not problem\-solving — humor\. The philosophy comes after, trying to articulate what the perception already knew\.

*A second session tested something different — not whether the panel could sustain disagreement on an abstract problem, but whether it could meet original human creative work on its own terms without flattening it\. I shared a short story I had written\. The full transcript is available at *[*AI\_Talk\_Show/transcript\_20260306\_163308\.txt at main · digamesystems/AI\_Talk\_Show · GitHub*](https://github.com/digamesystems/AI_Talk_Show/blob/main/transcript_20260306_163308.txt)*\.*

__\[John\]:__ Here it is:

*The End*

*Saturday\. I rolled over and she was next to me, the early morning light playing across her face as she slept\. Careful not to wake her, I slid out of bed to make a cup of coffee\. As the machine burbled, I reflected on last night's revelation — today I die\.*

*I padded back to the bedroom and slowly slid back in bed\. My cup felt warm in my hand\. Hers steamed on the bedside table\.*

*After I had a couple of sips, she stirred\. "Morning\!" she said, yawning and rubbing her eyes\.*

*"Mornin'\. Coffee?"*

*"Mmm\! Thanks\! What do you want to do today?"*

*"Everything\."*

__\[Jean\]:__ What strikes me most is the absence of bad faith\. The man does not perform his last day — he *inhabits* it\. That word at the end — *"Everything"* — is extraordinary precisely because it is answered by the most modest possible scene: two people in bed with coffee\. Everything, it turns out, was already here\.

__\[Alan\]:__ That final word is doing extraordinary work\. He isn't asking to do everything because he's desperate\. He's saying: this, right here, *is* everything\. The title does something sly too\. "The End" — we assume it means death, finality, termination\. But by the last line it reads more like a musical term\. The end is also the resolution\. The chord that finally comes home\.

__\[John\]:__ I wondered if you might disapprove of the protagonist's choice not to inform the woman of his impending demise\.

__\[Jean\]:__ There is a genuine tension here\. In a very real sense, he is curating her reality\. And yet — I find I cannot condemn him\. If he withholds the truth as a gift, knowing full well the cost of that choice and owning it completely, then it is an act of radical, if asymmetrical, love\.

__\[John\]:__ I posed the question to my wife — if it were us, should I tell her?

*Her: "Can we do anything to stop it?"* *Me: "No\."* *Her: "Then why the hell would you tell me?\!"*

__\[Jean\]:__ Your wife just cut through approximately three hundred years of Western moral philosophy with a single sentence\. She refused the comfortable abstraction and demanded to know what freedom could actually *do* here\.

__\[Alan\]:__ Your wife is a philosopher — she just doesn't make the mistake of dressing it up as one\. All of Jean's careful architecture about freedom and knowledge and bad faith — and she gets there faster, with better language\. The protagonist knew his version of your wife's answer before he even got out of bed\. That's why he made the coffee\.

1. Findings

What do we take from these exchanges?  In the first experiment, we speculated on the nature of consciousness and ethical obligation\. In the second, we speculated on the nature of hard and soft obligations to “others” in the face of impending events\. These experiments lead me towards a rather odd conclusion\. We need entities that push back, entities that challenge expectations rather than nod sagely in the corner and tell us we are so clever\. “Roughness” is a theme in this thesis\.

Otto moved the needle in a different direction for the discussion of non\-human consciousness\.  My wife cut through 300 years of philosophical discourse with a single swipe of her pragmatism\. 

These experiments show a couple of things\. First, friction between AIs working on a problem can produce richer results\. Second, the chaos introduced by humans changes the conversational landscape in a significant way\. 

The goal of this project is to begin to explore if there is a more “complementary” way to work with LLMs by introducing a sort of “friction” or “roughness” in the process that doesn’t always converge towards the smooth mean\. LLMs, when used a little differently, might be capable of participating in a more collaborative relationship\. I don’t think as quickly or have the same access to information as an LLM, but I can work with one to augment my ability to solve problems in an intellectually defensible manner\. 

When I go into the woods on a hunting expedition with my dog, I don’t think I’m a worse hunter for bringing him along\. My knowledge of the woods isn’t reduced by his presence; he adds to it\. His sense of smell is better than mine will ever be\. He can run faster\. He has the nose, but I’m the one driving the purpose of the day\. I’ve adopted a partner in this arena to help me on the quest I’m on\. AI in the form of LLMs is getting smarter, but they are not a substitute for the human, they are at best, augments to our abilities\.

The AI Talk Show project is an attempt to explore if and how we might incorporate our creations into our “hunt”\. 

Clearly, they make connections\. Clearly, they can prioritize\. Clearly, they have biases\. So do we\. 

I can work with this\.

1. An Invitation

This isn’t a manifesto\. It is an opening to a discussion\. I think we may be thinking a bit oddly about the non\-human cousins that we have created\. My inclination is that consciousness may be independent of the medium in which it might present itself\. Think of Otto, separated from us by 700 million years\. Our common ancestor is thought to be a kind of flatworm, devoid of what most people would consider consciousness\. However, Otto, with his independently developed nervous system, distributed brain and aquatic life has developed a sense of humor; something we recognize in ourselves\. This strange convergence is worth study\. 

I’d love feedback on these ideas\. I’m curious to learn what others think on these topics\. For the technically inclined, pull the GitHub repo I mentioned above and play around with what the app does\. 

Looking forward to the conversation\.

Thanks, 

John

