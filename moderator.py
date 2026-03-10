from models import Prompt, Statement, AddGuestAction, DropGuestAction

STATEMENT_PREFIX = "//"

class Moderator:
    def __init__(self, name: str):
        self.name = name

    def compose_action(self, raw: str, current_target: list | str,
                      panelists: list) -> Prompt | Statement | None:

        raw = raw.strip()

        if raw.lower() in ("/quit", "/exit"):
            return None

        if raw.lower().startswith("/add_guest"):
            parts = raw.split(maxsplit=2)
            if len(parts) >= 3:
                return AddGuestAction(name=parts[1], role_name=parts[2].lower())
            print("[System]: Usage: /add_guest Name role")
            return Prompt(content="", directed_at=current_target)

        if raw.lower().startswith("/drop_guest"):
            parts = raw.split(maxsplit=1)
            if len(parts) >= 2:
                return DropGuestAction(name=parts[1])
            print("[System]: Usage: /drop_guest Name")
            return Prompt(content="", directed_at=current_target)

        if raw.startswith(STATEMENT_PREFIX):
            content = raw[len(STATEMENT_PREFIX):].strip()
            return Statement(content=content)

        if raw.lower().startswith("/all"):
            content = raw[4:].strip()
            return Prompt(
                content=content if content else raw,
                directed_at="all"
            )

        for panelist in panelists:
            if raw.lower().startswith(panelist.name.lower() + ",") or \
               raw.lower().startswith(panelist.name.lower() + " "):
                content = raw[len(panelist.name):].lstrip(", ").strip()
                return Prompt(
                    content=content,
                    directed_at=[panelist]
                )

        return Prompt(
            content=raw,
            directed_at=current_target
        )

    def __repr__(self):
        return f"Moderator(name={self.name!r})"