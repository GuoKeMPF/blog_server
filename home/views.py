from django.http import HttpResponse
from django.views import View

class HomeView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse("Hello, world!")

    def post(self, request, *args, **kwargs):
        return HttpResponse("Hello, world!")