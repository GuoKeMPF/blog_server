from rest_framework.viewsets import ModelViewSet
from draft.models import Draft
from text.models import Text
from picture.models import Picture
from audio.models import Audio
from django.http import JsonResponse

# Create your views here.


class DashboardView(ModelViewSet):

    def retrieve(self, request, *args, **kwargs):
        draft_count = Draft.objects.count()
        text_count = Text.objects.count()
        picture_count = Picture.objects.count()
        audio_count = Audio.objects.count()
        return JsonResponse({
            "draft": draft_count,
            "text": text_count,
            "picture": picture_count,
            "audio": audio_count,
        }, status=200, safe=False)
