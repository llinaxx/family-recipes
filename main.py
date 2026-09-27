"""Family Recipes — сервис управления кулинарными рецептами семьи."""
from storage import (
    load_families,
    load_members,
    load_categories,
    load_recipes,
    save_all,
)
from utils import input_int


def show_recipes(recipes: list) -> None:
    """Вывести список рецептов."""
    if not recipes:
        print("Рецептов нет.")
        return
    for r in recipes:
        print(r)


def show_families(families: list) -> None:
    """Вывести семьи с участниками."""
    for f in families:
        print(f)


def find_recipes(recipes: list, query: str) -> list:
    """Найти рецепты по подстроке названия."""
    return [r for r in recipes if query.lower() in r.title.lower()]


def filter_recipes(recipes: list, max_time: int) -> list:
    """Отобрать рецепты по времени готовки."""
    return [r for r in recipes if r.cooking_time <= max_time]


def sort_recipes(recipes: list) -> list:
    """Отсортировать рецепты по времени готовки."""
    return sorted(recipes, key=lambda r: r.cooking_time)


def get_stats(recipes: list) -> dict:
    """Статистика по рецептам."""
    if not recipes:
        return {"total": 0, "avg_time": 0, "favorites": 0}
    total = len(recipes)
    avg_time = sum(r.cooking_time for r in recipes) / total
    favorites = sum(1 for r in recipes if r.is_favorite)
    return {"total": total, "avg_time": round(avg_time, 1), "favorites": favorites}


def main() -> None:
    families = load_families()
    members = load_members()
    categories = load_categories()
    recipes = load_recipes(members, categories)

    while True:
        print("\n=== Семейные рецепты ===")
        print("1. Показать все рецепты")
        print("2. Найти рецепт по названию")
        print("3. Фильтр по времени готовки")
        print("4. Сортировать по времени")
        print("5. Статистика")
        print("6. Показать семьи")
        print("7. Отметить рецепт избранным")
        print("0. Выход")
        choice = input_int("Выберите действие: ")

        if choice == 0:
            save_all(families, members, categories, recipes)
            print("Данные сохранены. До свидания!")
            break
        elif choice == 1:
            show_recipes(recipes)
        elif choice == 2:
            query = input("Введите часть названия: ")
            show_recipes(find_recipes(recipes, query))
        elif choice == 3:
            max_time = input_int("Максимальное время (мин): ")
            show_recipes(filter_recipes(recipes, max_time))
        elif choice == 4:
            show_recipes(sort_recipes(recipes))
        elif choice == 5:
            stats = get_stats(recipes)
            print(f"Всего рецептов: {stats['total']}")
            print(f"Среднее время готовки: {stats['avg_time']} мин")
            print(f"Избранных: {stats['favorites']}")
        elif choice == 6:
            show_families(families)
        elif choice == 7:
            rid = input_int("ID рецепта: ")
            for r in recipes:
                if r.id == rid:
                    r.mark_favorite()
                    print(f"Рецепт «{r.title}» отмечен как избранный.")
                    break
            else:
                print("Рецепт не найден.")
        else:
            print("Неверный выбор.")


if __name__ == "__main__":
    main()
