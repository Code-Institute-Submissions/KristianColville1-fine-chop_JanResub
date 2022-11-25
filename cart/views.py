from django.shortcuts import render, redirect, reverse, HttpResponse


def view_cart(request):
    """
    A view that renders the cart contents page
    """
    return render(request, 'cart/cart.html')


def add_to_cart(request, menu_item_id):
    """
    Adds quantity of the specified item to cart
    """

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
            else:
                cart[menu_item_id]['menu_items_by_size'][
                    portion_size] = quantity
        else:
            cart[menu_item_id] = {
                'menu_items_by_size': {
                    portion_size: quantity
                }
            }
    else:
        if menu_item_id in list(cart.keys()):
            cart[menu_item_id] += quantity
        else:
            cart[menu_item_id] = quantity

    request.session['cart'] = cart
    print(request.session['cart'])
    return redirect(redirect_url)


def update_cart(request, food_id):
    """Adjust the quantity of the specified product to the specified amount"""

    quantity = int(request.POST.get('quantity'))
    portion_size = None
    if 'portion_size' in request.POST:
        portion_size = request.POST['portion_size']
    cart = request.session.get('cart', {})

    if portion_size == 'm':
        print('I made it here')
        if quantity > 0:
            cart[food_id]['menu_items_by_size'][portion_size] = quantity

        else:
            del cart[food_id]['menu_items_by_size'][portion_size]
            if not cart[food_id]['menu_items_by_size']:
                cart.pop(food_id)

    else:
        if quantity > 0:
            cart[food_id] = quantity
        else:
            cart.pop(food_id)

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))


def remove_from_cart(request, menu_item_id):
    """
    Removes quantity of the specified item from cart
    """

    try:
        size = None
        if 'product_size' in request.POST:
            size = request.POST['portion_size']
        cart = request.session.get('cart', {})

        if size:
            del cart[menu_item_id]['menu_items_by_size'][size]
            if not cart[menu_item_id]['menu_items_by_size']:
                cart.pop(menu_item_id)
        else:
            cart.pop(menu_item_id)

        request.session['cart'] = cart
        return HttpResponse(status=200)

    except Exception as e:
        return HttpResponse(status=500)
