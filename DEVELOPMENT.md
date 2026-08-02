# AI Panel Discussion — Project Summary
*Updated 2026-08-02 — for continuity across Claude sessions*

---

## Project Vision

A console-based (first) then web-based moderated panel discussion app where a human moderator directs conversation between multiple AI panelists (and optionally human panelists). Inspired by a talk show format — the moderator holds the talking stick and directs who speaks. Each panelist hears the full conversation history regardless of who a turn was directed at.

Longer term vision includes: Slack integration as a natural multi-user interface, text-to-speech/speech-to-text for a real talk show feel, YouTube content production, and potentially a multi-user hosted platform.

---

## Current Status

A working Python console spike is complete and road-tested. Core conversation loop is functional with:
- Multiple Claude panelists with different role-based personas (Sartre, Watts, Basho, Searle, Wittgenstein, Turing, Skeptic, Optimist, Default)
- **DeepSeek panelist support** — `DeepSeekPanelist` talks to DeepSeek's OpenAI-compatible API
  (`openai` SDK, `base_url` pointed at DeepSeek, model `deepseek-chat`); same role YAML files
  work for both providers. First real (non-Claude) proof that `Panelist` is genuinely
  provider-agnostic, not just designed to be. Requires `DEEPSEEK_API_KEY`.
- **Panel presets** — `panels/*.yaml` files describe a full roster (moderator name, topic,
  panelist list with type/name/role) that can be loaded in one shot instead of building a
  session by hand every time; `main.py` asks "build by hand or load from file?" at startup.
- Structured YAML schema for historical-figure roles providing behavioral rather than descriptive personas
- Web search enabled per Claude panelist (Anthropic server-side tool) — not yet available for DeepSeek panelists
- Sticky target, pending state for /all broadcasts
- `/help` and `/?` — prints the full current command list on demand; startup banners now
  point at this instead of maintaining their own separate (and drifting) partial lists
- Clean annotated transcripts saved to `transcripts/` — directed turns and interjections annotated
- Multi-line / paste-safe input via `.` send sentinel (moderator and human panelists)
- Human panelists supported alongside AI panelists; `!` command signals human interjection request
- History summarization for long sessions; onboarding summaries for mid-session guests
  (Claude panelists only — see Known Issues)
- Mid-session guest management via `/add_guest` and `/drop_guest`
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
│   ├── Turing.yaml
│   ├── Watts.yaml
│   └── Wittgenstein.yaml
├── panels/
│   ├── cross_model_pilot.yaml
│   └── nuclear_legitimacy.yaml
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
├── in_response_to: Prompt | Statement | None
└── interjection: bool             # True when turn follows a leash pull (/allow)

AddGuestAction / DropGuestAction / AllowAction / InterjectionRequest / HelpAction
└── setup/control actions parsed by Moderator.compose_action(), dispatched to
    matching Session.handle_*() methods

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
└── respond() → reads from stdin (multi-line, `.` to send), returns Turn

ClaudePanelist(Panelist)
├── system_prompt: str         # built from module-level SYSTEM_PROMPT_TEMPLATE + role yaml
├── moderator_name: str
├── window: int
├── _trigger_keywords: list[str]  # loaded from role YAML at init
└── respond() → Anthropic API with web search tool

DeepSeekPanelist(Panelist)
├── system_prompt: str         # same SYSTEM_PROMPT_TEMPLATE as ClaudePanelist
├── moderator_name: str
├── window: int
├── _trigger_keywords: list[str]
├── client: openai.OpenAI      # base_url="https://api.deepseek.com", DEEPSEEK_API_KEY
└── respond() → deepseek-chat via Chat Completions; no web search tool yet;
    does not call summarize_history() beyond window (see Known Issues)

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
`format_history()` and `respond()` live on each Panelist subclass, not on Conversation. Each provider (Claude, DeepSeek, Human) knows how to translate shared history into its own API format. Conversation stays provider-agnostic — proven out for real, not just by design, once `DeepSeekPanelist` shipped and needed zero changes to `Conversation`, `Session`, or `Moderator`.

**Panel presets (`panels/*.yaml`)**
An alternative to building a session by hand every time: a preset file specifies `moderator_name`, `topic`, and a `panelists` list (`type`: claude/deepseek/human, `name`, `role`). `main.py`'s `create_session()` asks "build by hand or load from file?" and dispatches to `create_session_from_file()`, which reuses the same duplicate-name guard as the hand-built path and falls back to it if the preset is empty or missing. Existed first as a convenience for repeatedly re-running the same panel roster; became load-bearing for the cross-model experiment (Roadmap, cross-model entry below), since a preset is the only practical way to reliably load a mixed Claude/DeepSeek roster for a repeatable test.

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

