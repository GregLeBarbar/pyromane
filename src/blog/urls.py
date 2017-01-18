# coding:utf-8
from django.conf.urls import url
from .views import edit_article, get_article, get_articles_by_tag

urlpatterns = [

    url(r'^create/article/$',
        edit_article,
        name='create_article'),

    url(r'^edit/article/(?P<article_id>\d+)/$',
        edit_article,
        name='edit_article'),

    url(r'^articles/by-tag/(?P<tag_slug>[a-z0-9-_]+)/$',
        get_articles_by_tag,
        name='get_articles_by_tag'),

    url(r'^article/(?P<slug>[a-z0-9-_]+)/$',
        get_article,
        name='get_article'),
]
