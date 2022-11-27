from django.contrib import admin
from django.contrib.auth.models import User, Group
from .models import Profile


class ProfileInlineAdmin(admin.StackedInline):
    """
    ProfileInlineAdmin class
    """
    model = Profile
    list_display = [field.name for field in Profile._meta.get_fields()]
    search_fields = [field.name for field in Profile._meta.get_fields()]


class UserAdmin(admin.ModelAdmin):
    """
    UserAdmin provides a better site owner experience to manage the various
    models that a user can create
    """
    model = User
    fields = ['username', 'email']
    inlines = [ProfileInlineAdmin]


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.unregister(Group)
