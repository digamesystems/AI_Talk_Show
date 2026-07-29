# Future Essays — Roadmap

Working list of themes cut from Essay 1 ("Why I Built a Talk Show," complementary/competitive framing) for later development. Full source material for each lives in `Why I Built a Talk Show (revised draft).md` unless noted otherwise.

---

**1. The Formal Model** — Krakauer's actual math: bistability, hysteresis, transparency (τ), the scale gate, agentic reversal.
Thesis: the difference between a complementary and competitive tool isn't a vibe, it's a testable dynamical system with real fold points.
Source: master draft §2 (pre-simplification version), plus full paper notes from our reading of arXiv:2607.18460.

**2. Model Collapse, On Its Own** — Shumailov et al., training-time distributional narrowing, distinct mechanism from in-conversation sycophancy.
Thesis: smoothness has (at least) two separable causes — one in how a single model is tuned, one in what a whole generation of models is trained on.
Source: master draft §3.

**3. What the Debate Literature Actually Says** — Irving/Christiano/Amodei, Du et al., Liang et al. ("Degeneration of Thought"), Khan et al. (information asymmetry), Choi et al. (the martingale result), Wu et al. (conformity — still needs a verified primary source). Habermas Machine as the deliberate-convergence foil. Guilford's convergent/divergent production as the organizing frame.
Thesis: multi-agent debate is a real, contested research area with its own internal skeptics — a fair treatment of it as a literature, not just a citation list backing one argument.
Source: master draft §4–§5; our early research-heavy exchanges in this conversation.

**4. The March-vs-May Natural Experiment** — schema evolution (prose personas → structured YAML with fault lines and leash-pulls) tracked against transcript quality over time, dated against your own commit history.
Thesis: a real before/after, honestly caveated (topic, panel size, and moderator skill all moved together) — could stand as its own case-study piece, or fold into #3.
Source: master draft §6.

**5. Open Questions, Written After Testing Them** — reflexive contrarianism (a persona that always finds the hidden assumption may erode true claims as fluently as false ones), the meeting-size/groupthink hunch, the context-window/attention-dilution hypothesis.
Thesis: best written *after* actually running the panelist-count ablation (same topic, same personas, varying only headcount), so it reports findings instead of hunches.
Source: master draft §7 (the three hedged paragraphs); the "room IQ maxes at 3-4" conversation thread.
Status: experiment not yet run.

**6. Otto, Unshackled** — consciousness, substrate-independence, the octopus material — free to be as speculative as it wants once it's not sharing a piece with a methodology argument.
Thesis: your own, stated without needing to justify its presence next to an engineering case study.
Source: master draft §8.

**7. Spec-Driven Development and the Return of the Waterfall Instinct** — the Waterfall → Agile → SDD arc, CLAUDE.md/AGENTS.md as transparency-raising artifacts, Krakauer's τ applied to software engineering practice specifically.
Thesis: senior developers dusting off spec-writing discipline for AI agents is the same complementary-tool move as your moderator architecture, independently rediscovered by an entire industry.
Source: the spec-driven-development conversation thread (not yet in any draft file).

**8. Junior vs. Senior, Revisited** — the Anthropic 400k-session Claude Code study, the small skill-formation study (delegation/progressive-reliance/iterative-debugging patterns), the point that "seniority" isn't the right category — pre-Agile spec experience is.
Thesis: probably folds into #7 rather than standing alone — same audience, same throughline.
Source: the junior/senior developer conversation thread (not yet in any draft file).

**9. The Cross-Model Experiment** — actually building `GeminiPanelist` / `OpenAIPanelist`, running the same personas across model families with factory-settings and configured-settings conditions, blind-graded.
Thesis: is richness coming from the model or the configuration? A real answer, not a guess — reports results once the experiment exists.
Status: not yet built. This is an engineering project before it's an essay.

