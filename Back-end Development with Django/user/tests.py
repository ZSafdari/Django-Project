from django.test import TestCase
from django.test import Client
from django.contrib.auth.models import User



class UserListTest(TestCase):

    def setUp(self):
        self.c = Client()
        User.objects.create(
            username="sam"
        )

    def test_user_list(self):
        response = self.c.get('/user/list')
        self.assertEqual(
            response.status_code,
            200
        )
        self.assertEqual(
            response.json(),
            ['sam']
        )

