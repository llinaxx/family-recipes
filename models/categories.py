from typing import List, Dict


def add_category(categories: List[Dict], name: str, description: str = "") -> Dict:
    """Добавить категорию."""
    category_id = len(categories) + 1
    category = {"id": category_id, "name": name, "description": description}
    categories.append(category)
    return category


def find_category_by_name(categories: List[Dict], name: str) -> Dict:
    """Найти категорию по названию."""
    for c in categories:
        if c["name"].lower() == name.lower():
            return c
    return {}
