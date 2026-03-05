from models import Prompt, Statement, Turn

class Conversation:
    def __init__(self, topic: str = None, active_window: int = 20):
        self.topic = topic
        self.panelists = []
        self.history = []        # full record — never truncated
        self.summary = None
        self.active_window = active_window  # API context window only
        self.pending_prompt = None
        self.pending_respondents = []
        
    def add_panelist(self, panelist):
        self.panelists.append(panelist)

    def add_turn(self, turn: Turn):
        self.history.append(turn)

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