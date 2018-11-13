from django.test import TestCase

# Create your tests here.
from django.urls import reverse

class RssIndexViewTests(TestCase):
    def test_no_feed(self):
        response = self.client.get(reverse("index"))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["feed"], None)

    def test_user_feed(self):
        response = self.client.get(reverse("index") + "?url=https://www.djangoproject.com/rss/weblog/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["feed"], None)

