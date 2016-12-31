# coding:utf-8
from django.conf.urls import url
from .views import create_page, get_page, get_pages_by_tag

urlpatterns = [
    url(r'^create/$',
        create_page,
        name='create_page'),

    url(r'^by-tag/(?P<tag>[a-z0-9-_]+)/$',
        get_pages_by_tag,
        name='get_pages_by_tag'),

    url(r'^get/(?P<slug>[a-z0-9-_]+)/$',
        get_page,
        name='get_page'),
]
