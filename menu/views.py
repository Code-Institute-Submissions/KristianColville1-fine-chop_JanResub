from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models.functions import Lower
from django.db.models import Q
from .models import MenuItem, Category
from .forms import MenuItemForm


def get_menu(request):
    """
    Brings the user to the food menu page
    """
    menu_items = MenuItem.objects.all()
    query = None
    categories = None
    is_specific_food_menu = False
    is_category = 'All'
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey

            if sortkey == 'name':
                sortkey = 'lower_name'
                menu_items = menu_items.annotate(lower_name=Lower('name'))

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            menu_items = menu_items.order_by(sortkey)

        if 'category' in request.GET:
            categories = request.GET['category']
            if categories != 'All':
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

    current_sorting = f'{sort}_{direction}'
    context = {
        'menu_categories': Category.objects.all(),
        'is_category': is_category,
        'current_category': categories,
        'current_sorting': current_sorting,
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


def add_menu_item(request):
    """
    Add a menu item to the a food menu
    """
    if request.method == 'POST':
        form = MenuItemForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added a new menu item!')
            return redirect(reverse('add_menu_item'))
        else:
            messages.error(
                request,
                'Failed to add menu item. Please ensure the form is valid.')
    else:
        form = MenuItemForm()

    template = 'menu/add_menu_item.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


def edit_menu_item(request, menu_item_id):
    """
    Edit a food item on the a food menu
    """
    menu_item = get_object_or_404(MenuItem, pk=menu_item_id)
    if request.method == 'POST':
        form = MenuItemForm(request.POST, request.FILES, instance=menu_item)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('menu_item_detail', args=[menu_item.id]))
        else:
            messages.error(
                request,
                'Failed to update menu item. Please ensure the form is valid.')
    else:
        form = MenuItemForm(instance=menu_item)
        messages.info(request, f'You are editing {menu_item.name}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': menu_item,
    }

    return render(request, template, context)
