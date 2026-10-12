# Family Recipes

Сервис для хранения кулинарных рецептов семьи.

## Назначение

Приложение, в котором семья хранит свои рецепты: кто автор,
сколько готовить, к какой категории относится блюдо.
Реализованы консольная и веб-версии приложения.

## Используемые технологии

- Python 3
- Django 5.2 — веб-фреймворк
- Django Template Language (шаблоны)
- HTML, CSS, Bootstrap 5.3
- pytest — автоматизированные тесты
- flake8 — проверка качества кода

## Предметная область

Домашняя кулинария. Учёт рецептов, категорий блюд и участников семьи.

## Основные сущности

- Семья (family)
- Участник (member)
- Рецепт (recipe)
- Категория (category)

## Веб-страницы

| URL | Имя маршрута | Назначение |
|---|---|---|
| `/` | `homepage:index` | Главная страница |
| `/recipes/` | `recipes:list` | Список рецептов |
| `/recipes/<id>/` | `recipes:detail` | Карточка рецепта |
| `/categories/` | `categories:list` | Список категорий |
| `/categories/<id>/` | `categories:detail` | Карточка категории |

## Архитектура веб-части

HTTP-запрос → URLconf → view → context → Django Template → HTML → HTTP-ответ

Шаблоны используют:
- базовый шаблон `base.html` с блоками `{% block %}`;
- наследование через `{% extends %}`;
- включаемые фрагменты через `{% include %}`;
- циклы `{% for %}`, условия `{% if %}`;
- именованные URL через `{% url %}`;
- фильтры (например, `|length`, `|default`);
- статические файлы (CSS, JS, изображения) через `{% static %}`.

## Структура проекта

family-recipes/
├── manage.py
├── main.py                  # консольная версия (ПР3)
├── storage.py               # загрузка/сохранение JSON
├── utils.py
├── family_recipes/          # настройки Django-проекта
├── templates/               # общие шаблоны
│   ├── base.html
│   ├── 404.html
│   └── includes/
│       └── navigation.html
├── homepage/                # приложение: главная
│   ├── templates/homepage/index.html
│   └── static/homepage/
│       ├── css/style.css
│       └── js/main.js
├── recipes/                 # приложение: рецепты
│   └── templates/recipes/
├── categories/              # приложение: категории
│   └── templates/categories/
├── models/                  # классы предметной области (ПР3)
├── data/                    # JSON-файлы данных
├── tests/                   # автоматические тесты
├── requirements.txt
├── pytest.ini
└── .flake8

## Запуск

### Веб-версия (Django)

python manage.py runserver

Открыть: http://127.0.0.1:8000/

### Консольная версия (ПР3)

python main.py

## Тесты

pytest -v

## Проверка стиля

flake8 .

## План развития

- Перенос сущностей в Django ORM
- Подключение базы данных
- Формы создания и редактирования
- Пользователи и авторизация
- REST API
- Docker
