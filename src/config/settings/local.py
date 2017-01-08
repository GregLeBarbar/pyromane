# coding:utf-8
from .base import * # noqa


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

##
# Ubuntu paquets
# - postgresql
# - python-psycopg2
# - libpq-dev
#
# Packages python
# - psycopg2
#
# Help
# http://www.indjango.com/ubuntu-install-postgresql-and-pgadmin/
# http://stackoverflow.com/questions/8200917/postgresql-create-a-new-db-through-pgadmin-ui

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'pyromane',
        'USER': 'pyromane',
        'PASSWORD': get_secret("DATABASE_PASSWORD"),  # noqa
    }
}

STATIC_ROOT = BASE_DIR.child('static-for-dev')  # noqa

MEDIA_ROOT = BASE_DIR.child('uploads')  # noqa

ALLOWED_HOSTS = ['127.0.0.1', 'testserver']
