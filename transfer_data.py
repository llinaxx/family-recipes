import sqlite3
import os
import django

# ВАЖНО: Если твоя папка с настройками называется иначе (не family_recipes), поменяй строку ниже
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'family_recipes.settings')
django.setup()

from recipes.models import Category, Recipe

def transfer():
    try:
        old_conn = sqlite3.connect('db/project.db')
        old_conn.row_factory = sqlite3.Row
        cursor = old_conn.cursor()
        
        # Переносим категории (если таблица называлась categories)
        try:
            cursor.execute("SELECT * FROM categories")
            for row in cursor.fetchall():
                Category.objects.get_or_create(
                    id=row['id'],
                    defaults={'name': row['name']}
                )
            print("Категории перенесены!")
        except Exception as e:
            print(f"Категории не перенесены (возможно, другой формат): {e}")

        # Переносим рецепты (если таблица называлась recipes)
        try:
            cursor.execute("SELECT * FROM recipes")
            for row in cursor.fetchall():
                Recipe.objects.get_or_create(
                    id=row['id'],
                    defaults={
                        'title': row['title'],
                        'category_id': row['category_id'],
                        'cooking_time': 30, # Заглушка, если вдруг поля не было
                        'ingredients': 'Перенесено из старой БД',
                        'instructions': 'Перенесено из старой БД'
                    }
                )
            print("Рецепты перенесены!")
        except Exception as e:
             print(f"Рецепты не перенесены: {e}")
             
        old_conn.close()
    except Exception as e:
        print(f"Ошибка подключения к старой БД: {e}")

if __name__ == '__main__':
    transfer()
