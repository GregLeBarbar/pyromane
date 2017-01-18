# coding:utf-8
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from taggit.models import Tag

from .forms import PageForm
from .models import Page


@login_required
def edit_page(request, page_id=None):
    """ Create a new page or edit an existing page """
    if page_id:
        page = Page.objects.get(id=page_id)
    else:
        page = None
    is_edit_page = (page is not None)
    page_form = PageForm(request.POST or None, request.FILES or None, instance=page)
    if page_form.is_valid():
        data = page_form.data
        page = page_form.save()

        if 'save_and_close' in data:
            return redirect(page)

    return render(request, 'page/create_page.html', {'page_form': page_form, 'is_edit_page': is_edit_page})


@login_required
def get_page(request, slug):
    """ Get page """
    page = Page.objects.get(slug=slug)
    return render(request, 'page/get_page.html', {'page': page})


def get_pages_by_tag(request, tag_slug):
    """ Get list of pages by tag """
    tag = Tag.objects.get(slug=tag_slug)
    pages = Page.objects.filter(tags__slug__in=[tag_slug])
    return render(request, 'page/list.html', {'pages': pages, 'tag': tag})
