from django.contrib import admin
from .models import SubscribedUsers, Article, ArticleSeries


class SubscribedUsersAdmin(admin.ModelAdmin):
    """
    SubscribedUsersAdmin
    """
    list_display = ('email', 'name', 'created_date')


class ArticleSeriesAdmin(admin.ModelAdmin):
    """
    Series of Newsletters
    """
    fields = [
        'title',
        'subtitle',
        'slug',
        'author',
        'image',
    ]


class ArticleAdmin(admin.ModelAdmin):
    """
    Creating newsletters
    """
    fieldsets = [("Header", {
        "fields":
        ['title', 'subtitle', 'article_slug', 'series', 'author', 'image']
    }), ("Content", {
        "fields": ['content', 'notes']
    }), ("Date", {
        "fields": ['modified']
    })]


admin.site.register(SubscribedUsers, SubscribedUsersAdmin)
admin.site.register(ArticleSeries, ArticleSeriesAdmin)
admin.site.register(Article, ArticleAdmin)
