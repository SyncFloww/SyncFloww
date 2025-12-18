from .base import *

DEBUG = True
SECRET_KEY = 'django-insecure-dev-key'
ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

CELERY_BROKER_URL = 'redis://localhost:6379/0'
CORS_ALLOW_ALL_ORIGINS = True
