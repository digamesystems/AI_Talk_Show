import anthropic
from dataclasses import dataclass, field
from models import Prompt, Statement, Turn


def summarize_history(history: list, client: anthropic.Anthropic) -> str:
    """Summarize a list of Turns into a concise narrative briefing.

    Lossless on: names, facts, dates, concessions, unanswered questions.
    Lossy on: rhetorical scaffolding, restatements, extended metaphors.
    """
    lines = []
    for turn in history:
        name = getattr(turn.speaker, "name", str(turn.speaker))
        lines.append(f"[{name}]: {turn.content}")
    transcript = "\n\n".join(lines)

    prompt = f"""Below is a transcript of a panel discussion. Write a concise summary (150 words or fewer).

Be LOSSLESS about:
- Names, places, dates, and factual claims introduced
- Explicit concessions or position changes by any speaker
- Questions that were raised but not answered
- New participants introduced and when they joined

Be LOSSY about:
- Philosophical elaboration and rhetorical scaffolding
- Points that restate something already said
- Extended metaphors and illustrative examples

Transcript:
{transcript}

Summary:"""

    response = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=300,
        messages=[{"role": "user", "content": prompt}]
    )
    return response.content[0].text.strip()


@dataclass
class PanelistMeta:
    joined_at: int                    # turn index when panelist joined
    onboarding_summary: str | None = None


class Conversation:
    def __init__(self, topic: str = None, active_window: int = 30):
        self.topic = topic
        self.panelists = []
        self.history = []             # full record — never truncated
        self.pinned = []              # always in context, immune to summarization
        self.summary = None
        self.panelist_meta: dict[str, PanelistMeta] = {}
        self.active_window = active_window  # API context window only
        self.pending_prompt = None
        self.pending_respondents = []

    def add_panelist(self, panelist, onboarding_summary: str | None = None):
        self.panelists.append(panelist)
        self.panelist_meta[panelist.handle] = PanelistMeta(
            joined_at=len(self.history),
            onboarding_summary=onboarding_summary
        )

    def add_turn(self, turn: Turn):
        self.history.append(turn)

    def pin_turn(self, turn: Turn):
        if turn not in self.pinned:
            self.pinned.append(turn)

    def has_pending(self) -> bool:
        return self.pending_prompt is not None \
               and len(self.pending_respondents) > 0

    def pending_names(self) -> str:
        return ", ".join(p.name for p in self.pending_respondents)

    def broadcast(self, prompt: Prompt):
        self.pending_prompt = prompt
        self.pending_respondents = list(self.panelists)

    def record_response(self, panelist):
        if panelist in self.pending_respondents:
            self.pending_respondents.remove(panelist)
        if not self.pending_respondents:
            self.pending_prompt = None

    def clear_pending(self):
        self.pending_prompt = None
        self.pending_respondents = []

    def __repr__(self):
        return (f"Conversation(topic={self.topic!r}, "
                f"turns={len(self.history)}, "
                f"pending={self.pending_names() or None})")