from pathlib import Path
from django.utils.timezone import timedelta
from dotenv import load_dotenv
import os

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.getenv('SECRET_KEY')

DEBUG = True

ALLOWED_HOSTS = []


INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
	'django.contrib.staticfiles',
	
    'habit',
    'telegram',
    'users',

    'drf_yasg',
	'corsheaders',
	'rest_framework',
	'django_filters',
	'rest_framework_simplejwt',
    'crispy_forms',
	'crispy_bootstrap5',
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",

    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',

    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "config.urls"

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

WSGI_APPLICATION = "config.wsgi.application"


DATABASES = {
	'default': {
	'ENGINE': os.getenv('DB_ENGINE'),
	'NAME': os.getenv('DB_NAME'),
	'USER': os.getenv('DB_USER'),
	'PASSWORD': os.getenv('DB_PASSWORD'),
	'HOST': os.getenv('DB_HOST'),
	'PORT': os.getenv('DB_PORT'),
	'ATOMIC_REQUESTS': True
	}
}


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


LANGUAGE_CODE = "ru-ru"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


STATIC_URL = 'static/'
STATICFILES_DIRS = (
	BASE_DIR / 'static',
)


DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

CORS_ALLOWED_ORIGINS = [
    'http://localhost:8000',
    'https://read-and-write.example.com',
]

CSRF_TRUSTED_ORIGINS = [
    "https://read-and-write.example.com", 
]

CORS_ALLOW_ALL_ORIGINS = False

REST_FRAMEWORK = {
	'DATETIME_FORMAT': '%Y-%m-%d %H:%M:%S',
	'DATE_FORMAT': '%Y-%m-%d',
	'TIME_FORMAT': '%H:%M',
    'DEFAULT_FILTER_BACKENDS': (
        'django_filters.rest_framework.DjangoFilterBackend',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        # 'rest_framework.permissions.IsAuthenticated',
        'rest_framework.permissions.AllowAny',
    ),
}

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=15),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
} 


AUTH_USER_MODEL = 'users.User'
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'
LOGIN_URL = '/users/'

CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
CRISPY_TEMPLATE_PACK = "bootstrap5"

CACHE_ENABLED = os.getenv('CACHE_ENABLED')  == 'True'
if CACHE_ENABLED:
    CACHES = {
        "default": {
            "BACKEND": os.getenv('CACHES_BACKEND'),
            "LOCATION": os.getenv('CACHES_LOCATION'),
            "TIMEOUT": os.getenv('CACHES_TIMEOUT')
        }
    }
CELERY_BROKER_URL = os.getenv('CELERY_BROKER_URL')
CELERY_RESULT_BACKEND = os.getenv('CELERY_RESULT_BACKEND')

MAX_FREQUENCY = 7
MAX_TIME_REQUIRED = 120
TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
ADMIN_TELEGRAM_CHAT_ID = os.getenv('ADMIN_TELEGRAM_CHAT_ID')