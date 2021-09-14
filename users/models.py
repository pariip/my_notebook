from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.auth.models import AbstractUser
from django.db.models import Model
from django.utils import timezone

from users.managers import CustomUserManager, TokenManager
from django.utils.translation import gettext_lazy as _

# Create your models here.

class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        _('email address'),
        blank=True,
        null=True,
        unique=True
    )
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    status = models.SmallIntegerField(default=-1)
    date_joined = models.DateTimeField(default=timezone.now)
    phone = models.CharField(
        max_length=16,
        blank=True,
        null=True,
        unique=True
    )
    username = models.CharField(
        max_length=150,
        unique=True,
        blank=True,
        null=True
    )
    USERNAME_FIELD = 'username'
    is_online = models.SmallIntegerField(default=0)
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.username


class JWTToken(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    token = models.CharField(max_length=256)
    createdAt = models.DateTimeField(default=timezone.now)
    updatedAt = models.DateTimeField(default=timezone.now)
    objects = TokenManager()
