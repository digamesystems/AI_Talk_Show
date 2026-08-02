import sys
import yaml
from pathlib import Path

from conversation import Conversation
from moderator import Moderator
from panelist import ClaudePanelist, DeepSeekPanelist, HumanPanelist
from roles import list_roles, load_role
from session import Session

# Windows consoles default to cp1252, which can't print names like "Bashō" —
# force UTF-8 so role names with non-ASCII characters don't crash the session.
sys.stdout.reconfigure(encoding="utf-8")

PANELS_DIR = Path(__file__).parent / "panels"


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


def add_deepseek_panelist(moderator_name: str) -> DeepSeekPanelist:
    name = input("  Display name: ").strip() or "DeepSeek"
    handle = name.lower().replace(" ", "_")
    role_name = prompt_role_selection()
    return DeepSeekPanelist(
        name=name,
        handle=handle,
        role_name=role_name,
        moderator_name=moderator_name
    )


def add_human_panelist() -> HumanPanelist:
    name = input("  Display name: ").strip() or "Guest"
    role = input(f"  {name}'s role description: ").strip() or "Guest Panelist"
    return HumanPanelist(name=name, role=role)


def list_panel_files() -> list[str]:
    if not PANELS_DIR.exists():
        return []
    return sorted(p.stem for p in PANELS_DIR.glob("*.yaml"))


def load_panel_file(name: str) -> dict:
    path = PANELS_DIR / f"{name}.yaml"
    if not path.exists():
        raise FileNotFoundError(f"Panel preset '{name}' not found in {PANELS_DIR}")
    with open(path, encoding="utf-8") as f:
        return yaml.safe_load(f)


def prompt_panel_file_selection() -> str | None:
    files = list_panel_files()
    if not files:
        print("  No panel presets found in panels/.")
        return None
    print("\nAvailable panel presets:")
    for i, name in enumerate(files, 1):
        print(f"  {i}. {name}")
    print()
    while True:
        choice = input("  Select preset (name or number): ").strip().lower()
        if choice.isdigit():
            idx = int(choice) - 1
            if 0 <= idx < len(files):
                return files[idx]
        else:
            match = next((f for f in files if f.lower() == choice), None)
            if match:
                return match
        print("  Invalid selection. Try again.")


def build_panelist_from_preset(entry: dict, moderator_name: str):
    kind = entry.get("type", "claude").lower()
    name = entry["name"]
    if kind == "human":
        role = entry.get("role_description", "Guest Panelist")
        return HumanPanelist(name=name, role=role)
    role_name = entry.get("role", "Default")
    panelist_class = DeepSeekPanelist if kind == "deepseek" else ClaudePanelist
    return panelist_class(
        name=name,
        handle=name.lower().replace(" ", "_"),
        role_name=role_name,
        moderator_name=moderator_name
    )


def create_session_from_file() -> Session:
    preset_name = prompt_panel_file_selection()
    if preset_name is None:
        print("  Falling back to manual setup.")
        return create_session_by_hand()
    preset = load_panel_file(preset_name)

    moderator_name = preset.get("moderator_name") \
        or input("Moderator name: ").strip() or "Host"
    moderator = Moderator(name=moderator_name)

    topic = preset.get("topic") or (input("Opening topic (optional): ").strip() or None)
    conversation = Conversation(topic=topic, active_window=30)

    for entry in preset.get("panelists", []):
        panelist = build_panelist_from_preset(entry, moderator_name)
        handle = panelist.name.lower().replace(" ", "_")
        if any(p.handle == handle for p in conversation.panelists):
            print(f"  Skipping duplicate panelist name '{panelist.name}'.")
            continue
        conversation.add_panelist(panelist)
        print(f"  Added {panelist.name} ({panelist.role})")

    if not conversation.panelists:
        print("  No panelists loaded from preset — falling back to manual setup.")
        return create_session_by_hand()

    return Session(conversation=conversation, moderator=moderator)


def create_session() -> Session:
    print("\n=== Panel Discussion Setup ===\n")

    mode = input("Build panel by hand or load from file? (hand/file) [hand]: "
                ).strip().lower()
    if mode.startswith("f"):
        return create_session_from_file()
    return create_session_by_hand()


def create_session_by_hand() -> Session:
    moderator_name = input("Moderator name: ").strip() or "Host"
    moderator = Moderator(name=moderator_name)

    topic = input("Opening topic (optional): ").strip() or None
    conversation = Conversation(topic=topic, active_window=30)

    print("\nAdd panelists (minimum 1):")
    while True:
        print(f"\n  Panelist {len(conversation.panelists) + 1}:")
        kind = input("  Type (claude/deepseek/human): ").strip().lower()
        if kind == "claude":
            panelist = add_claude_panelist(moderator_name)
        elif kind == "deepseek":
            panelist = add_deepseek_panelist(moderator_name)
        elif kind == "human":
            panelist = add_human_panelist()
        else:
            print("  Invalid type. Enter 'claude', 'deepseek', or 'human'.")
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
    print("Type /help once the session starts to see the full command list.\n")

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
    from pathlib import Path
    transcripts_dir = Path(__file__).parent / "transcripts"
    transcripts_dir.mkdir(exist_ok=True)
    filename = transcripts_dir / f"transcript_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
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

            if turn.interjection:
                label = f"[{speaker} Interjects]"
            elif turn.speaker == session.moderator and \
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