from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from taggit.models import Tag

from page.forms import PageForm
from page.models import Page


@login_required
def edit_page(request, page_id=None):
    """ Create a new page or edit an existing page """
    if page_id:
        page = Page.objects.get(id=page_id)
    else:
        page = None
    is_edit_page = (page is not None)
    page_form = PageForm(instance=page, data=request.POST or None)
    if page_form.is_valid():
        page = page_form.save()
        return redirect(page)

    return render(request, 'page/create_page.html', {'page_form': page_form, 'is_edit_page': is_edit_page})


@login_required
def get_page(request, slug):
    """ Get page """
    page = Page.objects.get(slug=slug)
    return render(request, 'page/get_page.html', {'page': page})


def get_pages_by_tag(request, tag_slug):
    """ Get list of pages by tag """
    pages = Page.objects.filter(tags__slug__in=[tag_slug])
    return render(request, 'page/list.html', {'pages': pages})


def home(request):
    """ Display Homepage """
    tags = Tag.objects.all()
    return render(request, 'page/homepage.html', {'tags': tags})
