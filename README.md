# Family Recipes

Сервис для хранения кулинарных рецептов семьи.

## Назначение

Приложение, в котором семья хранит свои рецепты: кто автор,
сколько готовить, к какой категории относится блюдо.
Реализованы консольная и веб-версии приложения.

## Используемые технологии

- Python 3
- Django 5.2 — веб-фреймворк
- HTML, CSS, Bootstrap 5.3 — оформление страниц
- pytest — автоматизированные тесты
- flake8 — проверка качества кода

## Предметная область

Домашняя кулинария. Учёт рецептов, категорий блюд и участников семьи.

## Основные сущности

- Семья (family)
- Участник (member)
- Рецепт (recipe)
- Категория (category)

## Веб-страницы (ПР5)

| URL | Назначение | View-функция |
|---|---|---|
| `/` | Главная страница | `homepage.views.index` |
| `/recipes/` | Список рецептов | `recipes.views.recipes` |
| `/recipes/<int:recipe_id>/` | Карточка рецепта | `recipes.views.recipe_detail` |
| `/categories/` | Список категорий | `categories.views.categories` |
| `/categories/<int:category_id>/` | Карточка категории | `categories.views.category_detail` |

## Структура проекта

family-recipes/
├── manage.py
├── main.py
├── storage.py
├── utils.py
├── family_recipes/
├── homepage/
├── recipes/
├── categories/
├── models/
├── data/
├── tests/
├── requirements.txt
├── pytest.ini
├── .flake8
└── README.md

## Запуск

### Веб-версия (Django)

python manage.py runserver

Открыть в браузере: http://127.0.0.1:8000/

### Консольная версия (ПР3)

python main.py

## Тесты

pytest -v

## Проверка стиля

flake8 .

## План развития

- Перенос сущностей в Django ORM
- Подключение базы данных
- Переход на Django-шаблоны (templates/)
- Формы создания и редактирования
- Пользователи и авторизация
- REST API
- Docker
