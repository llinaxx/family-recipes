"""Главная страница и общий каркас HTML."""
from django.http import HttpResponse


def page(title: str, content: str) -> str:
    """Общий каркас HTML-страницы с Bootstrap 5.3."""
    bootstrap = (
        "https://cdn.jsdelivr.net/npm/bootstrap@5.3.3"
        "/dist/css/bootstrap.min.css"
    )
    return f"""<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>{title}</title>
    <link rel="stylesheet" href="{bootstrap}">
</head>
<body>
    <nav class="nav bg-light p-3 mb-4">
        <a class="nav-link" href="/">Главная</a>
        <a class="nav-link" href="/recipes/">Рецепты</a>
        <a class="nav-link" href="/categories/">Категории</a>
    </nav>
    <main class="container">{content}</main>
</body>
</html>"""


def index(request):
    """Главная страница."""
    content = """
    <h1 class="display-4">Family Recipes</h1>
    <p class="lead">Сервис для хранения кулинарных рецептов семьи.</p>
    <p>Основные разделы:</p>
    <a href="/recipes/" class="btn btn-primary me-2">Рецепты</a>
    <a href="/categories/" class="btn btn-secondary">Категории</a>
    """
    return HttpResponse(page("Family Recipes", content))


def page_not_found(request, exception):
    """Своя страница 404."""
    content = """
    <h1 class="text-danger">404 — страница не найдена</h1>
    <p>Проверьте адрес или вернитесь на главную.</p>
    <a href="/" class="btn btn-primary">На главную</a>
    """
    return HttpResponse(
        page("404 — страница не найдена", content),
        status=404,
    )
