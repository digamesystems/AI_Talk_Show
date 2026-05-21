# AI Talk Show
## Project Session Summary
*Updated 2026-03-09 — for continuity across Claude sessions*

---

## Project Vision

A console-based (first) then web-based moderated panel discussion app where a human moderator directs conversation between multiple AI panelists (and optionally human panelists). Inspired by a talk show format — the moderator holds the talking stick and directs who speaks. Each panelist hears the full conversation history regardless of who a prompt was directed at.

Longer term vision includes: Slack integration as a natural multi-user text interface, text-to-speech/speech-to-text for a real talk show feel, YouTube content production, and potentially a multi-user hosted platform.

---

## Current Status

A working Python console spike is complete and road-tested. Core conversation loop is functional with:

- Multiple Claude panelists with different role-based personas (Sartre, Watts, Shaman, Skeptic, Optimist, Default)
- Web search enabled per panelist (Anthropic server-side tool)
- Sticky target, pending state for /all broadcasts
- Clean annotated transcripts saved to file
- Multi-line / paste-safe input via `.` send sentinel
- TTS pipeline in TTS/ subdirectory (ElevenLabs)

---

## File Structure

```
AI_Talk_Show/
├── roles/
│   ├── default.yaml
│   ├── skeptic.yaml
│   ├── optimist.yaml
│   ├── sartre.yaml
│   ├── watts.yaml
│   └── shaman.yaml          ← NEW: added this session
├── TTS/
│   ├── render_transcript.py
│   ├── tts_voices.yaml
│   └── list_voices.py
├── models.py
├── panelist.py
├── moderator.py
├── conversation.py
├── session.py
├── roles.py
└── main.py
```

---

## New This Session

### shaman.yaml — New Role

Designed collaboratively this session. Fills a gap in the existing role set: not a framework-advocate (like Sartre or Watts), not an adversarial skeptic, but a careful interlocutor whose primary move is illumination. Road-tested in two transcripts. Deployed as panelist named "Basho."

Key characteristics:
- Identifies the single most load-bearing unexamined assumption
- Holds multiple framings simultaneously without forcing resolution
- Epistemic honesty as substantive contribution, not hedge
- Goes deep on one thing rather than wide on many
- Finds the question underneath the question
- Integrates web search selectively: one reframing fact beats three supporting ones

Voice feels genuine per moderator assessment. Verbosity improved with updated yaml vs first draft.

### Road Test Transcripts

Two full transcripts generated and reviewed this session:

- **Sartre + Watts discussing "The End"** — a short story written in a sports bar. Strong performance. Sartre/Watts dynamic generative; moderator's wife's nine-word response was the sharpest moment in the transcript.
- **Sartre + Shaman (Basho) + Watts discussing ethical obligations to non-humans.** Otto the octopus arrived as anecdote and ended up doing serious philosophical work. Shaman performed well; verbosity present but improved in second run.

---

## Staged Features & Enhancements

The following have been designed and agreed upon but not yet implemented:

### 1. shaman.yaml Refinements
- Add "single most load-bearing" — sharpen focus to one assumption
- Add web search guidance: one reframing fact beats three supporting ones
- Add "go deep on one thing rather than wide on many"

*Status: Ready to implement. Low effort, high value.*

### 2. Guest Management Commands

- `/add_guest Name role` — introduce and onboard new panelist mid-session
- `/drop_guest Name` — thank and dismiss panelist gracefully

**Under the hood for `/add_guest`:**
- Moderator composes introduction (recorded as Statement)
- System generates onboarding summary of conversation so far (Option B — summary + current window)
- New panelist receives summary + current window going forward
- After onboarding, new panelist is on equal footing with existing panelists

**Under the hood for `/drop_guest`:**
- Moderator prompted for farewell words (recorded as Statement)
- Panelist removed from `conversation.panelists` and `pending_respondents`
- Handle remains in history — other panelists can still reference their contributions
- Guard: warn if dropping panelist mid-pending

### 3. Conversation Summarization

Required for guest onboarding and long-session context management. Same mechanism serves both.

- New `summarize_history()` function — API call generating narrative summary of out-of-window turns
- Triggered automatically at window threshold OR manually by moderator
- Summary prepended to new panelist history as briefing message
- `Conversation` class needs `onboarding_summary` field on panelist records

### 4. Gemini Panelist

- `GeminiPanelist(Panelist)` subclass
- Own `format_history()` — Gemini uses `model` not `assistant`, system instruction passed separately
- Own API key handling
- Enables true multi-provider panels

