from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.db.models import Count, Avg, Q
from .models import Recipe, Category

def welcome_view(request):
    return render(request, 'recipes/welcome.html')

def recipe_list(request):
    # ВОТ ОНА, ОПТИМИЗАЦИЯ: select_related('category') убирает лишние запросы
    recipes = Recipe.objects.select_related('category').all().order_by('category_id', 'id')
    paginator = Paginator(recipes, 20) 
    page_obj = paginator.get_page(request.GET.get('page'))
    return render(request, 'recipes/recipe_list.html', {'page_obj': page_obj})

def recipe_detail(request, pk):
    recipe = get_object_or_404(Recipe.objects.select_related('category', 'author'), pk=pk)
    return render(request, 'recipes/recipe_detail.html', {'recipe': recipe})

def recipe_search(request):
    query = request.GET.get('q', '')
    recipes = Recipe.objects.select_related('category', 'author').all()
    if query:
        recipes = recipes.filter(
            Q(title__icontains=query) | Q(ingredients__icontains=query)
        )
    paginator = Paginator(recipes, 10)
    page_obj = paginator.get_page(request.GET.get('page'))
    return render(request, 'recipes/search.html', {'page_obj': page_obj, 'query': query})

def statistics(request):
    avg_time = Recipe.objects.aggregate(Avg('cooking_time'))['cooking_time__avg']
    total_recipes = Recipe.objects.count()
    categories = Category.objects.annotate(recipe_count=Count('recipes')).order_by('id')
    return render(request, 'recipes/stats.html', {
        'avg_time': avg_time, 'total_recipes': total_recipes, 'categories': categories
    })
