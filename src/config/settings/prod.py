# coding:utf-8
from .base import *  # noqa


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'pyromane',
        'USER': 'pyromane',
        'PASSWORD': get_secret("DATABASE_PASSWORD"),  # noqa
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}

STATIC_ROOT = BASE_DIR.child('static')  # noqa

ALLOWED_HOSTS = ['greglebarbar.pythonanywhere.com']
