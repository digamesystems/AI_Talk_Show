# AI Panel Discussion — Project Summary
*Updated 2026-03-06 (2) — for continuity across Claude sessions*

---

## Project Vision

A console-based (first) then web-based moderated panel discussion app where a human moderator directs conversation between multiple AI panelists (and optionally human panelists). Inspired by a talk show format — the moderator holds the talking stick and directs who speaks. Each panelist hears the full conversation history regardless of who a prompt was directed at.

Longer term vision includes: text-to-speech/speech-to-text for a "real" talk show feel, YouTube content production, and potentially a multi-user hosted platform.

---

## Current Status

A working Python console spike is complete and road-tested. Core conversation loop is functional with:
- Two Claude panelists with different role-based personas
- Web search enabled per panelist (Anthropic server-side tool)
- Sticky target, pending state for /all broadcasts
- Clean annotated transcripts saved to file
- Multi-line / paste-safe input via `.` send sentinel

---

## File Structure

```
AI_Talk_Show/
├── roles/
│   ├── default.yaml
│   ├── skeptic.yaml
│   ├── optimist.yaml
│   ├── sartre.yaml
│   └── watts.yaml
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

Conversation
├── topic: str
├── panelists: list[Panelist]
├── history: list[Turn]        # full record, never truncated
├── summary: str | None
├── active_window: int         # API context window only, not archive
├── pending_prompt: Prompt | None
└── pending_respondents: list[Panelist]

Panelist (base, ABC)
├── name: str                  # display name in transcript
├── handle: str                # unique system ID for history matching
└── role: str

HumanPanelist(Panelist)
└── respond() → reads from stdin

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
Everything else is treated as a Prompt directed at current_target. This was a usability decision — natural language directives ("Expand on that.") should elicit responses without requiring special syntax.

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

**History windowing**
`active_window` limits how many turns get sent to the API per call (cost management). Full history always preserved in `conversation.history` and always saved to transcript.

**`in_response_to` on Turn**
Moderator turns store a reference to their Prompt via `in_response_to`. Used in transcript generation to annotate directed turns: `[John → Jean]: what do you think?`

**Self-prefixing prevention**
`format_history()` omits the `[name]:` prefix from the model's own prior turns (stored as `role: "assistant"`). Other speakers retain the prefix. This prevents the model from pattern-matching the `[name]: content` format into its own output.

---

## Console Command Grammar

```
//...              → Statement (no response expected)
/all [prompt]      → Broadcast to all panelists (pending state)
/all [prompt] Name → Broadcast + immediately call on Name
Name, [prompt]     → Directed prompt, updates sticky target
Name [prompt]      → Also works (space after name)
[prompt]           → Directed at current sticky target
/quit or /exit     → End session
.                  → Send (terminates multi-line / pasted input)
```

Input accumulates across lines until `.` is entered on its own line. All prompts require `.` to send, enabling safe paste of multi-paragraph content.

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
- Historical figure roles added: `sartre.yaml` (Jean-Paul Sartre) and `watts.yaml` (Alan Watts)
- Transcript bug fixed: directed moderator follow-ups (`[John → Jean]: ...`) now recorded in both the pending-broadcast and fresh-direct code paths
- TTS experiment files moved to `TTS/` subdirectory

---

## Remaining Open Issues

- Response length still occasionally runs to 4 paragraphs when web search returns rich material — accepted as reasonable panel behaviour
- Panelist occasionally directs rhetorical questions back at moderator — accepted as moderator can redirect

---

## Roadmap (Prioritized)

1. **Continue road testing** — more topics, refine role yamls, observe edge cases
2. **Add Gemini panelist** — `GeminiPanelist(Panelist)` subclass, own `format_history()`, own API key handling
3. **Conversation summarization** — when history exceeds window, summarize older turns via API call rather than hard cutoff
4. **Persistence** — save/load conversations to SQLite, resume later
5. **Web UI** — Flask frontend, user login, conversation history browser
6. **Speech layer** — TTS for AI voices (ElevenLabs), STT for human panelists (Whisper/Deepgram)

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
1. **More role experimentation** — test other historical figures, observe edge cases
2. **Add Gemini panelist** — `GeminiPanelist(Panelist)` subclass, own `format_history()`, own API key
3. **Conversation summarization** — summarize older turns via API when history exceeds window
4. **TTS render** — top up ElevenLabs quota ($5 Starter) and render a full transcript
