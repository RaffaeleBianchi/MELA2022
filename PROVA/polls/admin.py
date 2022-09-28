from django.contrib import admin

# Register your models here.

from .models import The_lord_of_ring,Author,Harry_Potter,The_Chronicles_of_Narnia,Star_War,Hunger_Game


admin.site.register(Author)
admin.site.register(Harry_Potter)
admin.site.register(The_lord_of_ring)
admin.site.register(The_Chronicles_of_Narnia)
admin.site.register(Star_War)
admin.site.register(Hunger_Game)
class ArticleAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Header", {'fields': ["title", "subtitle", "article_slug", "series"]}),
        ("Content", {"fields": ["content", "notes"]}),
        ("Date", {"fields": ["modified"]})       
    ]

# django_project/main/admin.py
from .models import Article

class ArticleSeriesAdmin(admin.ModelAdmin):
    fields = [
        "title",
        "subtitle",
        "slug",
        # "published"
    ]

# Register your models here.
#admin.site.register(ArticleSeries, ArticleSeriesAdmin)
admin.site.register(Article, ArticleAdmin)