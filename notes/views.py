from django.shortcuts import get_object_or_404
from django.utils import timezone
from rest_framework import views, status
# Create your views here.
from rest_framework.response import Response

from notes.models import Note
from notes.serializers import NoteSerializers


class Notes(views.APIView):
    def post(self, request):
        serializer = NoteSerializers(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        notes = Note.objects.filter(user=request.user)
        serializer = NoteSerializers(notes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class Detail(views.APIView):
    def put(self, request, pk):
        note = get_object_or_404(Note, pk=pk, deletedAt__isnull=True)
        serializer = NoteSerializers(instance=note, data=request.data, context={'request': request})
        print('iii')
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        note = get_object_or_404(Note, pk=pk, deletedAt__isnull=True)
        note.deletedAt = timezone.now()
        note.delete()
        return Response(status=status.HTTP_200_OK)
