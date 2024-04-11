from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
from django.urls import re_path

from home.views import HomeView
from draft.views import DraftViewSet
from post.views import PostViewSet

from picture.views import PictureViewSet
from audio.views import AudioViewSet
from user.views import LoginView, LogoutView
from dashboard.views import DashboardView


urlpatterns = [
    # 登陆退出
    re_path(r"^/?$", HomeView.as_view(), name="home"),
    re_path(r"^login/?$", LoginView.as_view(), name="login"),
    re_path(r"^logout/?$", LogoutView.as_view(), name="logout"),
    # 看板
    re_path(
        r"^dashboard/?$", DashboardView.as_view({"get": "retrieve"}), name="dashboard"
    ),
    # 草稿
    re_path(
        r"^draft/?$",
        DraftViewSet.as_view({"get": "list", "post": "create"}),
        name="draft",
    ),
    re_path(
        r"^draft/(?P<pk>\w+)/?$",
        DraftViewSet.as_view(
            {
                "get": "retrieve",
                "put": "update",
                "patch": "partial_update",
                "delete": "destroy",
            }
        ),
        name="draft",
    ),
    # 文章
    re_path(
        r"^post/?$", PostViewSet.as_view({"get": "list", "post": "create"}), name="text"
    ),
    re_path(
        r"^post/(?P<pk>\w+)/?$",
        PostViewSet.as_view(
            {
                "get": "retrieve",
                "put": "update",
                "patch": "partial_update",
                "delete": "destroy",
            }
        ),
        name="text",
    ),
    # 图片
    re_path(
        r"^picture/?$",
        PictureViewSet.as_view({"get": "list", "post": "create"}),
        name="picture",
    ),
    re_path(
        r"^pictures/?$", PictureViewSet.as_view({"post": "uploads"}), name="picture"
    ),
    re_path(
        r"^picture/(?P<id>\w+)/?$",
        PictureViewSet.as_view({"get": "retrieve", "delete": "destroy"}),
        name="picture",
    ),
    # 音频
    re_path(
        r"^audio/?$",
        AudioViewSet.as_view({"get": "list", "post": "create"}),
        name="audio",
    ),
    re_path(r"^audios/?$", AudioViewSet.as_view({"post": "uploads"}), name="audio"),
    re_path(
        r"^audio/(?P<id>\w+)/?$",
        AudioViewSet.as_view({"get": "retrieve", "delete": "destroy"}),
        name="audio",
    ),
    re_path(r"^admin/*/?", admin.site.urls),
]

urlpatterns += staticfiles_urlpatterns()
