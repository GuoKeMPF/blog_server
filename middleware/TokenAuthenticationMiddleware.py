from django.http import HttpResponseForbidden


class TokenAuthenticationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # # 检查请求头中是否包含名为 'Authorization' 的 token，并验证其值
        # authorization_header = request.headers.get("Authorization")
        # if not authorization_header:
        #     return HttpResponseForbidden("Missing 'Authorization' header.")

        # # 解析 token，这里假设 token 存在于 Authorization header 的 Bearer 令牌中
        # token = authorization_header.split(" ")[1]  # 假设格式为 "Bearer token_value"

        # # 在这里进行验证 token 的逻辑，比如检查 token 是否在数据库中合法等
        # if not self.is_valid_token(token):
        #     return HttpResponseForbidden("Invalid token.")

        return self.get_response(request)

    def is_valid_token(self, token):
        # 在这里实现验证 token 的逻辑，例如检查数据库中是否存在该 token 等
        # 返回 True 表示 token 合法，返回 False 表示 token 不合法
        # 这里只是一个示例，你需要根据实际情况实现合适的逻辑
        return token == "valid_token_value"
