# coding:utf-8
from django.test import RequestFactory
from django.test import TestCase

from page.models import Page
from page.views import home, get_page, create_page, get_pages_by_tag


class PageModelTestCase(TestCase):

    def setUp(self):
        Page.objects.create(title="Ma 1ère page")
        Page.objects.create(title="Ma 1ère page")

    def test_slug_is_unique(self):
        """
        Slug must be unique
        """
        first_page = Page.objects.get(id=1)
        second_page = Page.objects.get(id=2)
        self.assertEqual(first_page.slug, "ma-1ere-page")
        self.assertEqual(second_page.slug, "ma-1ere-page-2")

    def test_str(self):
        """
         Test the special method __str__
        """
        first_page = Page.objects.get(id=1)
        self.assertEqual(first_page.__str__(), "Ma 1ère page")

    def test_get_absolute_url(self):
        """
        Test the method absolute_url.
        """
        first_page = Page.objects.get(id=1)
        self.assertEqual(first_page.get_absolute_url(), '/page/get/ma-1ere-page/')


class PageViewTestCase(TestCase):

    def setUp(self):
        Page.objects.create(title="Ma 1ère page")
        self.factory = RequestFactory()

    def test_home_view(self):
        request = self.factory.get('/')
        response = home(request)
        self.assertEqual(response.status_code, 200)

    def test_get_page_view(self):
        first_page = Page.objects.get(id=1)
        request = self.factory.get('/ma-1ere-page/')
        response = get_page(request, first_page.slug)
        self.assertEqual(response.status_code, 200)

    def test_create_page_and_get_pages_by_tag_views(self):
        request = self.factory.get('/ma-1ere-page/')
        response = create_page(request)
        self.assertEqual(response.status_code, 200)

        form_data = {'title': 'je ne suis pas inspiré', 'content': 'prout', 'tags': 'rototo'}
        response = self.client.post("/page/create/", form_data)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Page.objects.get(id=2).slug, 'je-ne-suis-pas-inspire')

        request = self.factory.get('/page/by-tag/rototo/')
        response = get_pages_by_tag(request, tag="rototo")
        self.assertEqual(response.status_code, 200)
