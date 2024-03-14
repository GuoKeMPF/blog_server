

# Create your views here.

from rest_framework.viewsets import ModelViewSet

from .models import Text
from .serializers import TextSerializer,TextsSerializer

class TextViewSet(ModelViewSet):
    queryset = Text.objects.all()
    serializer_class = TextSerializer
    filterset_fields = ['title', 'content', 'author']

    def list(self, request, *args, **kwargs):
        page = self.paginate_queryset(self.queryset)
        serializer = TextsSerializer(page, many=True)
        return self.get_paginated_response(serializer.data)