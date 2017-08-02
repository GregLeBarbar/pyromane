# coding:utf-8
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from taggit.models import Tag

from .forms import ArticleForm
from .models import Article


@login_required
def edit_article(request, article_id=None):
    """ Create a new article of blog or edit an existing article """

    if article_id:
        article = Article.objects.get(id=article_id)
    else:
        article = None
    is_edit_article = (article is not None)
    article_form = ArticleForm(request.POST or None, request.FILES or None, instance=article)
    if article_form.is_valid():
        data = article_form.data
        article = article_form.save()

        if 'save_and_close' in data:
            return redirect(article)

    return render(request,
                  'blog/create_article.html',
                  {'article_form': article_form, 'is_edit_article': is_edit_article})


def get_article(request, slug):
    """ Get page """
    article = Article.objects.get(slug=slug)
    return render(request, 'blog/get_article.html', {'article': article})


def get_articles_by_tag(request, tag_slug):
    """ Get list of pages by tag """
    tag = Tag.objects.get(slug=tag_slug)
    articles = Article.objects.filter(tags__slug__in=[tag_slug])
    return render(request, 'blog/list.html', {'articles': articles, 'tag': tag})


def home(request):
    """ Display Homepage """
    articles = Article.objects.all().order_by('-published')
    tags = Tag.objects.order_by('name')
    return render(request, 'blog/homepage.html', {'tags': tags, 'articles': articles})
