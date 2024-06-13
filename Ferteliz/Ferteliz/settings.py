"""
Django settings for Ferteliz project.

Generated by 'django-admin startproject' using Django 5.0.5.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

from pathlib import Path
import os
import pymongo
from django.utils.translation import gettext_lazy as _


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-!%kjgrqiu&2s9a&#3hg7=y^h=wgrr^dv(%m91^(&=4(m)ym!im'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'core',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    "django.middleware.locale.LocaleMiddleware",
]

ROOT_URLCONF = 'Ferteliz.urls'

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
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

from django.contrib import messages

MESSAGE_TAGS = {
    messages.DEBUG: 'alert-info',
    messages.INFO: 'alert-info',
    messages.SUCCESS: 'alert-success',
    messages.WARNING: 'alert-warning',
    messages.ERROR: 'alert-danger',
}

WSGI_APPLICATION = 'Ferteliz.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.dummy',
    }
}
MONGODB_SETTINGS = {
    'db': os.environ.get('MONGODB_DB', 'Ferteliz_DataBase'),
    'username': os.environ.get('MONGODB_USER', ''),
    'password': os.environ.get('MONGODB_PASS', ''),
    'host': os.environ.get('MONGODB_HOST', 'localhost'),
    'port': int(os.environ.get('MONGODB_PORT', 27017)),
    'authentication_source': 'admin'
}

client = pymongo.MongoClient(
    host=MONGODB_SETTINGS['host'],
    port=MONGODB_SETTINGS['port'],
    username=MONGODB_SETTINGS['username'],
    password=MONGODB_SETTINGS['password'],
    authSource=MONGODB_SETTINGS['authentication_source']
)
db = client[MONGODB_SETTINGS['db']]

# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'pt-br'

LANGUAGES = [
    ("en", _("English")),
    ("pt", _("Portuguese")),
]

TIME_ZONE = 'America/Sao_Paulo'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'


STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static")
]


# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL = 'core.UserModel'

APPEND_SLASH = True

# Configuração de autenticação
LOGIN_URL = 'login'

# Redireciona usuário após login
LOGIN_REDIRECT_URL = 'home'

# Redireciona usuário após logout
LOGOUT_REDIRECT_URL = 'login'

# Adiciona '/' no final dos urls que não o tiverem
APPEND_SLASH = True

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')