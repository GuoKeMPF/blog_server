from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend

User = get_user_model()


class EmailOrUsernameModelBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            # 尝试用提供的用户名或邮箱查找用户
            user = User.objects.get(email=username)
        except User.DoesNotExist:
            # 如果找不到用户，则尝试用提供的用户名查找用户
            try:
                user = User.objects.get(username=username)
            except User.DoesNotExist:
                return None

        # 检查用户提供的密码是否正确
        if user.check_password(password):
            return user  # 返回用户对象表示验证成功
        else:
            return None
