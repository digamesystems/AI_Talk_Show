# AI Panel Discussion — Project Summary
*Updated 2026-05-20 — for continuity across Claude sessions*

---

## Project Vision

A console-based (first) then web-based moderated panel discussion app where a human moderator directs conversation between multiple AI panelists (and optionally human panelists). Inspired by a talk show format — the moderator holds the talking stick and directs who speaks. Each panelist hears the full conversation history regardless of who a turn was directed at.

Longer term vision includes: Slack integration as a natural multi-user interface, text-to-speech/speech-to-text for a real talk show feel, YouTube content production, and potentially a multi-user hosted platform.

---

## Current Status

A working Python console spike is complete and road-tested. Core conversation loop is functional with:
- Multiple Claude panelists with different role-based personas (Sartre, Watts, Basho, Searle, Skeptic, Optimist, Default)
- Structured YAML schema for historical-figure roles providing behavioral rather than descriptive personas
- Web search enabled per panelist (Anthropic server-side tool)
- Sticky target, pending state for /all broadcasts
- Clean annotated transcripts saved to file
- Multi-line / paste-safe input via `.` send sentinel
- TTS pipeline in TTS/ subdirectory (ElevenLabs)
- Leash pull mechanism — idle panelists passively monitor turns via zero-token
  keyword matching; `/allow handle` lets the moderator follow a pull on demand

---

## File Structure

```
AI_Talk_Show/
├── roles/
│   ├── Basho.yaml
│   ├── Default.yaml
│   ├── Optimist.yaml
│   ├── Sartre.yaml
│   ├── Searle.yaml
│   ├── Skeptic.yaml
│   └── Watts.yaml
├── TTS/
│   ├── render_transcript.py
│   ├── tts_voices.yaml
│   └── list_voices.py
├── transcripts/
│   └── transcript_YYYYMMDD_HHMMSS.txt
├── documentation/
│   ├── AI_Talk_Show_Session_Summary_20260309.md
│   ├── AI_Talk_Show_Session_Summary_20260309.docx
│   ├── Why I built a talk show.md
│   └── Why I built a talk show.docx
├── models.py
├── panelist.py
├── moderator.py
├── conversation.py
├── session.py
├── roles.py
└── main.py
```

---

## Architecture

### Core Data Structures

```python
Statement
└── content: str

Prompt
├── content: str
├── directed_at: list[Panelist] | "all"
└── response_order: list[Panelist] | None

Turn
├── speaker: Panelist | Moderator
├── content: str
├── timestamp: datetime
└── in_response_to: Prompt | Statement | None

PanelistMeta
├── joined_at: int             # turn index when panelist joined
└── onboarding_summary: str | None

Conversation
├── topic: str
├── panelists: list[Panelist]
├── history: list[Turn]        # full record, never truncated
├── pinned: list[Turn]         # always in context, immune to summarization
├── summary: str | None        # rolling summary of out-of-window turns
├── panelist_meta: dict[str, PanelistMeta]
├── active_window: int         # turns sent raw to API (default: 30)
├── pending_prompt: Prompt | None
└── pending_respondents: list[Panelist]

Panelist (base, ABC)
├── name: str                  # display name in transcript
├── handle: str                # unique system ID for history matching
├── role: str
├── trigger_keywords: list[str]  # substring patterns; sniff() checks these
└── sniff(turn) → bool         # zero-token keyword scan; True = caught a scent

HumanPanelist(Panelist)
└── respond() → reads from stdin, returns (Turn, Prompt | None)

ClaudePanelist(Panelist)
├── system_prompt: str         # built internally from template + role yaml
├── moderator_name: str
├── window: int
├── _trigger_keywords: list[str]  # loaded from role YAML at init
└── respond() → Anthropic API with web search tool

Moderator
├── name: str
└── compose_action(raw, current_target, panelists) → Prompt | Statement | None

Session
├── conversation: Conversation
├── moderator: Moderator
├── current_target: list[Panelist] | "all"   # sticky
├── leash_pulls: dict[Panelist, Turn]         # panelist → turn that triggered signal
└── run() → main console loop
```

### Key Design Decisions & Rationale

**Panelist abstraction**
`format_history()` and `respond()` live on each Panelist subclass, not on Conversation. Each provider (Claude, Gemini, Human) knows how to translate shared history into its own API format. Conversation stays provider-agnostic.

