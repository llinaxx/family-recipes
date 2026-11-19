from django.contrib import admin
from .models import Category, Author, Recipe

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name') # Столбцы в списке
    search_fields = ('name',)     # Поиск по названию

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'role')
    search_fields = ('role',)

@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    # Отображаем название, категорию, автора и время
    list_display = ('id', 'title', 'category', 'author', 'cooking_time')
    # Добавляем фильтры справа
    list_filter = ('category', 'author') 
    # Поиск по названию и ингредиентам
    search_fields = ('title', 'ingredients')
