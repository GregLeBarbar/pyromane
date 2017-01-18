# coding:utf-8
from autoslug import AutoSlugField
from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django.urls import reverse
from model_utils.models import TimeStampedModel
from taggit.managers import TaggableManager


class Article(TimeStampedModel):

    published = models.DateTimeField()
    title = models.CharField(max_length=255, verbose_name="Titre")
    slug = AutoSlugField(populate_from='title', unique=True)
    subtitle = RichTextUploadingField(config_name='wiki', verbose_name="Sous titre")
    content = RichTextUploadingField(config_name='wiki', verbose_name="Contenu")
    file = models.FileField(null=True, blank=True)

    tags = TaggableManager(help_text="Les tags doivent être séparés par une virgule")

    class Meta:
        db_table = 'article'
        ordering = ('published', 'title')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('get_article', args=[self.slug])
