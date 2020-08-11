import json

from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIRequestFactory, force_authenticate

from notes.models import Note
from notes.serializers import NoteSerializers
from notes.views import Notes, Detail
from users.models import CustomUser


class TestNotes(TestCase):
    def setUp(self):
        self.user = CustomUser.objects.create(username='pari', password='123456', email='p@yahoo.com', is_active=True,
                                              status=1)
        self.note = Note.objects.create(title='test note', description='this is test for my note', public_note=True,
                                        user_id=self.user.id)
        self.factory = APIRequestFactory()
        self.view = Notes.as_view()

    def test_get(self):
        request = self.factory.get(reverse('note'))
        force_authenticate(request, user=self.user)
        response = self.view(request)
        note = Note.objects.all()
        serializer = NoteSerializers(note, many=True)
        for item in serializer.data:
            print(item['title'], self.note.title)
            self.assertEqual(item['title'], self.note.title, 'This field is required.')
            self.assertEqual(item['description'], self.note.description, 'This field is required.')
        self.assertEqual(status.HTTP_200_OK, response.status_code)

    def test_post(self):
        request = self.factory.post(reverse('note'), data=json.dumps(
            {'title': 'note1', 'description': 'this is test for note', 'public_note': True, 'user': self.user.id}),
                                    content_type='application/json')
        force_authenticate(request, user=self.user)
        response = self.view(request)
        self.assertEqual(status.HTTP_200_OK, response.status_code)


class TestDetail(TestCase):
    def setUp(self):
        self.user = CustomUser.objects.create(username='pari', password='123456', email='p@yahoo.com', is_active=True,
                                              status=1)
        self.note = Note.objects.create(title='test note', description='this is test for my note', public_note=True,
                                        user_id=self.user.id)
        self.factory = APIRequestFactory()
        self.view = Detail.as_view()

    def test_put(self):
        request = self.factory.put(reverse('detail', kwargs={'pk': self.note.id}), data=json.dumps(
            {'title': 'test note', 'description': 'this is test for note', 'public_note': True}),
                                   content_type='application/json')
        force_authenticate(request, user=self.user)
        response = self.view(request, self.note.id)
        self.assertEqual(status.HTTP_200_OK, response.status_code)

    def test_delete(self):
        request = self.factory.delete(reverse('detail', kwargs={'pk': self.note.id}))
        force_authenticate(request=request, user=self.user)
        response = self.view(request, self.note.id)
        self.assertEqual(status.HTTP_200_OK, response.status_code)
