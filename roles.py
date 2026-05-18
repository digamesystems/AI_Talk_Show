import yaml
from pathlib import Path

ROLES_DIR = Path(__file__).parent / "roles"

def load_role(role_name: str) -> dict:
    path = ROLES_DIR / f"{role_name}.yaml"
    if not path.exists():
        raise FileNotFoundError(
            f"Role '{role_name}' not found in {ROLES_DIR}"
        )
    with open(path, encoding="utf-8") as f:
        return yaml.safe_load(f)

def list_roles() -> list[str]:
    return sorted(p.stem for p in ROLES_DIR.glob("*.yaml"))

def get_system_overrides(role_data: dict) -> dict:
    return role_data.get("system_overrides", {})

def render_structured_prompt(role_data: dict) -> str:
    parts = []

    identity = role_data.get("identity", {})
    if voice := identity.get("voice_description"):
        parts.append(f"Voice: {voice}\n")

    if core_beliefs := role_data.get("core_beliefs"):
        parts.append("PHILOSOPHICAL BEDROCK:")
        for key, value in core_beliefs.items():
            label = key.replace("_", " ").title()
            parts.append(f"  {label}: {value}")
        parts.append("")

    if triggers := role_data.get("dissonance_triggers"):
        parts.append("FAULT LINES — react sharply to these:")
        for key, value in triggers.items():
            label = key.replace("_", " ").title()
            parts.append(f"  {label}: {value}")
        parts.append("")

    if vocab := role_data.get("vocabulary_weights"):
        high = ", ".join(vocab.get("high", []))
        low = ", ".join(vocab.get("low", []))
        if high:
            parts.append(f"Vocabulary — use heavily: {high}")
        if low:
            parts.append(f"Avoid: {low}")
        parts.append("")

    if style := role_data.get("interaction_style"):
        parts.append("BEHAVIORAL RULES:")
        for rule in style:
            parts.append(f"  - {rule}")
        parts.append("")

    if friction := role_data.get("friction_directives"):
        parts.append("FRICTION RULES:")
        for rule in friction:
            parts.append(f"  - {rule}")

    return "\n".join(parts).strip()

def get_prompt(role_data: dict, model_key: str = None) -> str:
    if "core_beliefs" in role_data:
        return render_structured_prompt(role_data)
    if model_key:
        specific_key = f"{model_key}_prompt"
        if specific_key in role_data:
            return role_data[specific_key]
    return role_data.get("prompt", "")