**name vs handle**
`name` = display label in transcript (e.g. "Jean").
`handle` = unique system key for history role mapping (e.g. "jean").
`format_history()` uses handle to determine assistant/user role in API calls. Prevents two Claude panelists from claiming each other's turns.

**Shared history**
All panelists receive full conversation history regardless of who a turn was directed at. Preserves the talk show feel and enables cross-panelist commentary.

**Statement vs Prompt**
Statements are declarative moderator turns — no response expected, just recorded in history. Prompts solicit responses from one or more panelists.

**`//` prefix forces Statement**
Everything else is treated as a Prompt directed at current_target. Natural language directives ("Expand on that.") elicit responses without requiring special syntax.

**Sticky target**
`current_target` persists until explicitly changed. Avoids requiring panelist name on every turn during extended single-panelist exchanges.

**Pending state for /all broadcasts**
`/all` broadcasts set pending_prompt and pending_respondents. Panelists don't respond until called on by name. Moderator retains full editorial control over response order. Warning issued if new /all prompt arrives before pending respondents have all replied.

**Role files (YAML) — two schemas**
Roles live in `roles/` directory as `.yaml` files. Two schemas are supported:

*Prose schema* (legacy — default, skeptic, optimist):
- `name`, `description`, `prompt` (default), `claude_prompt` (optional model-specific override)
- `get_prompt()` returns the string as-is

*Structured schema* (preferred — Basho, Searle, sartre, watts):
- Top-level `name` and `description` for menu display
- `identity` — name, era, archetype, voice_description
- `core_beliefs` — philosophical bedrock, keyed by concept
- `dissonance_triggers` — specific things that provoke sharp reactions
- `vocabulary_weights` — `high` and `low` word lists
- `interaction_style` — list of behavioral rules
- `friction_directives` — list of anti-smoothness rules
- `trigger_keywords` — list of substring patterns used by `sniff()` for zero-token
  leash-pull detection; derived from the character's own fault lines, not from
  other panelists' vocabulary; substring matching handles inflection automatically
  (e.g. `"biolog"` matches "biological", "biology", "biologically")
- `system_overrides` — optional per-character overrides for `register_instruction`
  and `closing_instruction` in `SYSTEM_PROMPT_TEMPLATE`

Detection: `get_prompt()` checks for `core_beliefs` key to determine schema type.
Rendering: `render_structured_prompt()` in `roles.py` serializes structured fields
into a compact, model-readable prompt block.

The structured schema is **behavioral** rather than descriptive — `dissonance_triggers`
names what provokes the character, `vocabulary_weights` constrains word choice, and
`friction_directives` enforces anti-smoothness rules. This produces characters that
react from a center of gravity rather than performing a persona.

**Leash pull — autonomous interrupt mechanism**
Idle panelists passively monitor every turn added to history via `sniff(turn) -> bool`,
a zero-token substring scan against their `trigger_keywords` list. When a match is
found, the panelist is flagged in `Session.leash_pulls` and a console signal fires:
`[!!!!!!!] Name is pulling at the leash. /allow handle to let them speak.`

Key design decisions:
- Detection fires only on *panelist response turns*, not moderator prompts — avoids
  signals appearing mid-thinking and preserves natural pacing
- One flag per panelist at a time — subsequent triggers are suppressed until the pull
  is followed or cleared
- Flags clear automatically when the panelist speaks via any path (directed prompt
  or `/allow`)
