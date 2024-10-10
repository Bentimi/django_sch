"""
Django settings for sch project.

Generated by 'django-admin startproject' using Django 5.1.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-8j2&lj4j6v9mo(lo90^7xzcy9k!kk)2&lgd*h!)f2_0n&r*254"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# AUTHENTICATION_BACKENDS = [
#     'admissionApp.backends.AdmissionBackend',  # Your custom backend
#     'django.contrib.auth.backends.ModelBackend',  # Default backend
# ]

# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    'userApp',
    'paymentApp',
    'recordApp',
    'adminApp',
    'admissionApp',

    'django_countries',
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "sch.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": ['%s/templates/' %(PROJECT_DIR),],
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

WSGI_APPLICATION = "sch.wsgi.application"


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": 'sch_db',
        'USER' : 'root',
        'PASSWORD' : 'ben_ayo002',
        'HOST' : 'localhost',
        'PORT' : '3306',
        'OPTIONS' : {
            'autocommit' : True
        },
    }
}

# Email Backend Configuration
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


"""

# Gmail

EMAIL_BACKEND = 'django.core.mail.backends.stmp.EmailBackend' # Replace with your preference
EMAIL_PORT = 587 # Replace with your email port
EMAIL_USE_TLS = True # Set to False if your email doesn't use TLS
EMAIL_HOST = 'stmp.gmail.com' #Replace with your email host for gmail -> 'stmp.gmail.com'
EMAIL_HOST_USER = 'shopping@gmail.com' # Replace with your email username
EMAIL_HOST_PASSWORD = 'shop1234' # Replace with your email password
DEFAULT_FROM_EMAIl = 'shopping@gmail.com'


# mailtrap

EMAIL_HOST = 'sandbox.smtp.mailtrap.io'
EMAIL_HOST_USER = '5893b28ff5a810'
EMAIL_HOST_PASSWORD = '********538d'
EMAIL_PORT = '2525'


"""


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = "static/"
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]

MEDIA_URL = 'media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# login and logout
LOGIN_URL = 'admission_login'
LOGIN_REDIRECT_URL = 'home'
LOGOUT_REDIRECT_URL = 'login'
