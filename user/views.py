import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.base import View
from django.utils.decorators import method_decorator
from django.contrib.auth import authenticate, login, logout
from django.middleware.csrf import get_token
from utils.cryptography.decrypt import decrypt
from django.conf import settings
from django.contrib.auth.models import AnonymousUser, User
from django.core.serializers import serialize
from django.utils import timezone


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


class GetUserInfoView(View):
    def get(self, request):
        user = request.user
        if user.is_authenticated:  # 更安全的检查用户是否认证
            # 使用 serializers 来安全地序列化用户对象，这里仅作为示例，实际可按需选择字段

            user_data = {
                "username": user.username,
                "first_name": user.first_name,
                "last_name": user.last_name,
                "email": user.email,
                "is_staff": user.is_staff,
                "is_active": user.is_active,
                "date_joined": user.date_joined,
                "last_login": user.last_login,  # 处理未登录情况
                "groups": [
                    group.name for group in user.groups.all()
                ],  # 获取用户所属组的名称列表
                "user_permissions": [
                    perm.codename for perm in user.user_permissions.all()
                ],  # 获取用户所有权限的codename列表
                "is_superuser": user.is_superuser,
            }
            return JsonResponse(user_data, safe=False, status=200)
        else:
            return JsonResponse({"message": "User is not authenticated."}, status=401)

    def dispatch(self, *args, **kwargs):
        return super(GetUserInfoView, self).dispatch(*args, **kwargs)
