# coding:utf-8
"""pyromane URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from ckeditor_uploader import views
from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.contrib.sitemaps import GenericSitemap
from django.contrib.sitemaps.views import sitemap

from page.models import Page
from page.views import home

info_dict = {
    'queryset': Page.objects.all(),
    'date_field': 'modified',
}

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    # Ckeditor explicit call to change decorator
    url(r'^upload/', login_required(views.upload), name='ckeditor_upload'),
    url(r'^browse/', login_required(views.browse), name='ckeditor_browse'),

    # the sitemap
    url(r'^sitemap\.xml$', sitemap,
        {'sitemaps': {'blog': GenericSitemap(info_dict, priority=0.6)}},
        name='django.contrib.sitemaps.views.sitemap'),

    url(r'^page/', include('page.urls')),
    url(r'^$', home, name='home'),
    url('^', include('django.contrib.auth.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
              + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

TAGGIT_CASE_INSENSITIVE = True
