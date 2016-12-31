from django.contrib import admin
from .models import Page


class PageAdmin(admin.ModelAdmin):
    readonly_fields = ('slug', 'created', 'modified', )


admin.site.register(Page, PageAdmin)