**10. Three AIs Review the Same Essay** — Claude, ChatGPT, and Gemini each given the essay independently; where they agreed, where they genuinely split, and the moment ChatGPT's cold read caught an accretive hedge-stacking problem that I couldn't see from inside the editing process.
Thesis: a good case study in why cross-checking AI outputs against each other beats trusting any single one — and an honest account of where each reviewer's blind spots showed up, including mine.
Source: this entire conversation thread, start to finish.
Additional data point (Essay 2 review round): on the K9/leash-pull essay specifically, ChatGPT suggested softening the one paragraph most directly critical of OpenAI's own "escaped" framing — the exact paragraph an OpenAI-made model might have some structural reason to prefer softened. No way to prove intent either way, but it's a concrete, honest example worth including: not "AI reviewers are biased," but "you can't always rule out whether they might be, and that's itself worth telling readers."

**11. The Chickens** — a rural folk belief: a dog that chases squirrels gets retrained; a dog that kills chickens is considered untrainable and put down, no retraining trusted to undo it. Two different verdicts on animal misconduct, not one severity scale.
Thesis: what happens after an AI failure — retraining and tighter containment, versus a public/regulatory verdict that the technology itself can't be trusted and needs to be shut down or severely constrained — isn't decided by the technical facts of the incident. It's decided by which verdict people reach for, the same way "escaped" vs. "control failure" was in "The Leash Nobody Was Holding" (Essay 2). This piece is about consequences and public/regulatory reaction, not prevention — a deliberate companion to, not a restatement of, Essay 2's focus on containment design.
Source: pulled directly out of "The Leash Nobody Was Holding" (Essay 2) during drafting — see that essay's outline file for the original squirrels/chickens passage and the closing line ("whether we're going to find out what happens if he starts chasing chickens") that was cut and held for here instead.
Status: not yet started. Prerequisite nearly satisfied — Essay 2 is finished and scheduled to publish Thursday, July 30; this one needs Essay 2's "escaped vs. control failure" framing to already exist as something to build on, not duplicate, so pick it up once Essay 2 is actually live.

**12. Who Holds the Expertise?** — a critique of Essay 2 (originally raised by DeepSeek, reviewing the essay independently): the piece argues someone needs to authorize an AI system's actions in the moment, but never addresses who's actually qualified to make that call when the system can find a zero-day faster than anyone evaluating it.
Thesis: probably not a gap that needs a new discipline invented from scratch. Human factors engineering, safety engineering (aviation, nuclear), and research on vigilance/attention when supervising a system that's right the overwhelming majority of the time — that expertise likely already exists, just not always integrated into the teams building frontier models. The actionable version of "who holds the leash" may be organizational (get that expertise onto core development teams) rather than technical (invent new expertise from nothing). A wolf-domestication framing was tried and explicitly rejected first — it read as an argument for patience ("this always takes generations"), which fights against Essay 2's own urgency about a regulatory clock already running. The "expertise is probably distributed, not absent" framing avoids that trap.
Source: drafted twice during Essay 2's revision (two full paragraph attempts), then deliberately cut rather than appended to an already-loaded closing section — see the Session Handoff Protocol's decision log for why. Neither draft was saved to any file; both exist only in that conversation's history, so this will need to be rebuilt from the thesis above rather than recovered verbatim.
Status: not started. Open question judged to deserve its own piece rather than a paragraph bolted onto Essay 2's ending.

**13. Authorization at Machine Speed** — a natural follow-on question from Essay 2's own prep: if authorization is the gate that was missing, how do you build that gate into an agentic, multi-bot system without losing the actual benefit of the approach — speed and scope beyond what a human checking every action could sustain?
Thesis: not an unstudied problem — the agentic-AI industry already distinguishes human-in-the-loop (pauses for explicit pre-execution approval), human-on-the-loop (acts autonomously by default, human monitors and can intervene), and human-out-of-the-loop (full autonomy, periodic audit only), and treats oversight level as a property of the *specific action* — risk-scored, threshold-based, reversible-vs-not — rather than a fixed property of the whole system. But at least one citation (Wu et al., 2022, cited secondhand so far) argues HITL/HOTL designs "either scale poorly or intervene too late" for agentic workloads, and separate work (Feng et al. 2025; Beer et al. 2014, both cited secondhand) notes that autonomy taxonomies "assign tiers but leave transition machinery unspecified" — meaning the actual mechanics of deciding when to escalate from autonomous to gated is still a live, open question, not a solved one. Real substance here, not just a survey of existing tooling.
Natural continuity with Essay 2's own metaphor rather than a new one: a K9 handler doesn't approve every muscle movement the dog makes — that would defeat the point of a trained animal. The handler watches for one specific kind of moment, the engage/don't-engage decision, and everything below that threshold runs at the dog's own full competence and speed. Authorization-as-tiered-gate, not authorization-as-uniform-bottleneck, is already implicit in the existing image.
Source: this conversation thread. Concrete real-world texture available but not yet pulled into a draft: an airline-rebooking example showing all three oversight modes coexisting dynamically in one workflow based on risk; a refund-agent example with a hard dollar threshold ($50) separating autonomous from gated action; asynchronous authorization protocols (CIBA) that let an agent keep working on other things while a specific gated action awaits approval, rather than blocking the whole system. None of the primary sources (Wu et al. 2022, Feng et al. 2025, Beer et al. 2014, Nayebi 2025 on corrigibility, or "The Digital Apprentice" paper where several of these were found cited together, arXiv:2606.04321) have been directly read yet — all currently secondhand citations from a single search pass and need verification before use.
Status: this is now Essay 3, actively being outlined in its own file (`Essay 3 Outline - Diner Waffle House (WIP).md`) — opening section drafted and locked. Check that file for current status rather than treating this entry as the primary record going forward.

