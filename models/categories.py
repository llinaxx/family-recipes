"""Класс Category — категория блюд."""


class Category:
    """Категория блюд."""

    def __init__(self, category_id: int, name: str, description: str = "") -> None:
        self.id = category_id
        self.name = name
        self.description = description

    def __str__(self) -> str:
        return f"Категория «{self.name}»"

    @classmethod
    def from_data(cls, data: dict) -> "Category":
        """Создать категорию из словаря."""
        return cls(
            category_id=data["id"],
            name=data["name"],
            description=data.get("description", ""),
        )

    def to_data(self) -> dict:
        """Преобразовать в словарь для JSON."""
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
        }
