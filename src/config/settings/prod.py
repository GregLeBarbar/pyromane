# coding:utf-8
from .base import *  # noqa


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'GregLeBarbar$pyromane',
        'USER': 'GregLeBarbar',
        'PASSWORD': get_secret("DATABASE_PASSWORD"),  # noqa
        'HOST': 'GregLeBarbar.mysql.pythonanywhere-services.com',
    }
}

STATIC_ROOT = BASE_DIR.child('static')  # noqa

MEDIA_ROOT = BASE_DIR.child('uploads')  # noqa

ALLOWED_HOSTS = ['greglebarbar.pythonanywhere.com']
