"""
Django settings for as207960_domains project.

Generated by 'django-admin startproject' using Django 3.0.5.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os
import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration
import logging

from django_countries.widgets import LazyChoicesMixin

LazyChoicesMixin.get_choices = lambda self: self._choices
LazyChoicesMixin.choices = property(LazyChoicesMixin.get_choices, LazyChoicesMixin.set_choices)


# logging.basicConfig(level=logging.DEBUG)

sentry_sdk.init(
    dsn="https://da23a217b5584ccaa296aea526e3fc2c@o222429.ingest.sentry.io/5247893",
    integrations=[DjangoIntegration()],
    send_default_pii=True
)


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv("SECRET_KEY", "")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = os.getenv("HOST", "domains.as207960.net").split(",")

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django_keycloak_auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'django.contrib.postgres',
    'phonenumber_field',
    'crispy_forms',
    'django_countries',
    'django_grpc',
    'rest_framework',
    'crispy_bootstrap5',
    'domains'
]

MIDDLEWARE = [
    'xff.middleware.XForwardedForMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    "django_keycloak_auth.middleware.OIDCMiddleware",
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'domains.exception_logging_middleware.ExceptionLoggingMiddleware',
    'domains.middleware.CountryMiddleware',
]

ROOT_URLCONF = 'as207960_domains.urls'

AUTHENTICATION_BACKENDS = ["django_keycloak_auth.auth.KeycloakAuthorization"]

LOGIN_URL = "oidc_login"
LOGOUT_REDIRECT_URL = "oidc_login"

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'as207960_domains.wsgi.application'

GRPCSERVER = {
    'servicers': ['domains.rdap.grpc_hook'],
    'maximum_concurrent_rpcs': None,
}

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        "ENGINE": "django_cockroachdb",
        "HOST": os.getenv("DB_HOST", "localhost"),
        "NAME": os.getenv("DB_NAME", "domains"),
        "USER": os.getenv("DB_USER", "domains"),
        "PASSWORD": os.getenv("DB_PASS"),
        "PORT": '26257',
        "OPTIONS": {
            "application_name": os.getenv("APP_NAME", "domains")
        }
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-gb'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

EXTERNAL_URL_BASE = os.getenv("EXTERNAL_URL", f"https://{ALLOWED_HOSTS[0]}")
RP_ID = os.getenv("RP_ID", ALLOWED_HOSTS[0])

STATIC_URL = os.getenv("STATIC_URL", f"{EXTERNAL_URL_BASE}/static/")
MEDIA_URL = os.getenv("MEDIA_URL", f"{EXTERNAL_URL_BASE}/media/")

AWS_S3_CUSTOM_DOMAIN = os.getenv("S3_CUSTOM_DOMAIN", "")
AWS_QUERYSTRING_AUTH = False
AWS_S3_REGION_NAME = os.getenv("S3_REGION", "")
AWS_S3_ENDPOINT_URL = os.getenv("S3_ENDPOINT", "")
AWS_STORAGE_BUCKET_NAME = os.getenv("S3_BUCKET", "")
AWS_S3_ACCESS_KEY_ID = os.getenv("S3_ACCESS_KEY_ID", "")
AWS_S3_SECRET_ACCESS_KEY = os.getenv("S3_SECRET_ACCESS_KEY", "")
AWS_S3_ADDRESSING_STYLE = "virtual"
AWS_S3_SIGNATURE_VERSION = "s3v4"

STORAGES = {
    "default": {"BACKEND": "storages.backends.s3boto3.S3Boto3Storage"},
    "staticfiles": {"BACKEND": "storages.backends.s3boto3.S3ManifestStaticStorage"}
}

KEYCLOAK_SERVER_URL = os.getenv("KEYCLOAK_SERVER_URL")
KEYCLOAK_REALM = os.getenv("KEYCLOAK_REALM")
OIDC_CLIENT_ID = os.getenv("KEYCLOAK_CLIENT_ID")
OIDC_CLIENT_SECRET = os.getenv("KEYCLOAK_CLIENT_SECRET")
OIDC_SCOPES = os.getenv("KEYCLOAK_SCOPES")

PHONENUMBER_DEFAULT_REGION = "GB"
CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
CRISPY_TEMPLATE_PACK = "bootstrap5"
CRISPY_FAIL_SILENTLY = not DEBUG

XFF_TRUSTED_PROXY_DEPTH = 1
XFF_NO_SPOOFING = True
XFF_HEADER_REQUIRED = True

REGISTRATION_ENABLED = True
REGISTRY_LOCK_ENABLED = True
EPP_PROXY_ADDR = os.getenv("EPP_PROXY_ADDR")
EPP_PROXY_CA = os.getenv("EPP_PROXY_CA")

DEFAULT_FROM_EMAIL = os.getenv("EMAIL_FROM", "AS207960 Domains <domains@as207960.net>")

LISTMONK_TEMPLATE_ID = int(os.getenv("LISTMONK_TEMPLATE_ID"))
LISTMONK_URL = os.getenv("LISTMONK_URL")

GCHAT_SERVICE_ACCOUNT = os.getenv("GCHAT_SERVICE_ACCOUNT_FILE")
GCHAT_PROJECT_ID = os.getenv("GCHAT_PROJECT_ID")

PRIV_KEY_LOCATION = os.getenv("PRIV_KEY_LOCATION")

with open(PRIV_KEY_LOCATION, "rb") as f:
    JWT_PRIV_KEY = f.read()

VERISIGN_NS_API_KEY = os.getenv("VERISIGN_NS_API_KEY")

BILLING_URL = os.getenv("BILLING_URL")
HEXDNS_URL = os.getenv("HEXDNS_URL")
FEEDBACK_URL = os.getenv("FEEDBACK_URL")
PAT_URL = os.getenv("PAT_URL")

CELERY_RESULT_BACKEND = "rpc://"
CELERY_BROKER_URL = os.getenv("CELERY_BROKER_URL")
CELERY_TASK_SERIALIZER = "json"
CELERY_ACCEPT_CONTENT = ["json"]

RESOLVER_ADDR = os.getenv("RESOLVER_ADDR")
RESOLVER_PORT = int(os.getenv("RESOLVER_PORT"))

RRPPROXY_USER = os.getenv("RRPPROXY_USER")
RRPPROXY_PASS = os.getenv("RRPPROXY_PASS")

RABBITMQ_RPC_URL = os.getenv("RABBITMQ_RPC_URL")

POSTAL_PUBLIC_KEY = os.getenv("POSTAL_PUBLIC_KEY")

ISNIC_CONTACT_EMAIL = os.getenv("ISNIC_CONTACT_EMAIL") or "isnic-auto@as207960.ltd.uk"
RDAP_OBJECT_TAG = os.getenv("RDAP_OBJECT_TAG") or "GLAUCA"

REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
    ],
    'DEFAULT_PARSER_CLASSES': [
        'rest_framework.parsers.JSONParser',
        'rest_framework.parsers.FormParser',
        'rest_framework.parsers.MultiPartParser'
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'as207960_utils.api.auth.BearerAuthentication',
        'as207960_utils.api.auth.PATAuthentication',
        'as207960_utils.api.auth.SessionAuthentication',
    ] if PAT_URL else [
        'as207960_utils.api.auth.BearerAuthentication',
        'as207960_utils.api.auth.SessionAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny',
    ],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'EXCEPTION_HANDLER': 'domains.api.exceptions.exception_handler',
    'PAGE_SIZE': 25
}

LOGGING = {
	'version': 1,
	'disable_existing_loggers': False,
	'filters': {
		'require_debug_false': {
			'()': 'django.utils.log.RequireDebugFalse',
		},
		'require_debug_true': {
			'()': 'django.utils.log.RequireDebugTrue',
		},
	},
	'formatters': {
		'django.server': {
			'()': 'django.utils.log.ServerFormatter',
			'format': '[%(server_time)s] %(message)s',
		}
	},
	'handlers': {
		'console': {
			'level': 'INFO',
			'filters': ['require_debug_true'],
			'class': 'logging.StreamHandler',
		},
		'console_debug_false': {
			'level': 'ERROR',
			'filters': ['require_debug_false'],
			'class': 'logging.StreamHandler',
		},
		'django.server': {
			'level': 'INFO',
			'class': 'logging.StreamHandler',
			'formatter': 'django.server',
		},
	},
	'loggers': {
		'django': {
			'handlers': ['console', 'console_debug_false'],
			'level': 'INFO',
		},
		'django.server': {
			'handlers': ['django.server'],
			'level': 'INFO',
			'propagate': False,
		}
	}
}

DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'

AFNIC_PROXY_CONTACT = os.getenv("AFNIC_PROXY_CONTACT")
EURID_PROXY_CONTACT = os.getenv("EURID_PROXY_CONTACT")
EURID_BILLING_CONTACT = os.getenv("EURID_BILLING_CONTACT")

SWITCH_REGISTRAR_ID = os.getenv("SWITCH_REGISTRAR_ID")
SWITCH_REGISTRAR_PASSWORD = os.getenv("SWITCH_REGISTRAR_PASSWORD")