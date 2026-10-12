"""View-функции приложения categories."""
from django.http import HttpResponse

from homepage.views import page
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
    items = ""
    for c in cats:
        text = f"{c.name} — {c.description}"
        items += f'<li class="list-group-item">{text}</li>'
    content = f"""
    <h1>Категории</h1>
    <ul class="list-group">{items}</ul>
    """
    return HttpResponse(page("Family Recipes — категории", content))


def category_detail(request, category_id):
    """Карточка категории с рецептами в ней."""
    cats, recipes = _load_all()
    category = next((c for c in cats if c.id == category_id), None)

    if category is None:
        content = """
        <h1 class="text-danger">Категория не найдена</h1>
        <a href="/categories/" class="btn btn-outline-secondary">
            ← к списку категорий
        </a>
        """
        return HttpResponse(
            page("Категория не найдена", content),
            status=404,
        )

    items = ""
    for r in recipes:
        if r.category.id == category.id:
            items += (
                f'<li class="list-group-item">'
                f'{r.title} — {r.cooking_time} мин'
                f'</li>'
            )

    if not items:
        items = (
            '<li class="list-group-item">'
            'Рецептов в этой категории нет.'
            '</li>'
        )

    content = f"""
    <h1>Категория: {category.name}</h1>
    <p>{category.description}</p>
    <h3>Рецепты:</h3>
    <ul class="list-group">{items}</ul>
    <a href="/categories/" class="btn btn-outline-secondary mt-3">
        ← к списку категорий
    </a>
    """
    return HttpResponse(page(category.name, content))
