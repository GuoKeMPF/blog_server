from django.test.testcases import TestCase
from django.contrib.auth import get_user_model
from test.config import username, password, email

class UserTestCase(TestCase):
     def setUpTestData():
        User = get_user_model()
        User.objects.create_superuser(
            username=username,
            password=password,
            email=email
        )


class GlobalSetupTestCase(UserTestCase):
    @classmethod
    def setUpTestData():
        User = get_user_model()
        User.objects.create_superuser(
            username='admin',
            password='admin',
            email='admin@qq.com'
        )

