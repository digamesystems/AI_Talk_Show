# AI Panel Discussion — Project Summary
*Updated 2026-03-09 — for continuity across Claude sessions*

---

## Project Vision

A console-based (first) then web-based moderated panel discussion app where a human moderator directs conversation between multiple AI panelists (and optionally human panelists). Inspired by a talk show format — the moderator holds the talking stick and directs who speaks. Each panelist hears the full conversation history regardless of who a turn was directed at.

Longer term vision includes: Slack integration as a natural multi-user interface, text-to-speech/speech-to-text for a real talk show feel, YouTube content production, and potentially a multi-user hosted platform.

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
│   └── shaman.yaml
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
└── role: str

HumanPanelist(Panelist)
└── respond() → reads from stdin, returns (Turn, Prompt | None)

ClaudePanelist(Panelist)
├── system_prompt: str         # built internally from template + role yaml
├── moderator_name: str
├── window: int
└── respond() → Anthropic API with web search tool

Moderator
├── name: str
└── compose_action(raw, current_target, panelists) → Prompt | Statement | None

Session
├── conversation: Conversation
├── moderator: Moderator
├── current_target: list[Panelist] | "all"   # sticky
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

**Role files (YAML)**
Roles live in `roles/` directory as `.yaml` files with metadata fields:
- `name`, `description`, `prompt` (default), `claude_prompt` (optional override)
- Model-specific prompt overrides allow same conceptual role to be tuned per provider
- `roles.py` handles loading, listing, and prompt selection

**System prompt ownership**
`ClaudePanelist` owns its own `SYSTEM_PROMPT_TEMPLATE` and builds the system prompt internally from `moderator_name`, `name`, and role yaml. `main.py` just passes high-level parameters.

**History windowing and summarization**
`active_window` (default: 30 turns) limits raw turns sent to API per call. Full history always preserved in `conversation.history`. When history exceeds the window, older turns are compressed by `summarize_history()` rather than hard-dropped. The summarizer is instructed to be lossless about facts, names, concessions, and pivots — and lossy about rhetorical scaffolding. Pinned turns are always included regardless of window.

**Guest onboarding**
When a panelist joins mid-session, `summarize_history()` generates an onboarding briefing. `ClaudePanelist` receives this as a synthetic message prepended to their context. `HumanPanelist` receives it as a console print before their first stdin prompt. `panelist_meta` tracks each panelist's `joined_at` index and `onboarding_summary`.

**HumanPanelist directive power**
`HumanPanelist.respond()` returns a `(Turn, Prompt | None)` tuple. If the human panelist types a directive matching `Name, prompt` syntax, the system parses it as a `Prompt` and queues the named panelist to respond — subject to moderator override before firing. Moderator-only commands (`//`, `/all`, `/add_guest`, `/drop_guest`, `/pin`) are not available to panelists.

**`in_response_to` on Turn**
Moderator turns store a reference to their Prompt via `in_response_to`. Used in transcript generation to annotate directed turns: `[John → Jean]: what do you think?`

**Self-prefixing prevention**
`format_history()` omits the `[name]:` prefix from the model's own prior turns (stored as `role: "assistant"`). Other speakers retain the prefix. This prevents the model from pattern-matching the `[name]: content` format into its own output.

---

## Console Command Grammar

### Moderator commands
```
//...                  → Statement (no response expected)
/all [prompt]          → Broadcast to all panelists (pending state)
/all [prompt] Name     → Broadcast + immediately call on Name
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

Input accumulates across lines until `.` is entered on its own line. All input requires `.` to send, enabling safe paste of multi-paragraph content.

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
- Response length: "3 paragraphs or fewer" added to `SYSTEM_PROMPT_TEMPLATE`; concision note added to `skeptic.yaml`
- Historical figure roles added: `sartre.yaml`, `watts.yaml`, `shaman.yaml`
- Transcript bug fixed: directed moderator follow-ups (`[John → Jean]: ...`) now recorded in both the pending-broadcast and fresh-direct code paths
- TTS experiment files moved to `TTS/` subdirectory

---

## Remaining Open Issues

- Response length still occasionally runs to 4 paragraphs when web search returns rich material — accepted as reasonable panel behaviour
- Panelist occasionally directs rhetorical questions back at moderator — accepted as moderator can redirect
- No `current_target` on session open — natural openers without a named target stall; `/all` or explicit name required first
- Multi-target syntax (`Jean and Alan, prompt`) not yet supported — use `/all` or address separately

---

## Roadmap (Prioritized)

1. **`summarize_history()`** — utility API call (not a panelist); smart prompt lossless on facts/concessions, lossy on scaffolding; foundation for everything below
2. **`Conversation.panelist_meta` + `pinned`** — data model updates; `PanelistMeta(joined_at, onboarding_summary)`; `pinned: list[Turn]`
3. **`format_history()` updates** — onboarding briefing prepend for late-joining panelists; rolling summary for out-of-window turns; merge both when applicable
4. **`/add_guest` and `/drop_guest`** — mid-session guest management; onboarding via summarizer; graceful dismissal with moderator farewell
5. **Parser fixes** — `/pin` command; multi-target syntax; no-target-on-open guard
6. **HumanPanelist directive power** — `respond()` returns `(Turn, Prompt | None)`; moderator override hook before queuing
7. **Gemini panelist** — `GeminiPanelist(Panelist)` subclass; own `format_history()`; own API key handling
8. **Persistence** — save/load conversations to SQLite, resume later
9. **Slack integration** — `slack_session.py`; open floor model; AI panelists respond to @mentions; human panelists are registered Slack users
10. **Web UI** — Flask frontend, user login, conversation history browser
11. **Speech layer** — TTS for AI voices (ElevenLabs), STT for human panelists (Whisper/Deepgram)

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
python render_transcript.py ../transcript.txt  # render to MP3
```

`tts_voices.yaml` maps panelist display names to ElevenLabs voice IDs and settings. Add a new entry for each speaker name used in a transcript.

Partial renders are saved on quota failure — the MP3 up to the failed turn is exported rather than lost.

---

## Notes for Next Session

Claude Code has memory of this project at `~/.claude/projects/.../memory/MEMORY.md` — no need to paste this document. Just open the project and say "let's continue".

Good next steps (in rough priority order):
1. **Implement `summarize_history()`** — standalone, testable immediately; includes smart summarization prompt
2. **Update `Conversation` data model** — add `panelist_meta`, `pinned`
3. **Update `format_history()`** — onboarding + rolling summary support
4. **Implement `/add_guest` and `/drop_guest`**