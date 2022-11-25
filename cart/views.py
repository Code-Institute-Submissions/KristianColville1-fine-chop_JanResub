from django.shortcuts import render, redirect


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
