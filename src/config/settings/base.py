# coding:utf-8
"""
Django settings for pyromane project.

Generated by 'django-admin startproject' using Django 1.10.4.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""
import json
from unipath import Path
from django.core.exceptions import ImproperlyConfigured


# Build paths inside the project
BASE_DIR = Path(__file__).ancestor(4)
print('BASE DIR : {0}'.format(BASE_DIR))

SRC_DIR = Path(__file__).ancestor(3)
print('SRC DIR : {0}'.format(SRC_DIR))

# JSON-Based secrets module
with open(BASE_DIR + "/secrets.json", 'r') as f:
    secrets = json.loads(f.read())


def get_secret(setting, secrets=secrets):
    """
    Get the secret variable or return explicit exception.
    """
    try:
        return secrets[setting]
    except KeyError:
        error_msg = "Set the {0} environnement variable".format(setting)
        raise ImproperlyConfigured(error_msg)


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = get_secret("SECRET_KEY")


ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    # django apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.redirects',
    'django.contrib.sitemaps',
    # packages
    'ckeditor',
    'taggit',
    # apps
    'page',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.contrib.redirects.middleware.RedirectFallbackMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [SRC_DIR.child('templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'

# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'fr'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = (SRC_DIR.child("static"),)

SITE_ID = 1


CKEDITOR_CONFIGS = {

    'wiki': {
        'skin': 'moono',
        'toolbar_wiki': [
            {'name': 'basicstyles1', 'items': ['Bold', 'Italic', 'Underline']},
            {'name': 'basicstyles2', 'items': ['NumberedList', 'BulletedList']},
            {'name': 'basicstyles3', 'items': ['Subscript', 'Superscript']},
            {'name': 'links', 'items': ['Link', 'Unlink']},
            {'name': 'clipboard', 'items': ['Undo', 'Redo']},
            {'name': 'tools', 'items': ['Maximize']},
            {'name': 'document', 'items': ['Source']},
        ],
        'toolbar': 'wiki',  # put selected toolbar config here
        'tabSpaces': 4,
        'height': 600,
        'width': 1500,

        ##
        # Link configuration
        ##

        # hide tab and browser server button
        'linkShowAdvancedTab': False,
        'linkShowTargetTab': False,
        'removeDialogTabs': 'link:upload',

        # hide browser server button
        'filebrowserBrowseUrl': '',
    },
}
