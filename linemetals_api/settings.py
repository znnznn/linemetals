import pyodbc
from pathlib import Path
from decouple import config


BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = config('SECRET_KEY')

DEBUG = config('DEBUG', default=False, cast=bool)

ALLOWED_HOSTS = [
    "*",
]

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Third party
    'rest_framework',

    # Our apps
    'users',
    'origindb',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
AUTH_USER_MODEL = "users.User"
ROOT_URLCONF = 'linemetals_api.urls'
MEDIA_URL = '/media/'
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'static'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'linemetals_api.wsgi.application'

DATABASES = {
    "default": {
        "ENGINE": "mssql",
        "NAME": config("DATABASE_NAME"),
        "USER": config("DATABASE_USER"),
        "PASSWORD": config("MSSQL_SA_PASSWORD"),
        "HOST": config("DATABASE_HOST"),
        "PORT": config("DATABASE_PORT", default=1433, cast=int),
        "OPTIONS": {
            "unicode_results": True,
            "driver": "ODBC Driver 17 for SQL Server",
            "setdecoding": [
                {"sqltype": pyodbc.SQL_CHAR, "encoding": 'utf-8'},
                {"sqltype": pyodbc.SQL_WCHAR, "encoding": 'utf-8'},
            ],
            "setencoding": [
                {"encoding": "utf-8"}],
        }
        ,
    },
}


# Password validation
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
LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

REST_FRAMEWORK = {
    "DEFAULT_PERMISSION_CLASSES": ("rest_framework.permissions.IsAuthenticated",),
    "DEFAULT_AUTHENTICATION_CLASSES": ("auth.authentication.TokenAuthentication",),
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.LimitOffsetPagination",
    "PAGE_SIZE": 20,
}
