
from django.test import TestCase, Client
from utils.cryptography.encrypt import encrypt
from django.urls import reverse

username = 'admin'
password = 'admin'


class TextTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_get_ping(self):
        responseUrl = self.client.get('/', content_type='application/json')
        self.assertEqual(responseUrl.status_code, 200)

        responseRev = self.client.get(
            reverse("home"), content_type='application/json')
        self.assertEqual(responseRev.status_code, 200)
        self.assertEqual(responseRev.content,
                         responseUrl.content,
                         "Hello, world!")
