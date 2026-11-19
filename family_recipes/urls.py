from django.contrib import admin
from django.urls import path, include
from recipes import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.welcome_view, name='welcome'),
    path('menu/', views.recipe_list, name='recipe_list'),
    path('recipe/<int:pk>/', views.recipe_detail, name='recipe_detail'),
    path('search/', views.recipe_search, name='recipe_search'),
    path('stats/', views.statistics, name='statistics'),
]

# Подключаем Debug Toolbar только в режиме разработки
from django.conf import settings
if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
