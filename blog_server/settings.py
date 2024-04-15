import os
from pathlib import Path
import datetime
import environ
import ast

BASE_DIR = Path(__file__).resolve().parent.parent

env = environ.Env()

"""
通过指定环境遍历加载不同env文件
PROJECT_ENV=production python manage.py crontab add
默认场景下可不指定，则加载local文件
"""
env_name = env.str("PROJECT_ENV", "develop")
# reading .env file
file_path = f"./envs/{env_name}.env"
file_path = file_path.replace("\r", "").replace("\n", "")
environ.Env.read_env(file_path)


SECRET_KEY = env("SECRET_KEY")
DEBUG = ast.literal_eval(env("DEBUG"))
SESSION_COOKIE_SECURE = ast.literal_eval(env("SESSION_COOKIE_SECURE"))
ALLOWED_HOSTS = ast.literal_eval(env("ALLOWED_HOSTS"))
CSRF_TRUSTED_ORIGINS = ast.literal_eval(env("CSRF_TRUSTED_ORIGINS"))
# ALLOWED_HOSTS = [
#     "localhost",
#     "127.0.0.1",
#     "[::1]",
#     "api.mapanfeng.com",
#     "admin.mapanfeng.com",
# ]

CORS_ORIGIN_WHITELIST = ast.literal_eval(env("ALLOWED_HOSTS"))

DOMAIN = env("DOMAIN")
STATIC_DOMAIN = env("STATIC_DOMAIN")
IMAGE_PATH = env("IMAGE_PATH")
AUDIO_PATH = env("AUDIO_PATH")
JWT_AUTH_HEADER_PREFIX = env("JWT_AUTH_HEADER_PREFIX")
CORS_ALLOWED_ORIGIN_REGEXES = [r"^https?:\/\/([a-zA-Z\.]?)+(mapanfeng\.com)"]
CORS_ALLOW_CREDENTIALS = True


# path
# 是否自动忽略url末尾 /
APPEND_SLASH = False


# Application definition
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "rest_framework",
    "rest_framework_simplejwt",
    "django_filters",
    "middleware.TokenAuthenticationMiddleware",
    "home.apps.HomeConfig",
    "user.apps.UserConfig",
    "draft.apps.DraftConfig",
    "post.apps.PostConfig",
    "picture.apps.PictureConfig",
    "audio.apps.AudioConfig",
]

MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    # "middleware.TokenAuthenticationMiddleware.TokenAuthenticationMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]


ROOT_URLCONF = "blog_server.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "blog_server.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

ANGUAGE_CODE = "zh-hans"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/
STATIC_URL = "/server_static/"
STATIC_ROOT = os.path.join(os.path.dirname(__file__), "server_static")
# 设置图片等静态文件的路径
STATICFILES_DIRS = [os.path.join(BASE_DIR, "server_static")]

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


# REST 分页
REST_FRAMEWORK = {
    "DEFAULT_SCHEMA_CLASS": "rest_framework.schemas.coreapi.AutoSchema",
    "DEFAULT_PAGINATION_CLASS": "utils.pagination.Pagination",
    "PAGE_SIZE": 10000,
    "DATETIME_FORMAT": "%Y-%m-%d %H:%M:%S",
    "DEFAULT_FILTER_BACKENDS": [
        "django_filters.rest_framework.DjangoFilterBackend",
    ],
    "DEFAULT_RENDERER_CLASSES": [
        "rest_framework.renderers.JSONRenderer",
        "rest_framework.renderers.BrowsableAPIRenderer",
    ],
    "DEFAULT_PARSER_CLASSES": [
        "rest_framework.parsers.JSONParser",
        "rest_framework.parsers.FormParser",
        "rest_framework.parsers.MultiPartParser",
    ],
    "DEFAULT_PERMISSION_CLASSES": [
        # 'rest_framework.permissions.IsAuthenticated',            # IsAuthenticated 仅通过认证的用户
        # 'rest_framework.permissions.AllowAny',                   # AllowAny 允许所有用户
        # 'rest_framework.permissions.IsAdminUser',                # IsAdminUser 仅管理员用户
        # 'rest_framework.permissions.IsAuthenticatedOrReadOnly',  # IsAuthenticatedOrReadOnly 认证的用户可以完全操作，否则只能get读取
        "rest_framework.permissions.IsAuthenticatedOrReadOnly",
    ],
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework.authentication.SessionAuthentication",
        "rest_framework.authentication.BasicAuthentication",
    ],
}

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": datetime.timedelta(days=7),
    "REFRESH_TOKEN_LIFETIME": datetime.timedelta(days=10),
}
