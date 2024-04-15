# Create your views here.


from rest_framework.viewsets import ModelViewSet
from django.http import JsonResponse
from .models import Post

from .serializers import PostSerializer, PostsSerializer


class PostViewSet(ModelViewSet):

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filterset_fields = ["title", "content", "author"]

    def list(self, request, *args, **kwargs):
        page = self.paginate_queryset(self.queryset)
        serializer = PostsSerializer(page, many=True)
        return self.get_paginated_response(serializer.data)

    def retrieve(self, request, pk=None):
        post = self.get_object()
        post.views += 1
        post.save()
        serializer = self.get_serializer(post)
        return JsonResponse(serializer.data)