*Structured schema* (preferred — Basho, Searle, Sartre, Watts, Wittgenstein, Turing):
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
- Followed leash pulls set `turn.interjection = True`; transcript renders as
  `[Name Interjects]` instead of `[Name]`
- Human panelists can signal an interjection request by typing `!` (or `!handle`
  for a specific panelist) at the moderator prompt — registers in `leash_pulls`,
  same `/allow` flow applies

**System prompt ownership**
`SYSTEM_PROMPT_TEMPLATE` lives at module level in `panelist.py`, shared by
`ClaudePanelist` and `DeepSeekPanelist` (promoted out of `ClaudePanelist` when
`DeepSeekPanelist` was added, to avoid a second copy of the same ~20-line template
drifting out of sync). Two slots are overridable per-character via `system_overrides`
in the role YAML:
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
of window. **Known gap:** `summarize_history()` in `conversation.py` is written
against Anthropic's `client.messages.create()` shape; `DeepSeekPanelist.respond()`
does not call it and falls back to plain window truncation instead. Not an issue for
short sessions (under ~30 turns); would need a provider-agnostic rewrite of
`summarize_history()` before long DeepSeek sessions are safe.

**Guest onboarding**
When a panelist joins mid-session, `summarize_history()` generates an onboarding
briefing. `ClaudePanelist` receives this as a synthetic message prepended to their
context. `HumanPanelist` receives it as a console print before their first stdin
prompt. `panelist_meta` tracks each panelist's `joined_at` index and
`onboarding_summary`.

**HumanPanelist input**
`HumanPanelist.respond()` accumulates lines until `.` on its own line — same sentinel
as the moderator. The human's typed input is not echoed after submission (terminal
already shows it). Human panelists can request to interject by typing `!` at the
moderator prompt between turns; this registers a leash pull that the moderator can
follow with `/allow handle` on their next turn.

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
/allow handle          → Let a flagged panelist speak (follow a leash pull)
!                      → Register human panelist interjection request
!handle                → Register specific human panelist interjection request
/add_guest Name role   → Introduce new panelist mid-session
/drop_guest Name       → Dismiss panelist gracefully
/help or /?            → Print the full current command list
/quit or /exit         → End session
Name, [prompt]         → Directed prompt, updates sticky target
Name [prompt]          → Also works (space after name)
[prompt]               → Directed at current sticky target
.                      → Send (terminates multi-line / pasted input)
```
Note: `/all [prompt] Name` (broadcast + immediately call on Name in one command) is
**not** implemented, despite once being documented here — `moderator.py`'s actual
`/all` handling only broadcasts. Corrected 2026-08-02 after finding the mismatch
during a documentation sync pass; see Remaining Open Issues.

### HumanPanelist input
```
[anything]             → Plain turn, recorded in history
.                      → Send (terminates multi-line / pasted input)
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
- `Turn.interjection: bool` field added; transcript renders `[Name Interjects]` for
  leash-pull responses instead of `[Name]`
- `InterjectionRequest` action added — `!` or `!handle` at moderator prompt registers
  human panelist leash pull; same `/allow` flow as AI panelists
- `HumanPanelist.respond()` updated to multi-line input with `.` sentinel
- Human panelist response no longer echoed after submission (was printing twice)
- `Wittgenstein.yaml` and `Turing.yaml` added as structured-schema roles
- Design principle established: `friction_directives` and `trigger_keywords` must be
  derived from the character's own worldview — never name specific co-panelists;
  friction emerges from worldview collision, not scripted opposition
- `transcripts/` and `documentation/` directories created; `main.py` updated to save
  transcripts to `transcripts/` automatically; `.gitignore` added for `__pycache__`
- **2026-08-02:** `DeepSeekPanelist` added (`panelist.py`) — OpenAI-compatible client
  against DeepSeek's API; `SYSTEM_PROMPT_TEMPLATE` promoted from a `ClaudePanelist`
  class attribute to a module-level constant shared by both provider panelists
- **2026-08-02:** Panel preset system added — `panels/*.yaml`, `main.py`'s
  `create_session_from_file()`/`build_panelist_from_preset()`/`prompt_panel_file_selection()`
- **2026-08-02:** `/help` and `/?` commands added (`HelpAction` in `models.py`,
  handled in `session.py`); `main.py` and `session.run()`'s own separate partial
  command-list banners trimmed to point at `/help` instead of maintaining duplicates
