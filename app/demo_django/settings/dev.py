import os

from .base import *
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent.parent
PROJECT_DIR = Path(__file__).resolve().parent.parent.parent.parent

load_dotenv(PROJECT_DIR.joinpath('.env'))

DATABASES = {
    # # postgres
    # "default": {
    #     "ENGINE": "django.db.backends.postgresql",
    #     "NAME": "demo_django",
    #     "USER": "postgres",  # TODO 数据库用户配置方式需要优化
    #     "PASSWORD": "wawawa",
    #     "HOST": "127.0.0.1",
    #     "PORT": "5432",
    # }

    # https://dev.mysql.com/doc/refman/8.1/en/option-files.html
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "demo_django",
        "HOST": "127.0.0.1",
        "PORT": "3306",
        "USER": os.getenv('MYSQL_USER'),
        "PASSWORD": os.getenv('MYSQL_PASSWORD')
    }
}

CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.redis.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379",
    }
}

INSTALLED_APPS.append('rest_framework')

REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ]
}

if __name__ == '__main__':
    print(os.getenv('MYSQL_USER'))
    pass
