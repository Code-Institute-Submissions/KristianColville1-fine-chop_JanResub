from django.db import models


class FoodItem(models.Model):
    """Abstract class for MenuItems"""

    name = models.CharField(max_length=250, unique=True)
    description = models.CharField(max_length=1000, unique=False)

    class Meta:
        abstract = True


