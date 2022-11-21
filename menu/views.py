from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import MenuItem, Category


def get_menu(request):
    """
    Brings the user to the food menu page
    """
    menu_items = MenuItem.objects.all()
    query = None
    categories = None
    is_specific_food_menu = False
    is_category = 'All'

    if request.GET:
        if 'category' in request.GET:
            categories = request.GET['category']
            is_category = f'{categories}'
            menu_items = menu_items.filter(category__name=is_category)
            categories = Category.objects.filter(name__in=categories)
            is_specific_food_menu = True
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request,
                               "You didn't enter any search criteria!")
                return redirect(reverse('menu'))

            queries = Q(name__icontains=query) | Q(
                description__icontains=query)
            menu_items = menu_items.filter(queries)

    context = {
        'menu_categories': Category.objects.all(),
        'is_category': is_category,
        'current_category': categories,
        'is_specific_food_menu': is_specific_food_menu,
        'search_term': query,
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
