from django.contrib import admin
from .models import Article


class ArticleAdmin(admin.ModelAdmin):
    readonly_fields = ('slug', 'created', 'modified', )


admin.site.register(Article, ArticleAdmin)
