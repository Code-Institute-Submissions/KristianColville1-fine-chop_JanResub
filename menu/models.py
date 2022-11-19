from django.db import models

CATEGORY_CHOICES = (
    ('A', 'Starters'),
    ('B', 'Mains'),
    ('C', 'Noodles'),
    ('D', 'Rices'),
    ('E', 'Wok'),
    ('F', 'Curries'),
    ('G', 'Soups'),
    ('H', 'Vegan'),
    ('I', 'Salads'),
    ('J', 'Kids Menu'),
    ('K', 'Drinks'),
)

STATUS_CHOICES = ((0, "Not Serving"), (1, "Serving"))


class FoodItem(models.Model):
    """Abstract class for MenuItems"""

    name = models.CharField(max_length=250, unique=True)
    description = models.TextField()
    image = models.ImageField(null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Food Items'
        abstract = True


class FoodItemProductDetails(models.Model):
    """Abstract class for Order Details"""
    product_code = models.CharField(max_length=255, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    class Meta:
        abstract = True


class MenuItem(FoodItem, FoodItemProductDetails):
    """Menu item class mixin"""
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=1)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS_CHOICES, default=1)

    def __str__(self):
        """String representation"""
        return self.name
