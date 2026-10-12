"""View-функции приложения categories."""
from django.shortcuts import render

from storage import load_categories, load_recipes, load_members


def _load_all():
    """Загрузить категории и связанные рецепты."""
    categories = load_categories()
    members = load_members()
    recipes = load_recipes(members, categories)
    return categories, recipes


def categories(request):
    """Список категорий."""
    cats, _ = _load_all()
    context = {
        "categories": cats,
    }
    return render(request, "categories/category_list.html", context)


def category_detail(request, category_id):
    """Карточка категории с рецептами."""
    cats, recipes = _load_all()
    category = next((c for c in cats if c.id == category_id), None)

    context = {
        "category": category,
        "recipes": recipes,
    }
    return render(
        request,
        "categories/category_detail.html",
        context,
        status=404 if category is None else 200,
    )
