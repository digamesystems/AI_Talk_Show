# AI Talk Show

A moderated panel discussion app where a human host directs conversation between multiple AI panelists. Each panelist is given a distinct personality and voice. The moderator holds the talking stick — directing who speaks, when, and about what.

Built to explore a specific question: can introducing friction and disagreement into AI interactions produce richer, more interesting results than the smooth consensus that LLMs tend toward on their own?

The conceptual background is in the essay [Why I Built a Talk Show](documentation/Why%20I%20built%20a%20talk%20show.md) — the short version is that LLMs, when used conventionally, tend to converge toward a kind of statistically average response. This project is an experiment in whether multi-agent panels with human intervention can push against that tendency.

---

## What It Does

You play the host. You direct questions at individual panelists or broadcast to all of them. Each panelist hears the full conversation history and responds in character. You can introduce factual provocations, redirect mid-discussion, bring in new guests, and generally cause the kind of productive chaos that a good talk show host generates.

Idle panelists passively monitor the conversation. When a turn crosses one of their configured fault lines, they signal with `[!!!!!!!] Name is pulling at the leash` — the moderator can follow the pull with `/allow handle` or ignore it and continue. No extra API calls: detection is pure keyword matching.

Human panelists are fully supported alongside AI panelists. They type their turns at the console using the same `.` sentinel to send. A human panelist can signal they want to interject by typing `!` at the moderator prompt — the same leash pull flow applies.

A session with Sartre, Wittgenstein, Turing, and Searle discussing the minds of octopi looks — and reads — quite differently than a single LLM asked the same question. The panel composition is the editorial decision — choose guests whose fault lines intersect with your topic.

---

## Quickstart

**Requirements:** Python 3.10+, an Anthropic API key (DeepSeek key optional — see below)

```bash
git clone https://github.com/digamesystems/AI_Talk_Show.git
cd AI_Talk_Show
pip install anthropic openai pyyaml
export ANTHROPIC_API_KEY=your_key_here
python main.py
```

At startup you'll choose to build a panel by hand (prompted for a topic and each
panelist in turn) or load one from a preset file in `panels/` (moderator name, topic,
and full roster defined in one YAML file — see `panels/nuclear_legitimacy.yaml` for
an example). Type your prompts at the console; use `.` on its own line to send
multi-line or pasted input; type `/help` once the session starts for the full command
list.

---

## Basic Commands

| Command | What it does |
|---|---|
| `Jean, what do you think?` | Direct a prompt at a named panelist |
| `Alan, respond to Jean's point` | Direct follow-up |
| `/all what is consciousness?` | Broadcast to all panelists (pending state — call on each by name) |
| `/allow jean` | Follow a leash pull — let a flagged AI panelist speak |
| `!` | Signal a human panelist wants to interject (at moderator prompt) |
| `//` followed by text | Moderator statement, no response expected |
| `/add_guest Name role` | Introduce a new panelist mid-session |
| `/drop_guest Name` | Gracefully dismiss a panelist |
| `/help` or `/?` | Print the full current command list |
| `/quit` | End session and save transcript |

The current target is sticky — once you've directed at a panelist, subsequent prompts go to them until you name someone else.

---

## Panelist Roles

Roles are defined in YAML files in the `roles/` directory. Current built-in roles:

- `Basho` — Matsuo Bashō, haiku master and precise observer
- `Searle` — John Searle, biological realist and critic of AI consciousness claims
- `Sartre` — Jean-Paul Sartre, existentialist philosopher of radical freedom
- `Watts` — Alan Watts, interpreter of Zen, Taoism, and Vedanta
- `Wittgenstein` — Ludwig Wittgenstein, meaning-as-use and the dissolution of philosophical problems
- `Turing` — Alan Turing, operationalist and architect of the Imitation Game
- `Skeptic` — adversarial, demands evidence
- `Optimist` — constructive, seeks synthesis
- `Default` — neutral, balanced

Historical-figure roles use a structured YAML schema with `core_beliefs`, `dissonance_triggers`, `vocabulary_weights`, `friction_directives`, and `trigger_keywords` — producing behavioral rather than purely descriptive personas. The `trigger_keywords` field drives the leash pull mechanism: a list of substring patterns derived from the character's own fault lines that fire when an idle panelist's fault lines are crossed. Generic roles use a simpler prose prompt.

The schema is domain-agnostic — any historical figure, fictional character, or domain expert can be authored as a role. See [`DEVELOPMENT.md`](DEVELOPMENT.md) for the full schema reference.

A role is the persona; separately, each panelist also has a **type** — `claude`, `deepseek`, or `human` — that decides which model (if any) powers it. The same role file works with any AI type: `Sartre` can be run as a Claude panelist or a DeepSeek panelist without changes to `Sartre.yaml`.

---

## Transcripts

Sessions are saved automatically to timestamped files in the `transcripts/` directory. The format annotates directed turns and interjections:

```
[JP → Jean]: what do you make of Otto's behavior?
[Jean]: The moment we must describe a creature's behavior in intentional terms...
[Ludwig Interjects]: What work is "causal powers" doing there, exactly?
```

---

## Architecture Notes

For contributors and the technically curious: the full architecture document — data structures, design decisions, command grammar, and roadmap — is in [`DEVELOPMENT.md`](DEVELOPMENT.md).

The short version: `Conversation` is provider-agnostic. Each `Panelist` subclass owns its own `format_history()` and `respond()` methods, translating the shared history into whatever format its API requires. `DeepSeekPanelist` proved this out — adding it required zero changes to `Conversation`, `Session`, or `Moderator`, just a new `Panelist` subclass. A Gemini panelist would work the same way.

---

## Roadmap

Near term:
- Multi-target syntax (`Jean and Alan, ...`)
- Gemini panelist support (DeepSeek shipped first — see `panelist.py`)
- Persona authoring guide — how to write a YAML role for any domain or figure

Longer term:
- SQLite persistence — save and resume conversations
- Slack integration as a multi-user interface
- Web UI
- Speech layer (TTS for AI voices, STT for human participants)

---

## Dependencies

```
pip install anthropic openai pyyaml
```

`openai` powers `DeepSeekPanelist` (DeepSeek's API is OpenAI-SDK-compatible) — skip it if you're only running Claude and human panelists.

---

## License

MIT

---

*Feedback welcome — open an issue or reach out directly.*
