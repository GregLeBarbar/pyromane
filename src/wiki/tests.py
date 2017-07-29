# coding:utf-8
from django.contrib.auth.models import User
from django.test import RequestFactory
from django.test import TestCase

from blog.views import home
from wiki.models import Page


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
        self.factory = RequestFactory()
        self.client.force_login(User.objects.get_or_create(username='testuser')[0])
        Page.objects.create(title="Ma 1ère page")

    def test_home_view(self):
        request = self.factory.get('/')
        response = home(request)
        self.assertEqual(response.status_code, 200)

    def test_get_page_view(self):
        response = self.client.get('/page/get/ma-1ere-page/')
        self.assertEqual(response.status_code, 200)

    def test_create_page_and_get_pages_by_tag_views(self):

        # Test create page
        response = self.client.post('/page/create/',
                                    {'title': 'je ne suis pas inspiré', 'content': 'vraiment pas', 'tags': 'supertag'})
        self.assertEqual(response.status_code, 200)

        # Test get page
        self.assertEqual(Page.objects.get(id=2).slug, 'je-ne-suis-pas-inspire')
        response = self.client.get('/page/get/je-ne-suis-pas-inspire/')
        self.assertEqual(response.status_code, 200)

        # Test get all pages by tag
        response = self.client.get('/page/by-tag/supertag/')
        self.assertEqual(response.status_code, 200)

        # Test edit page
        response = self.client.get('/page/edit/2/')
        self.assertEqual(response.status_code, 200)

        # Test modify page
        response = self.client.post('/page/edit/2/',
                                    {'title': 'je ne suis pas inspiré mais vraiment pas',
                                     'content': 'vraiment pas',
                                     'tags': 'supertag',
                                     },
                                    follow=True)
        self.assertEqual(response.status_code, 200)

        # Test get page
        # self.assertEqual(Page.objects.get(id=2).slug, 'je-ne-suis-pas-inspire-mais-vraiment-pas')
        # response = self.client.get('/page/get/je-ne-suis-pas-inspire-mais-vraiment-pas/')
        # self.assertEqual(response.status_code, 200)
