"""Класс Member — участник семьи."""


class Member:
    """Участник семьи."""

    def __init__(self, member_id: int, name: str, role: str) -> None:
        self.id = member_id
        self.name = name
        self.role = role

    def is_admin(self) -> bool:
        """Проверить, является ли участник администратором."""
        return self.role == "admin"

    def __str__(self) -> str:
        return f"{self.name} ({self.role})"

    @classmethod
    def from_data(cls, data: dict) -> "Member":
        """Создать участника из словаря."""
        return cls(
            member_id=data["id"],
            name=data["name"],
            role=data["role"],
        )

    def to_data(self) -> dict:
        """Преобразовать в словарь для JSON."""
        return {
            "id": self.id,
            "name": self.name,
            "role": self.role,
        }
