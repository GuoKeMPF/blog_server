import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.base import View
from django.utils.decorators import method_decorator
from django.contrib.auth import authenticate, login, logout
from django.middleware.csrf import get_token
from utils.cryptography.decrypt import decrypt
from django.conf import settings
from django.contrib.auth.models import AnonymousUser


@method_decorator(csrf_exempt, name="dispatch")
class LoginView(View):
    def post(sele, request):
        # json
        body = json.loads(request.body)
        account = body.get("account")
        password = body.get("password")
        realName = decrypt(account)
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
        if isinstance(request.user, AnonymousUser):
            response = JsonResponse({"message": "logout success"}, status=200)
            response.delete_cookie(key="csrftoken")
            response.delete_cookie(key="sessionid")
            return response
        else:
            response = JsonResponse({"message": "logout failed"}, status=500)
            return response

    def dispatch(self, *args, **kwargs):
        return super(LogoutView, self).dispatch(*args, **kwargs)
