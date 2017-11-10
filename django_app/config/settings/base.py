"""
Django settings for Monaegi-Usedbookstore project.

Generated by 'django-admin startproject' using Django 1.11.3.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""
import json
import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# django_app/templates
TEMPLATE_DIR = os.path.join(BASE_DIR, 'templates')
# django_app/static
STATIC_DIR = os.path.join(BASE_DIR, 'static')

STATICFILES_DIRS = [
    STATIC_DIR,
]

ROOT_DIR = os.path.dirname(BASE_DIR)

CONFIG_SECRET_DIR = os.path.join(ROOT_DIR, '.config_secret')
CONFIG_SECRET_COMMON_FILE = os.path.join(CONFIG_SECRET_DIR, 'settings_common.json')
CONFIG_SECRET_DEBUG_FILE = os.path.join(CONFIG_SECRET_DIR, 'settings_debug.json')
CONFIG_SECRET_DEPLOY_FILE = os.path.join(CONFIG_SECRET_DIR, 'settings_deploy.json')

config_secret_common = json.loads(open(CONFIG_SECRET_COMMON_FILE).read())

SECRET_KEY = config_secret_common['django']['secret_key']

##
# 외부 API
##
API_SECRET_KEYS_FILE = os.path.join(CONFIG_SECRET_DIR, 'api_secret_keys.json')
api_secret_keys = json.loads(open(API_SECRET_KEYS_FILE).read())

# Naver
NAVER_CLIENT_ID = api_secret_keys['naver']['client_id']
NAVER_CLIENT_SECRET = api_secret_keys['naver']['client_secret']

# Facebook
FACEBOOK_APP_ID = api_secret_keys['facebook']['app_id']
FACEBOOK_SECRET_CODE = api_secret_keys['facebook']['secret_key']

# Kakao
KAKAO_APP_ID = api_secret_keys['kakao']['app_id']
KAKAO_CLIENT_SECRET = api_secret_keys['kakao']['client_secret']


# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',

    'django_messages',

    'member',
    'book',
]

SITE_ID = 1

AUTH_USER_MODEL = 'member.MyUser'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            TEMPLATE_DIR,
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',

                # Custom context processors
                'django_messages.context_processors.inbox',
                'utils.context_processors.social_login.facebook_tag',
                'utils.context_processors.social_login.kakao_tag',
            ],
            # 'libraries': {
            #     'book_tags': 'book.book_tags',
            # },
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'

# ...

ENDLESS_PAGINATION_PER_PAGE = 8


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'ko-kr'

TIME_ZONE = 'Asia/Seoul'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Email_Backend
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = config_secret_common['django']['email_host_user']
EMAIL_HOST_PASSWORD = config_secret_common['django']['email_host_password']
EMAIL_PORT = '587'
