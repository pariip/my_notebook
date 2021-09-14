# Create your tests here.
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from rest_framework import status


class UsersManagersTests(TestCase):

    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(username='youyou', email='p@user.com', password='123456')
        self.assertEqual(user.email, 'p@user.com')
        self.assertEqual(user.username, 'youyou')
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
        try:
            # username is None for the AbstractUser option
            # username does not exist for the AbstractBaseUser option
            self.assertEqual(user.username, 'youyou')
        except AttributeError:
            pass
        with self.assertRaises(TypeError):
            User.objects.create_user()
        with self.assertRaises(TypeError):
            User.objects.create_user(email='')
        with self.assertRaises(TypeError):
            User.objects.create_user(username='')
        # with self.assertRaises(ValueError):
        #     User.objects.create_user(username='',email='', password='123456')

    def test_create_superuser(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser('pari', email='super@user.com', password='foo')
        self.assertEqual(admin_user.email, 'super@user.com')
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)
        try:
            # username is None for the AbstractUser option
            # username does not exist for the AbstractBaseUser option
            # self.assertIsNone(admin_user.username)
            self.assertEqual(admin_user.username, 'pari')
        except AttributeError:
            pass
        with self.assertRaises(ValueError):
            User.objects.create_superuser(
                username='pari', email='super@user.com', password='foo', is_superuser=False)


class JWTTokenTests(TestCase):
    def test_api_jwt(self):
        url = reverse('signIn')
        u = get_user_model().objects.create_user(username='user', email='user@foo.com', password='pass')
        u.is_active = True
        u.save()
        resp = self.client.get(url, data={'username': 'user', 'password': 'pass'}, format='json')
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
