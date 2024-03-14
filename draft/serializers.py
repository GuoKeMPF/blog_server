from rest_framework import serializers

from .models import Draft

class DraftSerializer(serializers.ModelSerializer):
    class Meta:
        model = Draft
        fields = '__all__'



class DraftsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Draft
        fields = ['id', 'title', 'author','description', 'create_time', 'update_time']