from django.http import JsonResponse
from .models import Audio
from .serializers import AudioSerializer
from rest_framework.viewsets import ModelViewSet
from utils.file.manageAudio import saveAudio, deleteAudio
from utils.pagination import Pagination


class AudioViewSet(ModelViewSet):
    serializer_class = AudioSerializer
    pagination_class = Pagination
    queryset = Audio.objects.all()

    def list(self, request, *args, **kwargs):
        page = self.paginate_queryset(self.queryset)
        serializer = self.serializer_class(page, many=True)
        return self.get_paginated_response(serializer.data)

    def create(self, request, *args, **kwargs):
        f = request.FILES.get("file")
        description = request.POST.get("description", "")
        imageInfo = saveAudio(f)
        audio = Audio(
            src=imageInfo["src"],
            name=imageInfo["name"],
            unique_name=imageInfo["unique_name"],
            description=description,
        )
        audio.save()
        return JsonResponse(imageInfo, safe=False, status=200)

    def destroy(self, request, *args, **kwargs):
        id = kwargs.get("pk")
        audio = Audio.objects.get(id=id)
        if audio is None:
            return JsonResponse(
                {"message": "file dose't exist"}, status=500, safe=False
            )
        else:
            res = audio.delete()
            try:
                deleteAudio(audio.unique_name)
            except FileNotFoundError:
                return JsonResponse(
                    {"message": "can't find file"}, status=500, safe=False
                )
            return JsonResponse(res, status=200, safe=False)

    def uploads(self, request, *args, **kwargs):
        files = request.FILES.getlist("file")
        description = request.POST.get("description", "")
        locations = []
        for f in files:
            imageInfo = saveAudio(f)
            picture = Audio(
                src=imageInfo["src"],
                name=imageInfo["name"],
                unique_name=imageInfo["unique_name"],
                description=description,
            )
            picture.save()
            locations.append(imageInfo)
        return JsonResponse(locations, safe=False, status=200)

    def retrieve(self, request, pk=None):
        audio = self.get_object()
        audio.views += 1
        audio.save()
        serializer = self.get_serializer(audio)
        return JsonResponse(serializer.data)
