from django.contrib import admin
from django.urls import path
from recipes import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.welcome_view, name='welcome'),       # Главная страница
    path('menu/', views.recipe_list, name='recipe_list'), # Меню с рецептами
    path('recipe/<int:pk>/', views.recipe_detail, name='recipe_detail'),
    path('search/', views.recipe_search, name='recipe_search'),
    path('stats/', views.statistics, name='statistics'),
]
