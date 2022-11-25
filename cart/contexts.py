from django.shortcuts import get_object_or_404
from django.conf import settings
from decimal import Decimal
from menu.models import MenuItem


def cart_contents(request):
    """
    Context processor for cart contents to render on all templates
    """
    cart_items = []
    total = 0
    item_count = 0
    user_distance = 0
    delivery_cost = 0
    can_deliver = True
    cart = request.session.get('cart', {})

    for food_id, food_amount in cart.items():
        if isinstance(food_amount, int):
            menu_item = get_object_or_404(MenuItem, pk=food_id)
            total += food_amount * menu_item.price
            item_count += food_amount
            cart_items.append({
                'food_id': food_id,
                'quantity': food_amount,
                'menu_item': menu_item,
            })
        else:
            menu_item = get_object_or_404(MenuItem, pk=food_id)
            for portion_size, quantity in food_amount[
                    'menu_items_by_size'].items():
                total += quantity * menu_item.price
                item_count += quantity
                cart_items.append({
                    'food_id': food_id,
                    'quantity': quantity,
                    'menu_item': menu_item,
                    'portion_size': portion_size
                })

    # calculates delivery cost based on kilometer
    # if the cart has items then add delivery cost
    if len(cart_items) > 0:
        if user_distance < 3:
            delivery_cost = settings.MINIMUM_DELIVERY_COST
        else:
            user_distance = user_distance - 3
            delivery_total = user_distance / 1 * settings.DELIVERY_COST_PER_KM
            delivery_total = Decimal(delivery_total + 3)
            # if the total delivery cost is above this
            # then don't deliver as too far away
            if delivery_total > 8.50:
                can_deliver = False

    grand_total = delivery_cost + total

    context = {
        'cart_items': cart_items,
        'total': total,
        'item_count': item_count,
        'delivery_cost': delivery_cost,
        'can_deliver': can_deliver,
        'grand_total': grand_total
    }
    return context
