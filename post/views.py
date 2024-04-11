# Create your views here.


from rest_framework.viewsets import ModelViewSet


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
