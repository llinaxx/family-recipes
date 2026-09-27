from typing import List, Dict


def add_recipe(recipes: List[Dict], title: str, author_id: int,
               category_id: int, cooking_time: int, difficulty: str) -> Dict:
    """Добавить рецепт в список."""
    recipe_id = len(recipes) + 1
    recipe = {
        "id": recipe_id,
        "title": title,
        "author_id": author_id,
        "category_id": category_id,
        "cooking_time": cooking_time,
        "difficulty": difficulty,
        "is_favorite": False,
    }
    recipes.append(recipe)
    return recipe


def find_recipes_by_title(recipes: List[Dict], query: str) -> List[Dict]:
    """Найти рецепты по подстроке названия."""
    return [r for r in recipes if query.lower() in r["title"].lower()]


def filter_recipes_by_time(recipes: List[Dict], max_time: int) -> List[Dict]:
    """Отобрать рецепты по времени готовки."""
    return [r for r in recipes if r["cooking_time"] <= max_time]


def sort_recipes_by_time(recipes: List[Dict]) -> List[Dict]:
    """Сортировка рецептов по времени готовки."""
    return sorted(recipes, key=lambda r: r["cooking_time"])


def get_recipes_stats(recipes: List[Dict]) -> Dict:
    """Статистика: всего рецептов, среднее время, избранных."""
    if not recipes:
        return {"total": 0, "avg_time": 0, "favorites": 0}
    total = len(recipes)
    avg_time = sum(r["cooking_time"] for r in recipes) / total
    favorites = sum(1 for r in recipes if r["is_favorite"])
    return {"total": total, "avg_time": round(avg_time, 1), "favorites": favorites}
