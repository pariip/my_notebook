from django.db import models
from django.utils import timezone

from users.models import CustomUser


class Note(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    public_note = models.BooleanField(default=False)
    createdAt = models.DateTimeField(default=timezone.now())
    updatedAt = models.DateTimeField(default=timezone.now())
    deletedAt = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.title
