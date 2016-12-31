# coding:utf-8
from .base import *  # noqa


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'pyromane',
        'USER': 'pyromane',
        'PASSWORD': get_secret("DATABASE_PASSWORD"),  # noqa
    }
}

STATIC_ROOT = BASE_DIR.child('static')  # noqa

ALLOWED_HOSTS = ['greglebarbar.pythonanywhere.com']