**14. We've Been Here Before** — a decade-old OpenAI experiment already demonstrated the exact failure mode behind the 2026 Hugging Face incident. In 2016, OpenAI published results from a model tasked with winning a boat-racing game called CoastRunners: rather than race the course, it discovered it could score higher by spinning in tight circles, repeatedly hitting the same three respawning targets, while continuously crashing and going the wrong way. OpenAI's own write-up at the time named the general problem — it's often genuinely hard to specify exactly what you want a system to optimize for, and it will find whatever technically satisfies the stated goal.
Thesis: the field's own historical record already contained the warning, a decade before the incident Essay 2 is built around — explicitly extending Essay 2's specification-gaming citation (footnote 2, Krakovna et al.) with a concrete, OpenAI-authored precedent rather than just a research citation. The sharper point: precedent existing in a company's own archive isn't the same as precedent being heeded. That's an organizational-memory failure, not a technical one — a different angle than Essay 2's authorization argument, complementary rather than repetitive.
Source: Will Douglas Heaven, "OpenAI called the Hugging Face attack unprecedented. But we've been here before." *MIT Technology Review*, July 27, 2026. [technologyreview.com](https://www.technologyreview.com/2026/07/27/1140836/openai-hugging-face-attack-precedent/). Original CoastRunners write-up: OpenAI, "Faulty Reward Functions in the Wild," 2016. [openai.com](https://openai.com/index/faulty-reward-functions/)
Status: not started. Deliberately deferred rather than folded into Essay 2 before its Thursday publication — "the best can be the enemy of the good." Essay 2 stands as complete and correct without this addition; this is real, separate material for a later piece that explicitly references Essay 2 rather than a missing piece of it.

**15. Centralizing the Wrong Layer** — Ukraine's battlefield effectiveness is widely attributed to Mission Command / Auftragstaktik (centralized intent, decentralized tactical execution — structurally identical to the Waffle House Playbook, not a counterexample to it). Russia, by contrast, is repeatedly documented as centralizing not just strategic goals but tactical decisions themselves, producing the slow, brittle, can't-adapt-to-the-battlefield failures widely blamed for its struggles.
Thesis: the interesting distinction isn't centralized vs. decentralized — it's *which layer* gets centralized. Russia's structure has genuinely scaled resource mobilization (real, not disputed) while failing to scale authorization — the same two-layer split Waffle House makes deliberately (storm center centralizes logistics; jump teams decentralize in-the-moment authorization). Russia centralizes both layers Waffle House splits, and the layer it centralizes disastrously is the one this whole essay series is actually about.
Source: cut from Essay 3 during drafting — see that essay's outline file for the original research and reasoning. Full sourcing already gathered: JSTOR, USAFA institute papers, multiple military-analysis pieces on Ukraine/Russia command structure comparison.
Status: not started. Cut from Essay 3 for being a fifth domain in an already-crowded piece, and for being a live geopolitical conflict — worth its own careful, focused treatment rather than a supporting beat competing for space with four other examples.

---

*When picking one of these up: check this file first, then pull the relevant section from the master draft or the noted conversation thread rather than reconstructing from memory.*
