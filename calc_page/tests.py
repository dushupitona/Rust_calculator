from django.test import TestCase

from django.urls import reverse

from http import HTTPStatus

# Create your tests here.


class IndexViewTestCase(TestCase):

    def test_view(self):
        path = reverse('index')
        response = self.client.get(path)

        self.assertEquals(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(response, 'calc_page/index.html')