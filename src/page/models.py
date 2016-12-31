# coding:utf-8
from autoslug import AutoSlugField
from ckeditor.fields import RichTextField
from django.db import models
from django.urls import reverse
from model_utils.models import TimeStampedModel
from taggit.managers import TaggableManager


class Page(TimeStampedModel):

    title = models.CharField(max_length=255)
    slug = AutoSlugField(populate_from='title', unique=True)
    content = RichTextField(config_name='wiki')

    tags = TaggableManager()

    class Meta:
        db_table = 'page'
        ordering = ('title',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('get_page', args=[self.slug])
