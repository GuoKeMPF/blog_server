from rest_framework import serializers

from .models import Text


class TextSerializer(serializers.ModelSerializer):
    class Meta:
        model = Text
        fields = '__all__'


class TextsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Text
        fields = ['id', 'title', 'author','description', 'create_time', 'update_time']