- `/allow handle` constructs a synthetic Prompt ("You have something to say about
  what was just discussed.") and calls the standard `respond()` pathway — same
  token cost as any directed prompt, no special handling
- `trigger_keywords` are character-intrinsic: derived from the character's own fault
  lines expressed in vocabulary *any* speaker might use — not from specific
  co-panelist vocabulary (which would couple YAML files to each other)
- Pending broadcast respondents are excluded from leash pull checks (they are already
  queued to speak)

**System prompt ownership**
`ClaudePanelist` owns its own `SYSTEM_PROMPT_TEMPLATE` and builds the system prompt
internally. Two slots are overridable per-character via `system_overrides` in the
role YAML:
- `register_instruction` — default: "Respond thoughtfully and concisely"
- `closing_instruction` — default: "Close with a concluding statement"

Structured-schema roles typically override both to match their character's register
and rhetorical style.

**History windowing and summarization**
`active_window` (default: 30 turns) limits raw turns sent to API per call. Full
history always preserved in `conversation.history`. When history exceeds the window,
older turns are compressed by `summarize_history()` rather than hard-dropped. The
summarizer is instructed to be lossless about facts, names, concessions, and pivots
— and lossy about rhetorical scaffolding. Pinned turns are always included regardless
of window.

**Guest onboarding**
When a panelist joins mid-session, `summarize_history()` generates an onboarding
briefing. `ClaudePanelist` receives this as a synthetic message prepended to their
context. `HumanPanelist` receives it as a console print before their first stdin
prompt. `panelist_meta` tracks each panelist's `joined_at` index and
`onboarding_summary`.

**HumanPanelist directive power**
`HumanPanelist.respond()` returns a `(Turn, Prompt | None)` tuple. If the human
panelist types a directive matching `Name, prompt` syntax, the system parses it as
a `Prompt` and queues the named panelist to respond — subject to moderator override
before firing. Moderator-only commands (`//`, `/all`, `/add_guest`, `/drop_guest`,
`/pin`) are not available to panelists.

**`in_response_to` on Turn**
Moderator turns store a reference to their Prompt via `in_response_to`. Used in
transcript generation to annotate directed turns: `[John → Jean]: what do you think?`

**Self-prefixing prevention**
`format_history()` omits the `[name]:` prefix from the model's own prior turns
(stored as `role: "assistant"`). Other speakers retain the prefix. This prevents
the model from pattern-matching the `[name]: content` format into its own output.

---

## Console Command Grammar

### Moderator commands
```
//...                  → Statement (no response expected)
/all [prompt]          → Broadcast to all panelists (pending state)
/all [prompt] Name     → Broadcast + immediately call on Name
/allow handle          → Let a flagged panelist speak (follow a leash pull)
/add_guest Name role   → Introduce new panelist mid-session
/drop_guest Name       → Dismiss panelist gracefully
/pin                   → Pin most recent turn (always in context)
/pin Name              → Pin most recent turn from named panelist
/quit or /exit         → End session
Name, [prompt]         → Directed prompt, updates sticky target
Name [prompt]          → Also works (space after name)
[prompt]               → Directed at current sticky target
.                      → Send (terminates multi-line / pasted input)
```

### HumanPanelist input (subset)
```
Name, [prompt]         → Directive (queues named panelist, moderator can override)
[anything else]        → Plain turn, recorded in history
.                      → Send
```

Input accumulates across lines until `.` is entered on its own line. All input
requires `.` to send, enabling safe paste of multi-paragraph content.

---

## Known Issues / Recent Fixes

- Empty input now ignored (re-prompts) rather than ending session
- `getattr(turn.speaker, 'handle', None)` guards against Moderator lacking handle
- Transcript annotations only applied to moderator turns (not panelist response turns)
- `encoding="utf-8"` on file write fixes Windows smart quote rendering
- `server_tool_use` (not `tool_use`) is the correct block type for web search detection
- Model string: `claude-sonnet-4-6`
- Self-prefixing fix: `format_history()` no longer wraps model's own turns in `[name]:` prefix
- Multi-line input: `read_prompt()` in `session.py` accumulates lines until `.` sentinel
- Response length: tightened to 2 paragraphs maximum; web search restricted to one
  supporting fact — do not enumerate findings
- Structured YAML schema introduced for historical-figure roles; `roles.py` updated
  with `render_structured_prompt()` and `get_system_overrides()`
- `sartre.yaml`, `watts.yaml` migrated from prose to structured schema
- `Searle.yaml` implemented as structured schema (was inert — no `prompt` key)
- `shaman.yaml` renamed `Basho.yaml` and rewritten as structured schema grounded in
  Matsuo Bashō's actual aesthetic philosophy
- `SYSTEM_PROMPT_TEMPLATE` now uses `{register_instruction}` and `{closing_instruction}`
  format slots, overridable per-character via `system_overrides` in role YAML
- Repeated-passage artifact observed in Jean (Sartre) responses under web search —
  monitor for pattern
- Leash pull mechanism implemented — `sniff()`, `trigger_keywords`, `AllowAction`,
  `/allow` command, `leash_pulls` dict, `_check_leash_pulls()`, `_add_turn()` wrapper,
  `handle_allow()` in session.py
- `trigger_keywords` added to all four structured YAML roles — character-intrinsic,
  derived from each character's own fault lines
- Searle's `trigger_keywords` expanded with philosophy-of-mind vocabulary ("inner life",
  "subjective", "sentien", "what it is like", "qualia") to catch sophisticated
  consciousness claims, not just naive ones
