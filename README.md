# AI Talk Show

A moderated panel discussion app where a human host directs conversation between multiple AI panelists. Each panelist is given a distinct personality and voice. The moderator holds the talking stick — directing who speaks, when, and about what.

Built to explore a specific question: can introducing friction and disagreement into AI interactions produce richer, more interesting results than the smooth consensus that LLMs tend toward on their own?

The conceptual background is in the essay [Why I Built a Talk Show](Why%20%20I%20built%20a%20talk%20show.docx) — the short version is that LLMs, when used conventionally, tend to converge toward a kind of statistically average response. This project is an experiment in whether multi-agent panels with human intervention can push against that tendency.

---

## What It Does

You play the host. You direct questions at individual panelists or broadcast to all of them. Each panelist hears the full conversation history and responds in character. You can introduce factual provocations, redirect mid-discussion, bring in new guests, and generally cause the kind of productive chaos that a good talk show host generates.

A session with Sartre, Alan Watts, and a character drawn from Matsuo Bashō discussing the ethical obligations we might have toward non-human minds looks — and reads — quite differently than a single LLM asked the same question.

---

## Quickstart

**Requirements:** Python 3.10+, an Anthropic API key

```bash
git clone https://github.com/digamesystems/AI_Talk_Show.git
cd AI_Talk_Show
pip install anthropic pyyaml
export ANTHROPIC_API_KEY=your_key_here
python main.py
```

On startup you'll be prompted for a discussion topic and which panelists to include. Type your prompts at the console. Use `.` on its own line to send multi-line or pasted input.

---

## Basic Commands

| Command | What it does |
|---|---|
| `Jean, what do you think?` | Direct a prompt at a named panelist |
| `Alan, respond to Jean's point` | Direct follow-up |
| `/all what is consciousness?` | Broadcast to all panelists (pending state — call on each by name) |
| `//` followed by text | Moderator statement, no response expected |
| `/add_guest Name role` | Introduce a new panelist mid-session |
| `/drop_guest Name` | Gracefully dismiss a panelist |
| `/pin` | Pin the last turn — always kept in context |
| `/quit` | End session and save transcript |

The current target is sticky — once you've directed at a panelist, subsequent prompts go to them until you name someone else.

---

## Panelist Roles

Roles are defined in YAML files in the `roles/` directory. Each file specifies a name, description, and system prompt. Current built-in roles:

- `sartre` — Jean-Paul Sartre, existentialist
- `watts` — Alan Watts, interpreter of Eastern thought  
- `shaman` — ranges freely across traditions
- `skeptic` — adversarial, demands evidence
- `optimist` — constructive, seeks synthesis
- `default` — neutral, balanced

To create a new role, add a `.yaml` file to `roles/` following the same structure. The model-specific `claude_prompt` field lets you tune the same conceptual role per provider.

---

## Transcripts

Sessions are saved automatically to timestamped transcript files. The format annotates directed turns:

```
[John → Jean]: what do you make of Otto's behavior?
[Jean]: The moment we must describe a creature's behavior in intentional terms...
```

---

## Architecture Notes

For contributors and the technically curious: the full architecture document — data structures, design decisions, command grammar, and roadmap — is in [`DEVELOPMENT.md`](DEVELOPMENT.md).

The short version: `Conversation` is provider-agnostic. Each `Panelist` subclass owns its own `format_history()` and `respond()` methods, translating the shared history into whatever format its API requires. Adding a Gemini or GPT panelist means subclassing `Panelist` — the conversation loop doesn't change.

---

## Roadmap

Near term:
- History summarization for long sessions
- `/add_guest` and `/drop_guest` (mid-session guest management)
- Multi-target syntax (`Jean and Alan, ...`)
- Gemini panelist support

Longer term:
- Slack integration as a multi-user interface
- Web UI
- Speech layer (TTS for AI voices, STT for human participants)

---

## Dependencies

```
pip install anthropic pyyaml
```


---

## License

MIT

---

*Feedback welcome — open an issue or reach out directly.*