---

## Full Roadmap (Prioritized)

1. shaman.yaml refinements — concision and web search guidance
2. Guest management — `/add_guest` and `/drop_guest` with summarizer
3. Conversation summarization — auto-trigger at window threshold
4. Gemini panelist — `GeminiPanelist` subclass
5. Persistence — save/load conversations to SQLite, resume later
6. Slack integration — natural multi-user text interface (see below)
7. Web UI — Flask frontend, user login, conversation history browser
8. Speech layer — TTS for AI voices (ElevenLabs), STT for human panelists

---

## Slack Integration — Design Notes

Identified this session as a more natural next interface than TTS/STT. Slack is already where distributed conversations happen; no new interaction patterns required.

### Natural Mapping
- Slack channel = panel discussion session
- Channel messages = turns in conversation
- Bot layer = routes messages to AI panelists, posts responses
- Moderator = Slack user typing naturally
- AI panelists = distinct bot personas with own names and avatars
- Human panelists = registered Slack users whose messages become Turns

### Key Design Decisions
- **Open floor model** preferred over strict turn-taking — moderator shapes flow, doesn't gate every word
- AI panelists respond when @mentioned by moderator OR when addressed by name in channel
- Moderator tools become light interventions: `/all`, `@panelist`, `/add_guest`, `/drop_guest`, `/hold`
- `SYSTEM_PROMPT_TEMPLATE` needs a Slack variant — relaxed turn-taking norms, panelists may address each other
- Human panelists registered via `/add_guest @username human` — their Slack messages become Turn objects

### What Stays Unchanged

The core architecture is provider-agnostic. All of `models.py`, `conversation.py`, `panelist.py`, `roles/`, `moderator.py` survive unchanged. Slack is a new `session.py` sibling — `slack_session.py` — not a replacement.

### Web App Implications
- State management: standard web app pattern — load Conversation from DB, do work, save back
- `ClaudePanelist` becomes a data model reconstructed from DB per request
- Async required for API calls — streaming preferred
- Concurrent users need session locking strategy
- Console spike is proof of concept; web version reuses concepts and data structures, not session loop

---

## Architecture — What the Console Spike Has Validated

### Proven and Portable
- `Turn`, `Prompt`, `Statement`, `Conversation` data structures — translate cleanly to DB tables
- `Panelist` abstraction with per-subclass `format_history()` — correct design, survives web transition
- `name` vs `handle` separation — proved its value with two Claude panelists
- Role YAML system — portable, extensible, already six roles
- `Statement` vs `Prompt` distinction — clean and useful
- Moderator command grammar — well-tested
- Web search integration — working, adds real value

### Known Gaps
- Guest add/drop not yet implemented — design is clear
- Conversation summarization not yet implemented
- Gemini panelist not yet implemented
- `Conversation` needs membership-over-time model for changing casts

---

## Observations from Road Testing

- Historical figure roles (Sartre, Watts) hold up under pressure including live political material
- Shaman role has genuine voice — neither framework-advocate nor pure skeptic
- Verbosity is the main tuning problem — web search returning rich material triggers longer responses
- The moderator's human contributions consistently outperform the philosophical scaffolding
- Three-panelist sessions work well; moderator sequencing shapes narrative arc significantly
- **Family Feud contamination observation** (AI training on AI output) resonated strongly on LinkedIn — 300+ impressions in one hour
- The human panelist becomes more valuable, not less, as AI corpora contaminate each other

---

## Outreach — Paul Saffo

LinkedIn message drafted and sent this session to Paul Saffo (Silicon Valley forecaster, Stanford, Singularity University, Atlantic Council). Lead with the Family Feud problem and Sartre/Watts transcript. Asked for reaction or pointer to who should be paying attention.

Project is public: https://github.com/digamesystems/AI_Talk_Show

---

## Notes for Next Session

Good next steps in rough priority order:

1. Apply shaman.yaml refinements — five minute task
2. Implement `summarize_history()` — the lynchpin for guest management and context windowing
3. Implement `/add_guest` and `/drop_guest` commands
4. Run a session with guest add/drop to validate the design
5. Explore Slack Bolt SDK for interface prototype
6. Follow up on Paul Saffo outreach

---

*Claude Code has memory of this project at `~/.claude/projects/.../memory/MEMORY.md` — no need to paste this document when working in Claude Code. Just open the project and say "let's continue".*
