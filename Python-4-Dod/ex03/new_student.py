import random
import string
from dataclasses import dataclass, field


def generate_id() -> str:
    """Generate a random 15-character lowercase string."""
    return "".join(random.choices(string.ascii_lowercase, k=15))


@dataclass
class Student:
    """A student with a name, surname, status, login, and a unique ID."""

    name: str
    surname: str
    is_active: bool = True
    login: str = field(init=False)
    id: str = field(init=False, default_factory=generate_id)

    def __post_init__(self) -> str:
        self.login = f"{self.name[0].upper()}{self.surname.lower()}"
