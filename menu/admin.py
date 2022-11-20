from django.contrib import admin
from .models import MenuItem, Category, Allergen


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
    CategoryAdmin provides staff and site owner with ability
    to manage menus for creation and updating.
    """
    model = Category
    list_display = ['name', 'friendly_name']


@admin.register(Allergen)
class AllergenAdmin(admin.ModelAdmin):
    """
    AllergenAdmin provides staff and site owner with ability
    to manage menu items and update allergy information
    accordingly.
    """
    model = Allergen
    list_display = ['name', 'friendly_name']
