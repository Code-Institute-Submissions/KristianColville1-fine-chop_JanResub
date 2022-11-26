from django.shortcuts import (
    render, redirect, reverse, HttpResponse, get_object_or_404)
from django.contrib import messages
from menu.models import MenuItem


def view_cart(request):
    """
    A view that renders the cart contents page
    """
    return render(request, 'cart/cart.html')


def add_to_cart(request, menu_item_id):
    """
    Adds quantity of the specified item to cart
    """
    menu_item = get_object_or_404(MenuItem, pk=menu_item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    portion_size = None

    if 'portion_size' in request.POST:
        portion_size = request.POST['portion_size']
    cart = request.session.get('cart', {})

    if portion_size:
        if menu_item_id in list(cart.keys()):
            if portion_size in cart[menu_item_id]['menu_items_by_size'].keys():
                cart[menu_item_id]['menu_items_by_size'][
                    portion_size] += quantity
                messages.success(
                    request, f"""
        Updated portion {portion_size.upper()}{menu_item.name} quantity to
        {cart[menu_item_id]["menu_items_by_size"][portion_size]}""")
            else:
                cart[menu_item_id]['menu_items_by_size'][
                    portion_size] = quantity
                messages.success(
                    request, f"""
        Added portion {portion_size.upper()}{menu_item.name} to your cart""")
        else:
            cart[menu_item_id] = {
                'menu_items_by_size': {
                    portion_size: quantity
                }
            }
            messages.success(
                request, f"""
        Added portion {portion_size.upper()}{menu_item.name} to your cart""")
    else:
        if menu_item_id in list(cart.keys()):
            cart[menu_item_id] += quantity
            messages.success(request,
                             f'Updated {menu_item.name} amount in your cart')
        else:
            cart[menu_item_id] = quantity
            messages.success(request, f'Added {menu_item.name} to your cart')

    request.session['cart'] = cart
    return redirect(redirect_url)


def update_cart(request, food_id):
    """
    Update the quantity of the specified menu item to the specified amount
    in the cart for users
    """
    menu_item = get_object_or_404(MenuItem, pk=food_id)
    quantity = int(request.POST.get('quantity'))
    portion_size = None
    if 'portion_size' in request.POST:
        portion_size = request.POST['portion_size']
    cart = request.session.get('cart', {})

    if portion_size:
        if quantity > 0:
            cart[food_id]['menu_items_by_size'][portion_size] = quantity
            messages.success(
                request, f"""
        Updated portion size {portion_size.upper()} {menu_item.name} quantity
        to {cart[food_id]['menu_items_by_size'][portion_size]}
        in your cart""")
        else:
            del cart[food_id]['menu_items_by_size'][portion_size]
            if not cart[food_id]['menu_items_by_size']:
                cart.pop(food_id)
            messages.success(
                request, f"""
        Removed portion size {portion_size.upper()} {menu_item.name} from your
        cart""")

    else:
        if quantity > 0:
            cart[food_id] = quantity
            messages.success(
                request, f"""
        Updated {menu_item.name} quantity in your cart to {cart[food_id]}""")
        else:
            cart.pop(food_id)
            messages.success(
                request, f"""
        Removed {menu_item.name} from your cart""")

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))


def remove_from_cart(request, menu_item_id):
    """
    Removes quantity of the specified item from cart
    """

    try:
        menu_item = get_object_or_404(MenuItem, pk=menu_item_id)
        portion_size = None
        if 'portion_size' in request.POST:
            portion_size = request.POST['portion_size']
        cart = request.session.get('cart', {})

        if portion_size:
            del cart[menu_item_id]['menu_items_by_size'][portion_size]
            if not cart[menu_item_id]['menu_items_by_size']:
                cart.pop(menu_item_id)
            messages.success(
                request, f"""
        Removed portion size {portion_size.upper()} {menu_item.name} from your
        cart""")
        else:
            cart.pop(menu_item_id)
            messages.success(
                request, f"""
        Removed {menu_item.name} from your cart""")

        request.session['cart'] = cart
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing Menu item: {e}')
        return HttpResponse(status=500)
