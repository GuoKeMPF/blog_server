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


def test_create_draft(client):
    login_url = getUrl('login')
    encodePwd = encrypt(password)
    encodeUser = encrypt(account)
    param = {
        "username": encodeUser,
        "password": encodePwd,
    }
    response = requests.post(login_url, data=json.dumps(param), headers={
                             'Content-Type': 'application/json'})
    assert response.status_code == 200
    res =  response.json()
    token = res['token']
    draft_url =  getUrl('draft')
    draft_body = {"title":"des4","description":"des4","content":"<p>des4</p>"}
    create_response = requests.post(draft_url, data=json.dumps(draft_body), headers={'Content-Type':'application/json', 'Authorization': token})
    create_result = response.json()
    assert create_response.ok, 'HTTP 请求失败'