- **2026-08-02:** Fixed a crash printing "Matsuo Bashō" on a default Windows console
  (cp1252 can't encode the macron) — `sys.stdout.reconfigure(encoding="utf-8")` added
  near the top of `main.py`
- **2026-08-02:** Fixed a stale doc claim — `/all [prompt] Name` (broadcast + immediate
  call) was documented here but never actually implemented in `moderator.py`; doc
  corrected to match the code rather than the other way around

---

## Remaining Open Issues

- Multi-target syntax (`Jean and Alan, prompt`) not yet supported — use `/all` or
  address separately
- `prompt.directed_at` renders as Python object repr in API messages when it is a
  list — functionally harmless but untidy; a named target or "all" string would be cleaner
- `summarize_history()` is Anthropic-specific; `DeepSeekPanelist` skips it and falls
  back to plain truncation beyond the window — fine short-term, needs a
  provider-agnostic rewrite before long DeepSeek sessions
- No web search tool wired up for `DeepSeekPanelist` yet — Claude panelists can search,
  DeepSeek panelists currently can't
- Minor: `/add_guest`/`/allow`/unknown-command usage messages in `moderator.py` return
  an empty-content `Prompt(directed_at=current_target)` to keep the input loop going —
  if `current_target` is a single directed panelist (not `"all"`) rather than a broadcast,
  this actually fires a live API call with blank content. Pre-existing, low-impact
  (only triggers on a malformed command while mid-conversation with one panelist),
  noticed 2026-08-02 while adding `/help` — `/help` itself deliberately avoids this
  by using a dedicated `HelpAction` instead of the same empty-Prompt pattern.

---

## Roadmap (Prioritized)

1. **Multi-target syntax** — `Jean and Alan, prompt`; currently use `/all` or address
   separately
2. **`/pin` command** — pin most recent turn (always in context); currently unimplemented
3. **HumanPanelist directive power** — human panelist can direct other panelists from
   within their turn (`Name, prompt` syntax); moderator override hook before queuing
4. **Gemini panelist** — `GeminiPanelist(Panelist)` subclass; own `format_history()`;
   own API key handling. `DeepSeekPanelist` shipped first (2026-08-02, cheaper to run
   and OpenAI-SDK-compatible) — Gemini would need its own client library
   (`google-generativeai` or successor), not a shared implementation with the
   OpenAI-compatible pair.
5. **Provider-agnostic `summarize_history()`** — currently Anthropic-only; blocks long
   (>30 turn) DeepSeek sessions from summarizing instead of truncating
6. **Persistence** — save/load conversations to SQLite, resume later
7. **Persona authoring guide** — how to write a structured YAML role from scratch
   for any domain (historical figures, fictional characters, domain experts);
   covers schema fields, trigger_keywords calibration, cross-panel fault-line
   design, and worked examples beyond the philosophy-of-mind panel.
   Key principle: `friction_directives` and `trigger_keywords` must be derived
   from the character's own worldview — never name specific co-panelists.
   Friction emerges from worldview collision, not from scripted opposition.
   A role that names its opponents is brittle and domain-specific; a role that
   expresses its own fault lines is composable across any panel.
8. **Slack integration** — `slack_session.py`; open floor model; AI panelists respond
   to @mentions; human panelists are registered Slack users
9. **Web UI** — Flask frontend, user login, conversation history browser
10. **Speech layer** — TTS for AI voices (ElevenLabs), STT for human panelists
    (Whisper/Deepgram)

### Cross-model experiment (essay-project Roadmap #9 — see `documentation/Future Essays - Roadmap.md`)

Engineering side of a question the essay project is tracking: does panel "richness"
come from persona configuration, or from having genuinely different models in the
room? `DeepSeekPanelist` + `panels/*.yaml` presets are the infrastructure for this.
First factory-settings data point (2026-08-02, `role: Default` on both sides, no
persona): real content-level cross-pollination between Claude and DeepSeek, but in a
smooth/concessive register — not the sharp friction the persona-configured six-Claude
panel produces. Tentative read: friction is coming from `friction_directives`
configuration, not model diversity alone. Full writeup and both transcripts referenced
in the essay roadmap entry; next step there is the same persona on both models to
isolate the variable further.

---

## Dependencies

```bash
pip install anthropic openai pyyaml
```

`openai` is only needed for `DeepSeekPanelist` (DeepSeek's API is OpenAI-SDK-compatible)
— not required if you're only running Claude/Human panelists.

Environment variables:
```
ANTHROPIC_API_KEY=your_key_here      # required
DEEPSEEK_API_KEY=your_key_here       # required only if using DeepSeekPanelist
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
1. **Multi-target syntax** — `Jean and Alan, prompt`
2. **`/pin` command** — implementation straightforward; data model already supports it
3. **Tune `trigger_keywords`** — run more sessions across topics; watch signal rate;
   tighten noisy keywords, expand gaps revealed by cross-panel analysis
4. **HumanPanelist directive power** — `respond()` returns `(Turn, Prompt | None)`
