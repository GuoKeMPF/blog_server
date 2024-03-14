
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.base import View
from django.utils.decorators import method_decorator
from django.contrib.auth import authenticate, login, logout
from django.middleware.csrf import get_token
from utils.cryptography.decrypt import decrypt

from django.conf import settings
from utils.token.getUserToken import get_tokens_for_user

# Create your views here.


@method_decorator(csrf_exempt, name='dispatch')
class LoginView(View):
    def post(sele, request):
        # json
        body = json.loads(request.body)
        username = body.get('username')
        password = body.get('password')
        realname = decrypt(username)
        realpwd = decrypt(password)
        user = authenticate(username=realname, password=realpwd)
        if user is not None:
            if user.is_active:
                csrftoken = get_token(request)
                access = get_tokens_for_user(user)
                refresh = access.get('refresh')
                token = access.get('token')
                HEADER_AUTH_PREFIX = settings.JWT_AUTH_HEADER_PREFIX
                return JsonResponse({
                    "username": user.get_username(),
                    "message": "login success",
                    "refresh": refresh,
                    "token": HEADER_AUTH_PREFIX + ' '+token,
                    "csrftoken": csrftoken
                })
            else:
                return JsonResponse(
                    {"message": "Error username or password"}, status=500)
        else:
            return JsonResponse({"message": "Error username or password"}, status=500)

    def dispatch(self, request, *args, **kwargs):
        return super(LoginView, self).dispatch(request, *args, **kwargs)


@method_decorator(csrf_exempt, name='dispatch')
class LogoutView(View):
    def post(self, request):
        res = logout(request)
        if res:
            return JsonResponse({"data": "logout success"}, status=200)
        else:
            return JsonResponse({"message": "logout failed"}, status=500)

    def dispatch(self, *args, **kwargs):
        return super(LogoutView, self).dispatch(*args, **kwargs)
