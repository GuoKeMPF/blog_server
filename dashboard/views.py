from rest_framework.viewsets import ModelViewSet
from draft.models import Draft
from post.models import Post
from picture.models import Picture
from audio.models import Audio
from django.http import JsonResponse

# Create your views here.


class DashboardView(ModelViewSet):

    def retrieve(self, request, *args, **kwargs):
        draft_count = Draft.objects.count()
        post_count = Post.objects.count()
        picture_count = Picture.objects.count()
        audio_count = Audio.objects.count()
        return JsonResponse(
            {
                "draft": draft_count,
                "post": post_count,
                "picture": picture_count,
                "audio": audio_count,
            },
            status=200,
            safe=False,
        )