- Leash pull signal now fires after full response text is printed (not before)
- Leash pull checks suppressed on moderator turns — only panelist responses trigger scans
- Duplicate panelist name guard added to `main.py` setup loop (same check as `/add_guest`)
- Web search response duplication fixed — when search occurs, only the final text block
  is used (post-search model output); pre-search fragment was causing near-duplicate
  opening sentences when joined with the continuation block
- Role YAML files renamed to consistent Title Case (Sartre, Watts, Default, Optimist,
  Skeptic); `load_role()` made case-insensitive so existing code passing lowercase names
  still resolves correctly

---

## Remaining Open Issues

- Multi-target syntax (`Jean and Alan, prompt`) not yet supported — use `/all` or
  address separately
- `prompt.directed_at` renders as Python object repr in API messages when it is a
  list — functionally harmless but untidy; a named target or "all" string would be cleaner

---

## Roadmap (Prioritized)

1. **`summarize_history()`** — utility API call (not a panelist); smart prompt
   lossless on facts/concessions, lossy on scaffolding; foundation for everything below
2. **`Conversation.panelist_meta` + `pinned`** — data model updates;
   `PanelistMeta(joined_at, onboarding_summary)`; `pinned: list[Turn]`
3. **`format_history()` updates** — onboarding briefing prepend for late-joining
   panelists; rolling summary for out-of-window turns; merge both when applicable
4. **`/add_guest` and `/drop_guest`** — mid-session guest management; onboarding
   via summarizer; graceful dismissal with moderator farewell
5. **Parser fixes** — `/pin` command; multi-target syntax; no-target-on-open guard
6. **HumanPanelist directive power** — `respond()` returns `(Turn, Prompt | None)`;
   moderator override hook before queuing
7. **Gemini panelist** — `GeminiPanelist(Panelist)` subclass; own `format_history()`;
   own API key handling
8. **Persistence** — save/load conversations to SQLite, resume later
9. **Persona authoring guide** — how to write a structured YAML role from scratch
   for any domain (historical figures, fictional characters, domain experts);
   covers schema fields, trigger_keywords calibration, cross-panel fault-line
   design, and worked examples beyond the philosophy-of-mind panel.
   Key principle: `friction_directives` and `trigger_keywords` must be derived
   from the character's own worldview — never name specific co-panelists.
   Friction emerges from worldview collision, not from scripted opposition.
   A role that names its opponents is brittle and domain-specific; a role that
   expresses its own fault lines is composable across any panel.
10. **Slack integration** — `slack_session.py`; open floor model; AI panelists respond
    to @mentions; human panelists are registered Slack users
11. **Web UI** — Flask frontend, user login, conversation history browser
12. **Speech layer** — TTS for AI voices (ElevenLabs), STT for human panelists
    (Whisper/Deepgram)

---

## Dependencies

```bash
pip install anthropic pyyaml
```

Environment variable required:
```
ANTHROPIC_API_KEY=your_key_here
```

---

## TTS Pipeline

Scripts live in `TTS/`. Requires ElevenLabs quota (30,000 chars/month on Starter plan).

```bash
cd TTS
python list_voices.py                          # list available voice IDs
python render_transcript.py ../transcripts/transcript_YYYYMMDD_HHMMSS.txt  # render to MP3
```

`tts_voices.yaml` maps panelist display names to ElevenLabs voice IDs and settings.
Add a new entry for each speaker name used in a transcript.

Partial renders are saved on quota failure — the MP3 up to the failed turn is
exported rather than lost.

---

## Notes for Next Session

Claude Code has memory of this project at `~/.claude/projects/.../memory/MEMORY.md`
— no need to paste this document. Just open the project and say "let's continue".

Good next steps (in rough priority order):
1. **Implement `summarize_history()`** — standalone, testable immediately
2. **Update `Conversation` data model** — add `panelist_meta`, `pinned`
3. **Update `format_history()`** — onboarding + rolling summary support
4. **Implement `/add_guest` and `/drop_guest`**
5. **Tune `trigger_keywords`** — run more sessions across topics; watch signal rate;
   tighten noisy keywords, expand gaps revealed by cross-panel analysis
