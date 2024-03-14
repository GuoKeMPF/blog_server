
from django.test import TestCase, Client
from utils.cryptography.encrypt import encrypt
from django.contrib.auth import get_user_model
from django.urls import reverse

from test.config import username, password
from test.UserTestCase import UserTestCase




class LoginTestCase(UserTestCase):
    def setUp(self):
        self.client = Client()
        

    def test_create_superuser(self):
        encodePwd = encrypt(password)
        encodeUserName = encrypt(username)
        params = {
            "username": encodeUserName,
            "password": encodePwd
        }
        response = self.client.post(
            reverse('login'), data=params, content_type='application/json')
        self.assertEqual(response.status_code, 200)
