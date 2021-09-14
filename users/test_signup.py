from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class TestSignUp(APITestCase):
    def test_post(self):
        url = reverse('signUp')
        response = self.client.post(url, data={'username': 'user', 'email': 'user@yahoo.com', 'password': 'pass'})
        user = get_user_model().objects.last()
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(response.data['username'], user.username)
        self.assertEqual(1, user.id)
        self.assertEqual(response.data['email'], user.email)
