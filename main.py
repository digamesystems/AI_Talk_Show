from conversation import Conversation
from moderator import Moderator
from panelist import ClaudePanelist, HumanPanelist
from roles import list_roles, load_role
from session import Session


def prompt_role_selection() -> str:
    roles = list_roles()
    print("\nAvailable roles:")
    for i, role_name in enumerate(roles, 1):
        role_data = load_role(role_name)
        print(f"  {i}. {role_name} — {role_data['description']}")
    print()
    while True:
        choice = input("  Select role (name or number, Enter for default): "
                       ).strip().lower()
        if not choice:
            return "Default"
        if choice.isdigit():
            idx = int(choice) - 1
            if 0 <= idx < len(roles):
                return roles[idx]
        else:
            match = next((r for r in roles if r.lower() == choice), None)
            if match:
                return match
        print(f"  Invalid selection. Try again.")


def add_claude_panelist(moderator_name: str) -> ClaudePanelist:
    name = input("  Display name: ").strip() or "Claude"
    handle = name.lower().replace(" ", "_")
    role_name = prompt_role_selection()
    return ClaudePanelist(
        name=name,
        handle=handle,
        role_name=role_name,
        moderator_name=moderator_name
    )


def add_human_panelist() -> HumanPanelist:
    name = input("  Display name: ").strip() or "Guest"
    role = input(f"  {name}'s role description: ").strip() or "Guest Panelist"
    return HumanPanelist(name=name, role=role)


def create_session() -> Session:
    print("\n=== Panel Discussion Setup ===\n")

    moderator_name = input("Moderator name: ").strip() or "Host"
    moderator = Moderator(name=moderator_name)

    topic = input("Opening topic (optional): ").strip() or None
    conversation = Conversation(topic=topic, active_window=30)

    print("\nAdd panelists (minimum 1):")
    while True:
        print(f"\n  Panelist {len(conversation.panelists) + 1}:")
        kind = input("  Type (claude/human): ").strip().lower()
        if kind == "claude":
            panelist = add_claude_panelist(moderator_name)
        elif kind == "human":
            panelist = add_human_panelist()
        else:
            print("  Invalid type. Enter 'claude' or 'human'.")
            continue

        handle = panelist.name.lower().replace(" ", "_")
        if any(p.handle == handle for p in conversation.panelists):
            print(f"  A panelist named '{panelist.name}' is already in the session. Choose a different name.")
            continue

        conversation.add_panelist(panelist)
        print(f"  Added {panelist.name} ({panelist.role})")

        if len(conversation.panelists) >= 1:
            another = input("\nAdd another panelist? (y/n): ").strip().lower()
            if another != "y":
                break

    return Session(conversation=conversation, moderator=moderator)


def main():
    print("=== Panel Discussion Console ===")
    print("Commands:")
    print("  //...        Statement (no response expected)")
    print("  /all ...     Broadcast to all panelists")
    print("  Name, ...    Direct to named panelist")
    print("  /quit        End session")
    print("  .            Send (terminate multi-line input)\n")

    session = create_session()
    session.run()

    print(f"\n=== Session Summary ===")
    print(f"Moderator : {session.moderator.name}")
    print(f"Panelists : "
          f"{', '.join(p.name for p in session.conversation.panelists)}")
    print(f"Topic     : {session.conversation.topic or 'Open discussion'}")
    print(f"Turns     : {len(session.conversation.history)}\n")

    save = input("Save transcript? (y/n): ").strip().lower()
    if save == "y":
        save_transcript(session)


def save_transcript(session: Session):
    from datetime import datetime
    filename = f"transcript_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(f"=== Panel Discussion Transcript ===\n")
        f.write(f"Date      : {datetime.now().strftime('%Y-%m-%d %H:%M')}\n")
        f.write(f"Moderator : {session.moderator.name}\n")
        f.write(f"Panelists : "
                f"{', '.join(p.name for p in session.conversation.panelists)}\n")
        f.write(f"Topic     : "
                f"{session.conversation.topic or 'Open discussion'}\n")
        f.write(f"{'=' * 40}\n\n")
        for turn in session.conversation.history:
            speaker = turn.speaker.name

            if turn.speaker == session.moderator and \
            turn.in_response_to is not None and \
            hasattr(turn.in_response_to, 'directed_at'):
                directed = turn.in_response_to.directed_at
                if directed != "all" and isinstance(directed, list):
                    target = directed[0].name
                    label = f"[{speaker} → {target}]"
                else:
                    label = f"[{speaker}]"
            else:
                label = f"[{speaker}]"

            f.write(f"{label}: {turn.content}\n\n")

    print(f"\n[System]: Transcript saved to {filename}\n")
if __name__ == "__main__":
    main()