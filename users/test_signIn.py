from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class TestSignIn(APITestCase):
    def test_get(self):
        url = reverse('signIn')
        u = get_user_model().objects.create_user(username='user', email='user@foo.com', password='pass')
        u.is_active = True
        u.save()
        resp = self.client.get(url, {'username': 'user', 'password': 'pass'}, format='json')
        print(resp.status_code)
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
