from dataclasses import dataclass, field
from datetime import datetime
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from panelist import Panelist

@dataclass
class Statement:
    content: str

@dataclass
class Prompt:
    content: str
    directed_at: list | str  # list of Panelist or "all"
    response_order: list | None = None

@dataclass
class Turn:
    speaker: object
    content: str
    timestamp: datetime = field(default_factory=datetime.now)
    in_response_to: Prompt | Statement | None = None

@dataclass
class AddGuestAction:
    name: str
    role_name: str     # role yaml name, or "human"

@dataclass
class DropGuestAction:
    name: str