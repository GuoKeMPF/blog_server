from rest_framework.viewsets import ModelViewSet
from .models import Draft
from .serializers import DraftsSerializer, DraftSerializer
from utils.pagination import Pagination
from .filters import DraftModelFilter


class DraftViewSet(ModelViewSet):
    queryset = Draft.objects.all()
    serializer_class = DraftSerializer
    pagination_class = Pagination
    filterset_class = DraftModelFilter

    def list(self, request, *args, **kwargs):
        filtered = self.filterset_class(request.GET, queryset=self.queryset)
        if filtered.is_valid():
            queryset = filtered.qs
        else:
            # 返回过滤参数错误的响应，如400 Bad Request
            return Response({"error": "Invalid filter parameters"}, status=400)
        data = self.paginate_queryset(queryset)
        serializer = DraftsSerializer(data, many=True)
        return self.get_paginated_response(serializer.data)
