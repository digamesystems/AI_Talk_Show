import yaml
from pathlib import Path

ROLES_DIR = Path(__file__).parent / "roles"

def load_role(role_name: str) -> dict:
    path = ROLES_DIR / f"{role_name}.yaml"
    if not path.exists():
        raise FileNotFoundError(
            f"Role '{role_name}' not found in {ROLES_DIR}"
        )
    with open(path) as f:
        return yaml.safe_load(f)

def list_roles() -> list[str]:
    return sorted(p.stem for p in ROLES_DIR.glob("*.yaml"))

def get_prompt(role_data: dict, model_key: str = None) -> str:
    if model_key:
        specific_key = f"{model_key}_prompt"
        if specific_key in role_data:
            return role_data[specific_key]
    return role_data["prompt"]