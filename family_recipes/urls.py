from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from recipes import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.welcome_view, name='welcome'),
    path('menu/', views.recipe_list, name='recipe_list'),
    path('recipe/new/', views.recipe_create, name='recipe_create'), # Новый маршрут
    path('recipe/<int:pk>/', views.recipe_detail, name='recipe_detail'),
    path('recipe/<int:pk>/edit/', views.recipe_edit, name='recipe_edit'), # Новый маршрут
    path('search/', views.recipe_search, name='recipe_search'),
    path('stats/', views.statistics, name='statistics'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    import debug_toolbar
    urlpatterns = [path('__debug__/', include(debug_toolbar.urls))] + urlpatterns
