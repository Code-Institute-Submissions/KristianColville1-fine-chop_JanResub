import uuid
from django.db import models
from django.db.models import Sum
from menu.models import MenuItem


class Order(models.Model):
    """
    Order model for customer information
    """
    order_number = models.CharField(max_length=32, null=False, editable=False)
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    country = models.CharField(max_length=40, null=False, blank=False)
    postcode = models.CharField(max_length=20, null=True, blank=True)
    town_or_city = models.CharField(max_length=40, null=False, blank=False)
    street_address1 = models.CharField(max_length=80, null=False, blank=False)
    street_address2 = models.CharField(max_length=80, null=True, blank=True)
    county = models.CharField(max_length=80, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    delivery_cost = models.DecimalField(max_digits=6,
                                        decimal_places=2,
                                        null=False,
                                        default=0)
    can_deliver = models.BooleanField(default=False, null=False, blank=False)
    order_total = models.DecimalField(max_digits=10,
                                      decimal_places=2,
                                      null=False,
                                      default=0)
    grand_total = models.DecimalField(max_digits=10,
                                      decimal_places=2,
                                      null=False,
                                      default=0)
    original_cart = models.TextField(null=False, blank=False, default='')
    stripe_pid = models.CharField(max_length=254,
                                  null=False,
                                  blank=False,
                                  default='')

    def _generate_order_number(self):
        """
        Private Method generates a random, unique order number using UUID
        """
        return uuid.uuid4().hex.upper()

    def update_total(self):
        """
        Checks the address to make sure it can deliver to this location,
        Updates grand total each time a line item is added
        """
        self.order_total = self.lineitems.aggregate(
            Sum('lineitem_total'))['lineitem_total__sum'] or 0
        self.grand_total = self.order_total + self.delivery_cost
        self.save()

    def save(self, *args, **kwargs):
        """
        Overrides the original save method to set the order number
        if it hasn't been set already.
        """
        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_number


class OrderLineItem(models.Model):
    """
    OrderLineItem Model for Orders
    """
    order = models.ForeignKey(Order,
                              null=False,
                              blank=False,
                              on_delete=models.CASCADE,
                              related_name='lineitems')
    menu_item = models.ForeignKey(MenuItem,
                                  null=False,
                                  blank=False,
                                  on_delete=models.CASCADE)
    portion_size = models.CharField(max_length=2, null=True,
                                    blank=True)  # is it a meal?
    quantity = models.IntegerField(null=False, blank=False, default=0)
    lineitem_total = models.DecimalField(max_digits=6,
                                         decimal_places=2,
                                         null=False,
                                         blank=False,
                                         editable=False)

    def save(self, *args, **kwargs):
        """
        Overrides the original save method to set the lineitem total
        and update the order total.
        """
        self.lineitem_total = self.menu_item.price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return f"""
Menu Item Code {self.menu_item.product_code} on order {self.order.order_number}
"""
