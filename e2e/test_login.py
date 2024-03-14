"""Test login."""

import requests
import json
from .config import account, password
from .urls import getUrl
from utils.cryptography.encrypt import encrypt
import pytest
from django.test import Client

@pytest.fixture
def client():
    return Client()


def test_my_function(client):
    url = getUrl('login')
    encodePwd = encrypt(password)
    encodeUser = encrypt(account)
    param = {
        "username": encodeUser,
        "password": encodePwd,
    }
    response = requests.post(url, data=json.dumps(param), headers={
                             'Content-Type': 'application/json'})
    assert response.status_code == 200
