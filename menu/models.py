from django.db import models

STATUS_CHOICES = ((0, "Not Serving"), (1, "Serving"))


class Category(models.Model):
    """
    Category model for food menu items
    """

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class FoodItem(models.Model):
    """Abstract class for MenuItems"""

    name = models.CharField(max_length=250, unique=True)
    description = models.TextField()
    image = models.ImageField(null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)

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
    category = models.ForeignKey('Category',
                                 null=True,
                                 blank=True,
                                 on_delete=models.SET_NULL)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS_CHOICES, default=1)
    portion_sizes = models.BooleanField(default=False, null=True, blank=True)
    rating = models.DecimalField(max_digits=6,
                                 decimal_places=2,
                                 null=True,
                                 blank=True)
    rating = models.DecimalField(max_digits=6,
                                 decimal_places=2,
                                 null=True,
                                 blank=True)

    def __str__(self):
        """String representation"""
        return self.name
