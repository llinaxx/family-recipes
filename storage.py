"""Загрузка и сохранение данных проекта в JSON."""
import json
import os
from models import Family, Member, Category, Recipe

DATA_DIR = "data"


def load_json(filename: str) -> list:
    """Загрузить список словарей из JSON."""
    path = os.path.join(DATA_DIR, filename)
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def save_json(filename: str, data: list) -> None:
    """Сохранить список словарей в JSON."""
    os.makedirs(DATA_DIR, exist_ok=True)
    path = os.path.join(DATA_DIR, filename)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def load_families() -> list:
    """Загрузить семьи как объекты."""
    return [Family.from_data(d) for d in load_json("families.json")]


def load_members() -> list:
    """Загрузить участников как объекты."""
    return [Member.from_data(d) for d in load_json("members.json")]


def load_categories() -> list:
    """Загрузить категории как объекты."""
    return [Category.from_data(d) for d in load_json("categories.json")]


def load_recipes(members: list, categories: list) -> list:
    """Загрузить рецепты, связав с участниками и категориями."""
    mem_by_id = {m.id: m for m in members}
    cat_by_id = {c.id: c for c in categories}
    recipes = []
    for d in load_json("recipes.json"):
        author = mem_by_id.get(d.get("author_id"))
        category = cat_by_id.get(d.get("category_id"))
        if author and category:
            recipes.append(Recipe.from_data(d, author, category))
    return recipes


def save_all(
    families: list,
    members: list,
    categories: list,
    recipes: list,
) -> None:
    """Сохранить все коллекции объектов в JSON."""
    save_json("families.json", [f.to_data() for f in families])
    save_json("members.json", [m.to_data() for m in members])
    save_json("categories.json", [c.to_data() for c in categories])
    save_json("recipes.json", [r.to_data() for r in recipes])
