from rest_framework import serializers

from users.models import CustomUser


class SignInSerializers(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'phone', 'email']


class SignupSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=32)
    email = serializers.EmailField(required=True)
    password = serializers.CharField(min_length=6, max_length=100, write_only=True)

    def create(self, validated_data):
        user = CustomUser.objects.create(email=validated_data['email'],
                                         username=validated_data['username'])
        user.set_password(validated_data['password'])
        user.save()
        return user

    class Meta:
        model = CustomUser
        feilds = ("__all__")


class UserSerializer(serializers.ModelSerializer):
    fields = "__all__"
    extra_kwargs = {
        'user': {'read_only': True},
    }

    class Meta:
        model = CustomUser
        fields = "__all__"
        extra_kwargs = {
            'user': {'read_only': True},
        }

    def to_representation(self, instance):
        data = {}
        data['id'] = instance.id
        data['username'] = instance.username
        # data['email'] = ''
        # if data['email'] != '':
        data['email'] = instance.email
        return data
