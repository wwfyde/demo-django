from django.test import TestCase
from django.urls import reverse


# Create your tests here.

class ViewsTestCase(TestCase):

    def test_index(self):
        resp = self.client.get(reverse('index'))
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, 'Hello, world!')