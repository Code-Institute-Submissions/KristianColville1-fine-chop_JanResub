from django.contrib import admin
from .models import MenuItem, Category


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    """
    MenuItemAdmin provides staff and site owner with ability
    to manage menu items for creation and updating.
    """
    model = MenuItem
    list_display = [
        field.name for field in MenuItem._meta.get_fields()
        if field.name != "allergens"
    ]
    search_fields = [field.name for field in MenuItem._meta.get_fields()]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """
    MenuItemAdmin provides staff and site owner with ability
    to manage menu items for creation and updating.
    """
    model = Category
