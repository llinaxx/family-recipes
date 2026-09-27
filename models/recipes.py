"""Класс Recipe — кулинарный рецепт."""
from .members import Member
from .categories import Category


class Recipe:
    """Кулинарный рецепт."""

    def __init__(
        self,
        recipe_id: int,
        title: str,
        author: Member,
        category: Category,
        cooking_time: int,
        difficulty: str = "средне",
        is_favorite: bool = False,
    ) -> None:
        self.id = recipe_id
        self.title = title
        self.author = author
        self.category = category
        self.cooking_time = cooking_time
        self.difficulty = difficulty
        self.is_favorite = is_favorite

    def is_quick(self, threshold: int = 30) -> bool:
        """Проверить, быстрый ли рецепт."""
        return self.cooking_time <= threshold

    def mark_favorite(self) -> None:
        """Отметить рецепт как избранный."""
        self.is_favorite = True

    def __str__(self) -> str:
        fav = "★" if self.is_favorite else " "
        return (
            f"{fav} [{self.id}] {self.title} — {self.cooking_time} мин "
            f"({self.category.name}, автор: {self.author.name})"
        )

    @classmethod
    def from_data(cls, data: dict, author: Member, category: Category) -> "Recipe":
        """Создать рецепт из словаря, связав с автором и категорией."""
        return cls(
            recipe_id=data["id"],
            title=data["title"],
            author=author,
            category=category,
            cooking_time=data["cooking_time"],
            difficulty=data.get("difficulty", "средне"),
            is_favorite=data.get("is_favorite", False),
        )

    def to_data(self) -> dict:
        """Преобразовать в словарь для JSON."""
        return {
            "id": self.id,
            "title": self.title,
            "author_id": self.author.id,
            "category_id": self.category.id,
            "cooking_time": self.cooking_time,
            "difficulty": self.difficulty,
            "is_favorite": self.is_favorite,
        }
