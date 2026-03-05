from models import Prompt, Statement, Turn
from conversation import Conversation
from moderator import Moderator

def resolve_recipients(prompt: Prompt, panelists: list) -> list:
    if prompt.directed_at == "all":
        return panelists
    return [p for p in panelists if p in prompt.directed_at]

class Session:
    def __init__(self, conversation: Conversation, moderator: Moderator):
        self.conversation = conversation
        self.moderator = moderator
        self.current_target = "all"

    def target_name(self) -> str:
        if self.current_target == "all":
            return "all"
        return self.current_target[0].name

    def handle_statement(self, action: Statement):
        turn = Turn(speaker=self.moderator, content=action.content)
        self.conversation.add_turn(turn)
        print(f"\n[{self.moderator.name}]: {action.content}\n")

    def handle_broadcast(self, action: Prompt):
        if self.conversation.has_pending():
            print(f"\n[Warning]: "
                  f"{self.conversation.pending_names()} "
                  f"haven't responded yet. "
                  f"Discard pending prompt? (y/n): ", end="")
            confirm = input().strip().lower()
            if confirm != "y":
                return
        self.conversation.clear_pending()
        self.conversation.broadcast(action)
        self.conversation.add_turn(
            Turn(speaker=self.moderator, content=action.content)
        )
        print(f"\n[{self.moderator.name} → all]: {action.content}\n")

    def handle_directed(self, action: Prompt):
        panelist = action.directed_at[0]

        if self.conversation.pending_prompt and \
           panelist in self.conversation.pending_respondents:
            turn = panelist.respond(
                self.conversation.history,
                self.conversation.pending_prompt
            )
            self.conversation.add_turn(turn)
            self.conversation.record_response(panelist)
            print(f"\n[{panelist.name}]: {turn.content}\n")

            if not self.conversation.has_pending():
                print("[System]: All panelists have responded.\n")
        else:
            self.current_target = action.directed_at
            turn = panelist.respond(
                self.conversation.history,
                action
            )
            self.conversation.add_turn(turn)
            print(f"\n[{panelist.name}]: {turn.content}\n")

    def run(self):
        print(f"\n[System]: Session started. "
              f"Panelists: "
              f"{', '.join(p.name for p in self.conversation.panelists)}\n"
              f"Type // to make a statement, "
              f"/all to address everyone, "
              f"/quit to exit.\n")

        while True:
            try:
                raw = input(f"[{self.moderator.name} "
                        f"→ {self.target_name()}]: ").strip()
            except (EOFError, KeyboardInterrupt):
                print("\n[System]: Session ended.")
                break

            if not raw:
                continue  # ignore empty input, re-prompt
            
            action = self.moderator.compose_action(
                raw,
                self.current_target,
                self.conversation.panelists
            )
            if action is None:
                print("\n[System]: Session ended.")
                break
            elif isinstance(action, Statement):
                self.handle_statement(action)
            elif isinstance(action, Prompt):
                if action.directed_at == "all":
                    self.handle_broadcast(action)
                else:
                    self.handle_directed(action)

            if self.conversation.has_pending():
                print(f"[Pending]: "
                      f"{self.conversation.pending_names()} "
                      f"haven't responded yet.\n")

    def __repr__(self):
        return (f"Session(moderator={self.moderator.name!r}, "
                f"conversation={self.conversation!r})")