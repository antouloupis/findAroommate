import os
from pathlib import Path
from decouple import config,RepositoryEnv,Config

config = Config(RepositoryEnv('.env.prod'))

SECRET_KEY = config('SECRET_KEY')

BASE_DIR = Path(__file__).resolve().parent.parent

# Setup variables from .env 
# Path to login url
LOGIN_URL = '/account/login/'

# Debug setting
DEBUG = config('DEBUG', default=False, cast=bool)

# Allowed hosts
ALLOWED_HOSTS = config('ALLOWED_HOSTS').split(',')

AUTH_USER_MODEL = 'account.CustomUser'

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'core',
    'account',
    'listings',
    'search',
    'profiles',
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

ROOT_URLCONF = 'findaroommate.urls'

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

WSGI_APPLICATION = 'findaroommate.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': config('SQL_ENGINE'),
        'NAME': config('SQL_DATABASE'),  # Create this database in your Postgres container
        'USER': config('SQL_USER'),  # Set this user in your Postgres container
        'PASSWORD': config('SQL_PASSWORD'),  # Set this password in your Postgres container
        'HOST': config('SQL_HOST'),  # Use 'db' because this will be the service name in Docker Compose
        'PORT': config('SQL_PORT'),
    }
}

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


LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


STATIC_URL = 'static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]
STATIC_ROOT = os.path.join(BASE_DIR, 'assets')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

#EMAIL CONFIG

EMAIL_FROM_USER=config('EMAIL_FROM_USER')
EMAIL_HOST=config('EMAIL_HOST')
EMAIL_HOST_USER=config('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD=config('EMAIL_HOST_PASSWORD')
EMAIL_USE_TLS=config('EMAIL_USE_TLS')
EMAIL_PORT=config('EMAIL_PORT')