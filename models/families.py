"""Класс Family — семья."""
from typing import List
from .members import Member


class Family:
    """Семья — группа пользователей с общими рецептами."""

    def __init__(self, family_id: int, name: str, created_at: str) -> None:
        self.id = family_id
        self.name = name
        self.created_at = created_at
        self.members: List[Member] = []

    def add_member(self, member: Member) -> None:
        """Добавить участника в семью."""
        self.members.append(member)

    def __str__(self) -> str:
        return f"Семья «{self.name}» ({len(self.members)} участников)"

    @classmethod
    def from_data(cls, data: dict) -> "Family":
        """Создать семью из словаря."""
        return cls(
            family_id=data["id"],
            name=data["name"],
            created_at=data["created_at"],
        )

    def to_data(self) -> dict:
        """Преобразовать в словарь для JSON."""
        return {
            "id": self.id,
            "name": self.name,
            "created_at": self.created_at,
        }
