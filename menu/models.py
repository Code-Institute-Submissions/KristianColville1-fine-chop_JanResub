from django.db import models

CATEGORIES = [
    'Starters',
    'Mains',
    'Noodles',
    'Rices',
    'Wok',
    'Curries',
    'Soups',
    'Vegan',
    'Salads',
    'Kids Menu',
    'Drinks',
]


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

