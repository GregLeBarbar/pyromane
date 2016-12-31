from django.shortcuts import render, redirect
from taggit.models import Tag

from page.forms import PageForm
from page.models import Page


def create_page(request):
    """ Create a new page """
    page_form = PageForm(request.POST or None)
    if page_form.is_valid():
        page = page_form.save()
        return redirect(page)

    return render(request, 'page/create_page.html', {'page_form': page_form})


def get_page(request, slug):
    """ Get page """
    page = Page.objects.get(slug=slug)
    return render(request, 'page/get_page.html', {'page': page})


def get_pages_by_tag(request, tag):
    """ Get list of pages by tag """
    pages = Page.objects.filter(tags__name__in=[tag])
    return render(request, 'page/list.html', {'pages': pages})


def home(request):
    """ Display Homepage """
    tags = Tag.objects.all()
    return render(request, 'page/homepage.html', {'tags': tags})
