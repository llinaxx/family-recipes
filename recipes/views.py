from django.shortcuts import render
from db.database import get_connection

def recipes(request):
    """Список рецептов из базы данных SQLite."""
    conn = get_connection()
    # Используем JOIN, чтобы сразу получить имена авторов и категорий
    recipes_data = conn.execute("""
        SELECT recipes.id, recipes.title, recipes.cooking_time, recipes.difficulty, recipes.is_favorite,
               categories.name AS category_name, members.name AS author_name
        FROM recipes
        JOIN categories ON recipes.category_id = categories.id
        JOIN members ON recipes.author_id = members.id
        ORDER BY recipes.title;
    """).fetchall()
    conn.close()
    
    return render(request, "recipes/recipe_list.html", {"recipes": recipes_data})

def recipe_detail(request, recipe_id):
    """Карточка рецепта из базы данных."""
    conn = get_connection()
    # Передаем recipe_id через параметр ? (защита от SQL-инъекций)
    recipe = conn.execute("""
        SELECT recipes.id, recipes.title, recipes.cooking_time, recipes.difficulty, recipes.is_favorite,
               categories.name AS category_name, members.name AS author_name
        FROM recipes
        JOIN categories ON recipes.category_id = categories.id
        JOIN members ON recipes.author_id = members.id
        WHERE recipes.id = ?;
    """, (recipe_id,)).fetchone()
    conn.close()
    
    return render(
        request, 
        "recipes/recipe_detail.html", 
        {"recipe": recipe},
        status=404 if recipe is None else 200
    )
