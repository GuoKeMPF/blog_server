from .settings import *

# 将默认数据库配置更改为 test 配置

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'test_db.sqlite3',
    },
}
