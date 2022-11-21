from django.shortcuts import render, get_object_or_404
from .models import MenuItem, Category


def get_menu(request):
    """
    Brings the user to the food menu page
    """
    categories = Category.objects.all()
    menu_items = MenuItem.objects.all()
    context = {
        'categories': categories,
        'menu_items': menu_items,
    }
    return render(request, 'menu/menu-all.html', context)


def get_menu_item_detail(request, menu_item_id, str):
    """
    Renders a specific menu item for viewing
    """
    categories = Category.objects.all()
    menu_item = get_object_or_404(MenuItem, pk=menu_item_id)
    context = {
        'categories': categories,
        'menu_item': menu_item,
    }
    return render(request, 'menu/menu_item_detail.html', context)


def get_food_menu(request, str):
    categories = Category.objects.all()
    context = {
        'main_menu': False,
        'categories': categories,
    }
    return render(request, 'menu/category.html', context)
