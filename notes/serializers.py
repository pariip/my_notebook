from rest_framework import serializers

from notes.models import Note
from users.serializers import UserSerializer


class NoteSerializers(serializers.ModelSerializer):
    title = serializers.CharField(max_length=100)
    description = serializers.CharField(max_length=300)
    owner = UserSerializer(default=serializers.CurrentUserDefault(), source='user', read_only=True)
    public_note = serializers.BooleanField(required=True)

    class Meta:
        model = Note
        fields = "__all__"
        extra_kwargs = {
            'user': {'read_only': True},
        }

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return Note.objects.create(**validated_data)

    def to_representation(self, obj):
        data = super(NoteSerializers, self).to_representation(obj)
        data['title'] = obj.title
        data['description'] = obj.description
        data['public_note'] = obj.public_note
        data.pop('user')
        return data
