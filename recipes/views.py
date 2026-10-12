"""View-функции приложения recipes."""
from django.http import HttpResponse

from homepage.views import page
from storage import load_recipes, load_members, load_categories


def _load_recipes():
    """Загрузить рецепты с авторами и категориями."""
    members = load_members()
    categories = load_categories()
    return load_recipes(members, categories)


def recipes(request):
    """Список рецептов."""
    items = ""
    for r in _load_recipes():
        fav = "★ " if r.is_favorite else ""
        text = (
            f"{fav}{r.title} — {r.cooking_time} мин "
            f"({r.category.name}, автор: {r.author.name})"
        )
        items += f'<li class="list-group-item">{text}</li>'
    content = f"""
    <h1>Рецепты</h1>
    <ul class="list-group">{items}</ul>
    """
    return HttpResponse(page("Family Recipes — рецепты", content))


def recipe_detail(request, recipe_id):
    """Карточка рецепта."""
    recipes_list = _load_recipes()
    recipe = next((r for r in recipes_list if r.id == recipe_id), None)

    if recipe is None:
        content = """
        <h1 class="text-danger">Рецепт не найден</h1>
        <a href="/recipes/" class="btn btn-outline-secondary">
            ← к списку рецептов
        </a>
        """
        return HttpResponse(
            page("Рецепт не найден", content),
            status=404,
        )

    fav_badge = (
        '<span class="badge bg-warning text-dark">Избранный</span>'
        if recipe.is_favorite
        else '<span class="badge bg-secondary">Не избранный</span>'
    )
    quick_badge = (
        '<span class="badge bg-success">Быстрый</span>'
        if recipe.is_quick()
        else '<span class="badge bg-info text-dark">Долгий</span>'
    )

    content = f"""
    <div class="card">
        <div class="card-body">
            <h5 class="card-title">{recipe.title}</h5>
            <p class="card-text"><strong>ID:</strong> {recipe.id}</p>
            <p class="card-text"><strong>Автор:</strong> {recipe.author.name}</p>
            <p class="card-text"><strong>Категория:</strong> {recipe.category.name}</p>
            <p class="card-text"><strong>Время готовки:</strong> {recipe.cooking_time} мин</p>
            <p class="card-text"><strong>Сложность:</strong> {recipe.difficulty}</p>
            <p class="card-text">{quick_badge} {fav_badge}</p>
            <a href="/recipes/" class="btn btn-outline-secondary">
                ← к списку рецептов
            </a>
        </div>
    </div>
    """
    return HttpResponse(page(recipe.title, content))
