
from django.test import TestCase, Client
from json import loads
from draft.models import Draft
from utils.cryptography.encrypt import encrypt

from test.config import username, password



class DraftTest(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        Draft.objects.create(
            title="test title 1", content="test content 1", author="test author 1", description="test description 1")
        Draft.objects.create(
            title="test title 2", content="test content 2", author="test author 2", description="test description 2")


    def test_create_draft_without_login(self):
        payload = {
            "title":"test title 1", 
            "content":"test content 1",
        	"author":"test author 1",
            "description":"test description 1"
		}
        response = self.client.post('/draft', payload)
        self.assertEqual(response.status_code, 401)
    
    
    def test_create_draft_with_login(self):
        payload = {
            "title":"test title 1", 
            "content":"test content 1",
        	"author":"test author 1",
            "description":"test description 1"
		}
        
        encodePwd = encrypt(password)
        encodeUserName = encrypt(username)
        params = {
            "username": encodeUserName,
            "password": encodePwd
        }
        loginRes = self.client.post('/login', data=params, content_type='application/json')
        # self.assertEqual(loginRes.status_code, 200)

    def test_draft_exists(self):
        response = self.client.get('/draft')
        self.assertEqual(response.status_code, 200)
        res = loads(response.content)
        self.assertEqual(res["count"], 2)
        self.assertEqual(res["size"], 10000)
        self.assertEqual(res["page"], 1)
        self.assertEqual(len(res['data']), 2)

