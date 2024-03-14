from rest_framework.viewsets import ModelViewSet
from .models import Draft
from .serializers import DraftsSerializer, DraftSerializer
from utils.pagination import Pagination

class DraftViewSet(ModelViewSet):
    queryset = Draft.objects.all()
    serializer_class = DraftSerializer
    pagination_class = Pagination
    filterset_fields = ['title', 'content', 'author']

    def list(self, request, *args, **kwargs):
        page = self.paginate_queryset(self.queryset)
        serializer = DraftsSerializer(page, many=True)
        return self.get_paginated_response(serializer.data)
