import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.base import View
from django.utils.decorators import method_decorator
from django.contrib.auth import authenticate, login, logout
from django.middleware.csrf import get_token
from utils.cryptography.decrypt import decrypt
from django.conf import settings

# Create your views here.
cookieConfig = {
    "domain": "localhost",
    "secure": True,
    "httponly": True,
    "samesite": "lax",
}


@method_decorator(csrf_exempt, name="dispatch")
class LoginView(View):
    def post(sele, request):
        # json
        body = json.loads(request.body)
        username = body.get("username")
        password = body.get("password")
        realName = decrypt(username)
        realPwd = decrypt(password)
        user = authenticate(username=realName, password=realPwd)
        if user is not None:
            if user.is_active:
                login(request, user)
                csrftoken = get_token(request)
                response = JsonResponse(
                    {
                        "username": user.get_username(),
                        "message": "login success",
                        "csrftoken": csrftoken,
                    }
                )
                response.set_cookie(
                    key="X-Csrftoken",
                    value=csrftoken,
                    secure=cookieConfig.get("secure"),
                    httponly=cookieConfig.get("httponly"),
                    samesite=cookieConfig.get("samesite"),
                )
                return response
            else:
                return JsonResponse(
                    {"message": "Error user name or password"}, status=500
                )
        else:
            return JsonResponse({"message": "Error user name or password"}, status=500)

    def dispatch(self, request, *args, **kwargs):
        return super(LoginView, self).dispatch(request, *args, **kwargs)


@method_decorator(csrf_exempt, name="dispatch")
class LogoutView(View):
    def post(self, request):
        res = logout(request)
        if res:
            return JsonResponse({"data": "logout success"}, status=200)
        else:
            return JsonResponse({"message": "logout failed"}, status=500)

    def dispatch(self, *args, **kwargs):
        return super(LogoutView, self).dispatch(*args, **kwargs)
