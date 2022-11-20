from django.shortcuts import render, get_object_or_404
from .models import MenuItem, Category


def get_menu(request):
    """
    Brings the user to the food menu page
    """
    categories = Category.objects.all()
    context = {
        'main_menu': 'main_menu',
        'categories': categories,
    }
    return render(request, 'menu/index.html', context)


def get_food_menu(request, str):
    categories = Category.objects.all()
    context = {
        'main_menu': 'main_menu',
        'categories': categories,
        'main_menu': False,
    }
    return render(request, 'menu/index.html', context)
