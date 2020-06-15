from rest_framework import serializers

from users.models import CustomUser


class SignInSerializers(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'phone', 'email']
