"""View-функции приложения recipes."""
from django.shortcuts import render

from storage import load_recipes, load_members, load_categories


def _load_recipes():
    """Загрузить рецепты с авторами и категориями."""
    members = load_members()
    categories = load_categories()
    return load_recipes(members, categories)


def recipes(request):
    """Список рецептов."""
    context = {
        "recipes": _load_recipes(),
    }
    return render(request, "recipes/recipe_list.html", context)


def recipe_detail(request, recipe_id):
    """Карточка рецепта."""
    recipes_list = _load_recipes()
    recipe = next((r for r in recipes_list if r.id == recipe_id), None)

    context = {
        "recipe": recipe,
    }
    return render(
        request,
        "recipes/recipe_detail.html",
        context,
        status=404 if recipe is None else 200,
    )
