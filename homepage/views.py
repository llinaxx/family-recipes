"""Главная страница и обработка 404."""
from django.shortcuts import render


def index(request):
    """Главная страница."""
    return render(request, "homepage/index.html")


def page_not_found(request, exception):
    """Своя страница 404."""
    return render(request, "404.html", status=404)
