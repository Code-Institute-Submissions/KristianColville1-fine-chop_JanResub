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
    cart = request.session.get('cart', {})

    if menu_item_id in list(cart.keys()):
        cart[menu_item_id] += quantity
    else:
        cart[menu_item_id] = quantity

    request.session['cart'] = cart
    print(request.session['cart'])
    return redirect(redirect_url)
