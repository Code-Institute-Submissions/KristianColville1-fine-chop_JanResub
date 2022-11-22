from django.conf import settings
from decimal import Decimal


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

    # calculates delivery cost based on kilometer
    if user_distance < 3.5:
        delivery_cost = settings.MINIMUM_DELIVERY_COST
    else:
        user_distance = user_distance - 3.5
        delivery_total = user_distance / 1 * settings.DELIVERY_COST_PER_KM
        delivery_total = Decimal(delivery_total + 3.5 / 100)
        if delivery_total > 8.50:
            can_deliver = False
            # if the total delivery cost is above this
            # then don't deliver as too far away

    grand_total = delivery_total + total

    context = {
        'cart_items': cart_items,
        'total': total,
        'item_count': item_count,
        'delivery_cost': delivery_cost,
        'can_deliver': can_deliver,
        'grand_total': grand_total
    }
    return context
