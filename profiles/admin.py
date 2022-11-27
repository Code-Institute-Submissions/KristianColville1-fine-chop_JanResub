from django.contrib import admin
from django.contrib.auth.models import User, Group
from .models import Role, Address, Profile


class RoleInlineAdmin(admin.StackedInline):
    """
    RoleInlineAdmin class
    """
    model = Role
    list_display = [field.name for field in Role._meta.get_fields()]
    search_fields = [field.name for field in Role._meta.get_fields()]


class AddressInlineAdmin(admin.StackedInline):
    """
    AddressInlineAdmin class
    """
    model = Address
    list_display = [field.name for field in Address._meta.get_fields()]
    search_fields = [field.name for field in Address._meta.get_fields()]


class ProfileInlineAdmin(admin.StackedInline):
    """
    ProfileInlineAdmin class
    """
    model = Profile
    list_display = [field.name for field in Profile._meta.get_fields()]
    search_fields = [field.name for field in Profile._meta.get_fields()]


class UserAdmin(admin.ModelAdmin):
    """
    UserAdmin class
    """
    model = User
    fields = ['username', 'email']
    inlines = [ProfileInlineAdmin, RoleInlineAdmin, AddressInlineAdmin]


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.unregister(Group)
