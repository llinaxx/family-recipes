"""
Family Recipes — сервис управления кулинарными рецептами семьи.
"""

from storage import load_data, save_data
from models.recipes import (
    add_recipe,
    find_recipes_by_title,
    filter_recipes_by_time,
    sort_recipes_by_time,
    get_recipes_stats,
)
from utils import input_int


def show_recipes(recipes: list) -> None:
    """Вывести список рецептов."""
    if not recipes:
        print("Рецептов нет.")
        return
    for r in recipes:
        fav = "★" if r["is_favorite"] else " "
        print(f"{fav} [{r['id']}] {r['title']} — {r['cooking_time']} мин")


def main() -> None:
    recipes = load_data("recipes.json")

    while True:
        print("\n=== Семейные рецепты ===")
        print("1. Показать все рецепты")
        print("2. Найти рецепт по названию")
        print("3. Фильтр по времени готовки")
        print("4. Сортировать по времени")
        print("5. Статистика")
        print("6. Добавить рецепт")
        print("0. Выход")
        choice = input_int("Выберите действие: ")

        if choice == 0:
            save_data("recipes.json", recipes)
            print("Данные сохранены. До свидания!")
            break
        elif choice == 1:
            show_recipes(recipes)
        elif choice == 2:
            query = input("Введите часть названия: ")
            show_recipes(find_recipes_by_title(recipes, query))
        elif choice == 3:
            max_time = input_int("Максимальное время (мин): ")
            show_recipes(filter_recipes_by_time(recipes, max_time))
        elif choice == 4:
            show_recipes(sort_recipes_by_time(recipes))
        elif choice == 5:
            stats = get_recipes_stats(recipes)
            print(f"Всего рецептов: {stats['total']}")
            print(f"Среднее время готовки: {stats['avg_time']} мин")
            print(f"Избранных: {stats['favorites']}")
        elif choice == 6:
            title = input("Название рецепта: ")
            author_id = input_int("ID автора: ")
            category_id = input_int("ID категории: ")
            cooking_time = input_int("Время готовки (мин): ")
            difficulty = input("Сложность (легко/средне/сложно): ")
            add_recipe(recipes, title, author_id, category_id,
                       cooking_time, difficulty)
            print(f"Рецепт «{title}» добавлен.")
        else:
            print("Неверный выбор.")


if __name__ == "__main__":
    main()
