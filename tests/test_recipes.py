from models.recipes import (
    add_recipe,
    find_recipes_by_title,
    filter_recipes_by_time,
    sort_recipes_by_time,
    get_recipes_stats,
)


def test_add_recipe():
    recipes = []
    add_recipe(recipes, "Борщ", 1, 1, 90, "средне")
    assert len(recipes) == 1
    assert recipes[0]["title"] == "Борщ"
    assert recipes[0]["is_favorite"] is False


def test_find_recipes_by_title():
    recipes = []
    add_recipe(recipes, "Борщ", 1, 1, 90, "средне")
    add_recipe(recipes, "Салат", 1, 2, 15, "легко")
    assert len(find_recipes_by_title(recipes, "бор")) == 1
    assert len(find_recipes_by_title(recipes, "САЛ")) == 1
    assert len(find_recipes_by_title(recipes, "пицца")) == 0


def test_filter_recipes_by_time():
    recipes = []
    add_recipe(recipes, "Борщ", 1, 1, 90, "средне")
    add_recipe(recipes, "Салат", 1, 2, 15, "легко")
    assert len(filter_recipes_by_time(recipes, 30)) == 1
    assert len(filter_recipes_by_time(recipes, 100)) == 2


def test_sort_recipes_by_time():
    recipes = []
    add_recipe(recipes, "Борщ", 1, 1, 90, "средне")
    add_recipe(recipes, "Салат", 1, 2, 15, "легко")
    sorted_recipes = sort_recipes_by_time(recipes)
    assert sorted_recipes[0]["title"] == "Салат"


def test_get_recipes_stats():
    recipes = []
    add_recipe(recipes, "Борщ", 1, 1, 90, "средне")
    add_recipe(recipes, "Салат", 1, 2, 30, "легко")
    stats = get_recipes_stats(recipes)
    assert stats["total"] == 2
    assert stats["avg_time"] == 60.0
    assert stats["favorites"] == 0


def test_empty_stats():
    stats = get_recipes_stats([])
    assert stats["total"] == 0
    assert stats["avg_time"] == 0
