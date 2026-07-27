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

---

*When picking one of these up: check this file first, then pull the relevant section from the master draft or the noted conversation thread rather than reconstructing from memory.*
