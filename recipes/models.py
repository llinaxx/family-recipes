from django.db import models

class Author(models.Model):
    role = models.CharField(max_length=50, verbose_name="Роль в семье", help_text="Например: Бабушка, Дедушка")
    def __str__(self): return self.role
    class Meta:
        verbose_name = "Автор"
        verbose_name_plural = "Авторы"

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="Название категории")
    def __str__(self): return self.name
    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

class Recipe(models.Model):
    title = models.CharField(max_length=200, verbose_name="Название рецепта")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="recipes", verbose_name="Категория")
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True, blank=True, related_name="recipes", verbose_name="Автор")
    cooking_time = models.PositiveIntegerField(help_text="Время в минутах", verbose_name="Время готовки")
    ingredients = models.TextField(verbose_name="Ингредиенты")
    instructions = models.TextField(verbose_name="Инструкция")
    # НОВОЕ ПОЛЕ ДЛЯ КАРТИНКИ
    image = models.ImageField(upload_to='recipes/', blank=True, null=True, verbose_name="Фото блюда")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    def __str__(self): return self.title
    class Meta:
        verbose_name = "Рецепт"
        verbose_name_plural = "Рецепты"
