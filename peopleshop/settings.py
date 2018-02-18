"""
Django settings for peopleshop project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""
import os
from os.path import dirname, join


BASE_DIR = dirname(dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'b-4w@s(qw@7tdn#=i&amp;lh9!2im6u(p_d_x64l*rwcxn_$ej237q'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['52.42.172.130', 'peopleshop.gq', 'www.peopleshop.gq', 'localhost']


# Application definition
INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'bootstrap3', # optional module for making bootstrap forms easier

    'allauth',
    'allauth.account',
    'allauth.socialaccount',



    'allauth.socialaccount.providers.facebook',  # enabled by configure


    'allauth.socialaccount.providers.google',  # enabled by configure

    #'allauth.socialaccount.providers.dropbox',
    #'allauth.socialaccount.providers.github',
    #'allauth.socialaccount.providers.linkedin',
    # etc


    # 'allauthdemo.auth',
    # 'allauthdemo.demo',

    'apps.auth',
    'apps.demo',
    'apps.main',
    'apps.selling',

    'storages',
)

AWS_STORAGE_BUCKET_NAME = 'peopleshopmedia'
AWS_S3_REGION_NAME = 'us-west-2'  # e.g. us-east-2
AWS_ACCESS_KEY_ID = 'AKIAIFMADSVAG7EIMBMQ'
AWS_SECRET_ACCESS_KEY = 'GcL8sueE3a00cOwOiSB7096f5sGrUOA8pdUIaW6V'

# Tell django-storages the domain to use to refer to static files.
AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME

# Tell the staticfiles app to use S3Boto3 storage when writing the collected static files (when
# you run `collectstatic`).
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

STATICFILES_LOCATION = 'static'
STATICFILES_STORAGE = 'custom_storages.StaticStorage'

MEDIAFILES_LOCATION = 'media'
DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
CORS_ORIGIN_ALLOW_ALL = True

ROOT_URLCONF = 'peopleshop.urls'

WSGI_APPLICATION = 'peopleshop.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = '/static/'

# Authentication

AUTHENTICATION_BACKENDS = (
    "allauth.account.auth_backends.AuthenticationBackend",
)

TEMPLATES = [
    {
    #'TEMPLATE_DEBUG': True,
    'BACKEND': 'django.template.backends.django.DjangoTemplates',
    'DIRS': [
        # allauth templates: you could copy this directory into your
        # project and tweak it according to your needs
        # join(PROJECT_ROOT, 'templates', 'uniform', 'allauth'),
        # example project specific templates
        join(BASE_DIR, 'peopleshop', 'templates', 'plain', 'example'),
        #join(BASE_DIR, 'peopleshop', 'templates', 'bootstrap', 'allauth'),
        join(BASE_DIR, 'peopleshop', 'templates', 'allauth'),
        join(BASE_DIR, 'peopleshop', 'templates'),
    ],
    'APP_DIRS': True,
    'OPTIONS': {
        'context_processors': [
            # needed for admin templates
            'django.contrib.auth.context_processors.auth',
            # these *may* not be needed
            'django.template.context_processors.debug',
            'django.template.context_processors.i18n',
            'django.template.context_processors.media',
            'django.template.context_processors.static',
            'django.template.context_processors.tz',
            'django.contrib.messages.context_processors.messages',
            # allauth needs this from django
            'django.template.context_processors.request',
            # allauth specific context processors
            #'allauth.account.context_processors.account',
            #'allauth.socialaccount.context_processors.socialaccount',
          ],
       },
    }
]

MESSAGE_STORAGE = 'django.contrib.messages.storage.session.SessionStorage'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.yandex.com'
EMAIL_PORT = 465
EMAIL_HOST_USER = 'info@peopleshop.gq'
EMAIL_HOST_PASSWORD = 'delorean1107'
EMAIL_USE_SSL = True

DEFAULT_FROM_EMAIL = 'info@peopleshop.gq'
ADMINS = (
    ('People Shop', 'admin@peopleshop.gq'),
)

STATICFILES_DIRS = (
    join(BASE_DIR, "static"),
)

SITE_ID = 1
AUTH_USER_MODEL = 'allauthdemo_auth.User'
LOGIN_REDIRECT_URL = '/member/'
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_USERNAME_MIN_LENGTH = 3
# ACCOUNT_EMAIL_VERIFICATION = 'none'  # testing...
ACCOUNT_USER_MODEL_USERNAME_FIELD = None
SOCIALACCOUNT_AUTO_SIGNUP = False  # require social accounts to use the signup form ... I think
# For custom sign-up form:
# http://stackoverflow.com/questions/12303478/how-to-customize-user-profile-when-using-django-allauth
SOCIALACCOUNT_PROVIDERS = {
    'facebook': {
        'SCOPE': ['email'],  #, 'publish_stream'],
        'METHOD': 'oauth2'  # 'js_sdk'  # instead of 'oauth2'
    },
    'google':
        { 'SCOPE': ['profile', 'email'],
        'AUTH_PARAMS': { 'access_type': 'online' }
    },
}
