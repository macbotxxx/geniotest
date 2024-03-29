"""
Django settings for config project.

Generated by 'django-admin startproject' using Django 5.0.1.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""
import environ
import os

from pathlib import Path
from .apps import *
from datetime import timedelta


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Take environment variables from .env file
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))
env = environ.Env()


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# localhost email
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'sandbox.smtp.mailtrap.io'
EMAIL_HOST_USER = 'f7f1d4d566645a'
EMAIL_HOST_PASSWORD = '1917db4a003d90'
EMAIL_PORT = '2525'


ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,"templates")],
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


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Celery settings
CELERY_BROKER_URL = "redis://localhost:6379"
CELERY_RESULT_BACKEND = CELERY_BROKER_URL

CELERY_BROKER_CONNECTION_RETRY_ON_STARTUP = True
CELERY_RESULT_BACKEND_MAX_RETRIES = 10
CELERY_ACCEPT_CONTENT = ["json"]
CELERY_TASK_SERIALIZER = "json"
CELERY_RESULT_SERIALIZER = "json"
CELERY_TASK_TIME_LIMIT = 5 * 60
CELERY_TASK_SOFT_TIME_LIMIT = 60
CELERY_BEAT_SCHEDULER = "django_celery_beat.schedulers:DatabaseScheduler"
CELERY_WORKER_SEND_TASK_EVENTS = True
CELERY_TASK_SEND_SENT_EVENT = True
CELERY_RESULT_EXTENDED = True

SESSION_ENGINE = "django.contrib.sessions.backends.cache"
SESSION_CACHE_ALIAS = "default"


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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

AUTH_USER_MODEL = 'account.User'


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


CORS_ALLOWED_ORIGIN_REGEXES = [
    r"^https://\w+\.example\.com$",
]

CORS_ALLOWED_ORIGINS = [
    "http://localhost:8000",
    "http://127.0.0.1:8000",
]


CORS_ALLOW_ALL_ORIGINS = True

CORS_ALLOW_METHODS = (
    "DELETE",
    "GET",
    "OPTIONS",
    "PATCH",
    "POST",
    "PUT",
)


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    "django.middleware.locale.LocaleMiddleware",
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(days=1),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
    'ROTATE_REFRESH_TOKENS': True,
    'BLACKLIST_AFTER_ROTATION': True,
    'ALGORITHM': 'HS256',
    'UPDATE_LAST_LOGIN': True,
    'SLIDING_TOKEN_REFRESH_EXP_CLAIM': 'refresh_exp',
    'SLIDING_TOKEN_LIFETIME': timedelta(days=1),
    'SLIDING_TOKEN_REFRESH_LIFETIME': timedelta(days=1),

    'ALGORITHM': 'HS256',
    'SIGNING_KEY': "cRcpzLRunm5WJt9mRnLySoPdoM2mjFlRcuSOFbB8xOo9kLxW1JQDrT98EjLBQGfh",
    'VERIFYING_KEY': None,
    'AUDIENCE': None,
    'ISSUER': None,
    'JWK_URL': None,
    'LEEWAY': 0,

    'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',),
    'TOKEN_TYPE_CLAIM': 'token_type',
}

SWAGGER_SETTINGS = {
    "SUPPORTED_SUBMIT_METHODS": [  # Specify which methods to enable in Swagger UI
        'get',
        'post',
        'put',
        'patch',
        'destroy',
        'head',
        'delete'
    ],
    # 'LOGIN_URL': reverse_lazy('account_login'),
    # 'LOGOUT_URL': reverse_lazy('account_logout'),
    'USE_SESSION_AUTH': True,
    'JSON_EDITOR': True,
    'DOC_EXPANSION': 'none',  # ["list"*, "full", "none"]
    'REFETCH_SCHEMA_ON_LOGOUT': True,
    'SHOW_REQUEST_HEADERS': True,
    'APIS_SORTER': 'alpha',
    'DEFAULT_MODEL_DEPTH': 3,  # -1
    'DEFAULT_MODEL_RENDERING': 'example',
    'OPERATIONS_SORTER': 'None',  # [alpha, method, none],
    'TAGS_SORTER': 'alpha',
    'DEEP_LINKING': True,
    'DISPLAY_OPERATION_ID': True,
    'PERSIST_AUTHORIZATION': True,
    # 'SUPPORTED_SUBMIT_METHODS': "[\"get\", \"post\"]",
    'TRY_IT_OUT_ENABLED': True,
    'FILTER': True,
    'WITH_CREDENTIALS': True,
    'PERSIST_AUTHORIZATION': True,
    'DEFAULT_INFO': 'config.admin_api_urls',
    'COMPONENT_SPLIT_REQUEST': True,
    'HIDE_HOSTNAME': False,
    'PATH_IN_MIDDLE': False,
    'REQUIRED_PROPS_FIRST': True
}

REDOC_SETTINGS = {
    'LAZY_RENDERING': True,
    'PATH_IN_MIDDLE': True
}



REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework.authentication.SessionAuthentication",
        "rest_framework.authentication.TokenAuthentication",
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ],
    "DEFAULT_PERMISSION_CLASSES": ("rest_framework.permissions.IsAuthenticated",),

    'DEFAULT_RENDERER_CLASSES': [
        # 'djangorestframework_camel_case.render.CamelCaseJSONRenderer',
        # 'djangorestframework_camel_case.render.CamelCaseBrowsableAPIRenderer',
        'rest_framework.renderers.JSONRenderer',
        # 'rest_framework.renderers.BrowsableAPIRenderer',
        # 'core.api.renderers.CustomRenderer',
        # 'rest_framework_json_api.renderers.JSONRenderer',
        # 'rest_framework_json_api.renderers.BrowsableAPIRenderer',
    ],


    # 'DEFAULT_FILTER_BACKENDS': (
    #     'django_filters.rest_framework.DjangoFilterBackend',
    # ),
    'TEST_REQUESTS_RENDERER_CLASSES':[
        'rest_framework.renderers.MultiPartRenderer',
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.TemplateHTMLRenderer'
    ]
   
}

GENIOPAY_BASE_URL = env('GENIOPAY_BASE_URL')
GENIOPAY_SECRET_KEY = env('GENIOPAY_SECRET_KEY')
GENIOPAY_CLIENT_KEY = env('GENIOPAY_CLIENT_KEY')


