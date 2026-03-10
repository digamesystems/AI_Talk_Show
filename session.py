from models import Prompt, Statement, Turn, AddGuestAction, DropGuestAction
from conversation import Conversation, summarize_history
from moderator import Moderator
from panelist import ClaudePanelist, HumanPanelist


def read_prompt(prefix: str) -> str:
    """Read one or more lines until a line containing only '.' is entered."""
    lines = []
    line = input(prefix)
    while line != ".":
        lines.append(line)
        line = input("")
    return "\n".join(lines)


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
            # Directed follow-up to a pending broadcast — record the moderator prompt
            moderator_turn = Turn(
                speaker=self.moderator,
                content=action.content,
                in_response_to=action
            )
            self.conversation.add_turn(moderator_turn)
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
            # Regular directed prompt — record it first
            moderator_turn = Turn(
                speaker=self.moderator,
                content=action.content,
                in_response_to=action
            )
            self.conversation.add_turn(moderator_turn)

            self.current_target = action.directed_at
            turn = panelist.respond(
                self.conversation.history,
                action
            )
            self.conversation.add_turn(turn)
            print(f"\n[{panelist.name}]: {turn.content}\n")

    def handle_add_guest(self, action: AddGuestAction):
        name = action.name
        role_name = action.role_name
        handle = name.lower().replace(" ", "_")

        if any(p.handle == handle for p in self.conversation.panelists):
            print(f"\n[System]: A panelist named '{name}' is already in the session.\n")
            return

        onboarding_summary = None
        if self.conversation.history:
            print(f"\n[System]: Generating onboarding summary for {name}...", flush=True)
            client_ref = next(
                (p.client for p in self.conversation.panelists
                 if isinstance(p, ClaudePanelist)), None
            )
            if client_ref:
                onboarding_summary = summarize_history(
                    self.conversation.history, client_ref
                )

        if role_name == "human":
            panelist = HumanPanelist(name=name, role="Human Guest")
            if onboarding_summary:
                print(f"\n[System -- for {name}]: Here is what was discussed before you joined:\n")
                print(onboarding_summary + "\n")
        else:
            panelist = ClaudePanelist(
                name=name,
                handle=handle,
                role_name=role_name,
                moderator_name=self.moderator.name
            )
            panelist.onboarding_summary = onboarding_summary

        self.conversation.add_panelist(panelist, onboarding_summary=onboarding_summary)
        print(f"\n[System]: {name} ({role_name}) has joined the panel.\n")

    def handle_drop_guest(self, action: DropGuestAction):
        name = action.name
        panelist = next(
            (p for p in self.conversation.panelists
             if p.name.lower() == name.lower()), None
        )
        if not panelist:
            print(f"\n[System]: No panelist named '{name}' found.\n")
            return

        if panelist in self.conversation.pending_respondents:
            print(f"\n[Warning]: {name} has a pending response. Drop anyway? (y/n): ", end="")
            if input().strip().lower() != "y":
                return

        farewell = input(f"\nFarewell words for {name} (or Enter to skip): ").strip()
        if farewell:
            turn = Turn(speaker=self.moderator, content=farewell)
            self.conversation.add_turn(turn)
            print(f"\n[{self.moderator.name}]: {farewell}\n")

        self.conversation.panelists.remove(panelist)
        if panelist in self.conversation.pending_respondents:
            self.conversation.pending_respondents.remove(panelist)
        print(f"\n[System]: {name} has left the panel.\n")

    def run(self):
        print(f"\n[System]: Session started. "
              f"Panelists: "
              f"{', '.join(p.name for p in self.conversation.panelists)}\n"
              f"Type // to make a statement, "
              f"/all to address everyone, "
              f"/quit to exit.\n")

        while True:
            try:
                raw = read_prompt(f"[{self.moderator.name} "
                                  f"→ {self.target_name()}]: ").strip()
            except (EOFError, KeyboardInterrupt):
                print("\n[System]: Session ended.")
                break

            if not raw:
                continue

            action = self.moderator.compose_action(
                raw,
                self.current_target,
                self.conversation.panelists
            )
            if action is None:
                print("\n[System]: Session ended.")
                break
            elif isinstance(action, AddGuestAction):
                self.handle_add_guest(action)
            elif isinstance(action, DropGuestAction):
                self.handle_drop_guest(action)
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