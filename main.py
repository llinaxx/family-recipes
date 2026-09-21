"""
Сервис управления кулинарными рецептами семьи.
"""

from datetime import date

# --- Данные семьи ---
family_name = "Гревцевы"
family_members_count = 3
family_created_at = date(2026, 9, 21)

# --- Данные участников ---
member_1_name = "Папа"
member_1_role = "member"

member_2_name = "Мама"
member_2_role = "member"

member_3_name = "Дочь"
member_3_role = "admin"

# --- Данные категории ---
category_name = "Суп"
category_description = "Первые блюда"

# --- Данные рецепта ---
recipe_title = "Борщ"
recipe_author = member_2_name
recipe_category = category_name
recipe_cooking_time = 90       # минуты
recipe_servings = 6
recipe_is_family_favorite = True


# --- Функции ---

def get_family_info(name, members_count, created_at):
    """Вернуть строку с информацией о семье."""
    return f"Семья «{name}» — {members_count} участника, создана {created_at}"


def get_recipe_info(title, author, category):
    """Вернуть строку с основной информацией о рецепте."""
    return f"Рецепт «{title}» (автор: {author}, категория: {category})"


def check_cooking_time(time_minutes):
    """Классифицировать рецепт по времени готовки."""
    if time_minutes <= 30:
        return "Быстрый рецепт (до 30 минут)"
    elif time_minutes <= 60:
        return "Среднее время готовки (30–60 минут)"
    return "Долгий рецепт (более 60 минут)"


def check_servings(servings, members_count):
    """Проверить, хватит ли порций на всю семью."""
    if servings >= members_count:
        return "Порций хватит на всю семью"
    return "Порций недостаточно для всей семьи"


def is_favorite(status):
    """Вернуть текстовый статус избранного рецепта."""
    if status:
        return "Рецепт в избранном семьи"
    return "Рецепт не отмечен как избранный"


# --- Основной сценарий ---

print("=" * 50)
print(get_family_info(family_name, family_members_count, family_created_at))
print("=" * 50)

print("\nУчастники семьи:")
print(f"  • {member_1_name} ({member_1_role})")
print(f"  • {member_2_name} ({member_2_role})")
print(f"  • {member_3_name} ({member_3_role})")

print("\nКатегория:")
print(f"  • {category_name}: {category_description}")

print("\nРецепт:")
print(f"  {get_recipe_info(recipe_title, recipe_author, recipe_category)}")
print(f"  {check_cooking_time(recipe_cooking_time)}")
print(f"  {check_servings(recipe_servings, family_members_count)}")
print(f"  {is_favorite(recipe_is_family_favorite)}")
