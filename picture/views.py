from django.http import JsonResponse
from .models import Picture
from .serializers import PictureSerializer
from rest_framework.viewsets import ModelViewSet
from utils.file.manageImage import saveImage, deleteImage
from utils.pagination import Pagination


class PictureViewSet(ModelViewSet):
    serializer_class = PictureSerializer
    pagination_class = Pagination
    queryset = Picture.objects.all()

    def list(self, request, *args, **kwargs):
        page = self.paginate_queryset(self.queryset)
        serializer = self.serializer_class(page, many=True)
        return self.get_paginated_response(serializer.data)

    def create(self, request, *args, **kwargs):
        f = request.FILES.get("file")
        description = request.POST.get("description", "")
        imageInfo = saveImage(f)
        picture = Picture(
            src=imageInfo["src"],
            width=imageInfo["width"],
            height=imageInfo["height"],
            name=imageInfo["name"],
            unique_name=imageInfo["unique_name"],
            description=description,
        )
        picture.save()
        return JsonResponse(imageInfo, safe=False, status=200)

    def destroy(self, request, *args, **kwargs):
        id = kwargs.get("id")
        picture = Picture.objects.get(id=id)
        if picture is None:
            return JsonResponse(
                {"message": "file dose't exist"}, status=500, safe=False
            )
        else:
            res = picture.delete()
            try:
                deleteImage(picture.unique_name)
            except FileNotFoundError:
                return JsonResponse(
                    {"message": "can't find file"}, status=500, safe=False
                )
            return JsonResponse(res, status=200, safe=False)

    def retrieve(self, request, pk=None):
        picture = self.get_object()
        picture.views += 1
        picture.save()
        serializer = self.get_serializer(picture)
        return JsonResponse(serializer.data)

    def uploads(self, request, *args, **kwargs):
        files = request.FILES.getlist("file")
        description = request.POST.get("description", "")
        locations = []
        for f in files:
            imageInfo = saveImage(f)
            picture = Picture(
                src=imageInfo["src"],
                width=imageInfo["width"],
                height=imageInfo["height"],
                name=imageInfo["name"],
                unique_name=imageInfo["unique_name"],
                description=description,
            )
            picture.save()
            locations.append(imageInfo)
        return JsonResponse(locations, safe=False)
