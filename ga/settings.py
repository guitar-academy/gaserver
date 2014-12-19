"""
Django settings for ga project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '@2hoo4y@n90_obdnm=%)+kuv_8_f0q$q_hp_8rc46ul%z5_hp='

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = (
    # Django Internal Contrib Applications
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',

    # Third Party Applications
    'django_extensions',
    'rest_framework',
    'rest_framework.authtoken',
    'social.apps.django_app.default',

    # Guitar Academy Applications
    'accounts',
    'training',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'ga.urls'

WSGI_APPLICATION = 'ga.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'

# HTML Templates
TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'templates'),
)

# Site Name
SITE_ID = 1

# Template Context
TEMPLATE_CONTEXT_PROCESSORS = (
    # Django core/contrib context
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.core.context_processors.tz",
    "django.contrib.messages.context_processors.messages",

    # Third party context
    'social.apps.django_app.context_processors.backends',
    'social.apps.django_app.context_processors.login_redirect',

    # Guitar Academy internal context
    'ga.context_processors.site',
)


# User Authentication
AUTHENTICATION_BACKENDS = (
    'social.backends.facebook.FacebookAppOAuth2',
    'social.backends.facebook.FacebookOAuth2',
#    'social.backends.google.GoogleOAuth',
#    'social.backends.google.GoogleOAuth2',
#    'social.backends.google.GoogleOpenId',
#    'social.backends.google.GooglePlusAuth',
#    'social.backends.google.GoogleOpenIdConnect',
    'django.contrib.auth.backends.ModelBackend',
)

AUTH_USER_MODEL = 'accounts.User'
LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL = '/profile/'
SOCIAL_AUTH_URL_NAMESPACE = 'social'
SOCIAL_AUTH_FACEBOOK_KEY = os.getenv('FACEBOOK_KEY', '')
SOCIAL_AUTH_FACEBOOK_SECRET = os.getenv('FACEBOOK_SECRET', '')
SOCIAL_AUTH_FACEBOOK_SCOPE = ['email']
SOCIAL_AUTH_LOGIN_ERROR_URL = '/social-auth/login-error/'
SOCIAL_AUTH_LOGIN_URL = '/social-auth/login/'
#SOCIAL_AUTH_NEW_USER_REDIRECT_URL = '/social-auth/new-users/'
#SOCIAL_AUTH_NEW_ASSOCIATION_REDIRECT_URL = '/social-auth/new-association/'
#SOCIAL_AUTH_DISCONNECT_REDIRECT_URL = '/social-auth/account-disconnected/'
#SOCIAL_AUTH_INACTIVE_USER_URL = '/social-auth/inactive-user/'

# Django Rest Framework Configuration
REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
        'ga.renderers.GABrowsableAPIRenderer',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.TokenAuthentication',
    )
}

# Fixture Directory (Initial Data, Dump Data, Test Data, etc.)
FIXTURE_DIRS = (
    os.path.join(BASE_DIR, 'fixtures'),
)

try:
    LOCAL_SETTINGS
except NameError:
    try:
        from .local_settings import *
    except ImportError:
        pass
