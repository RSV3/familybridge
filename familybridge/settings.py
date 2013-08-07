"""
Django settings for familybridge project.

For more information on this file, see
https://docs.djangoproject.com/en/dev/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/dev/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/dev/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '^o)l3eq8uaoidlw$^ec(-1bfh3r&pry^f4ci%(q6(l41shi#ky'


if 'DEPLOY' in os.environ and os.environ['DEPLOY'] == 'true':
  DEPLOY = True  # only True if production (for mail settings and https)
else:
  DEPLOY = False

# SECURITY WARNING: don't run with debug turned on in production!
if 'DEBUG' in os.environ and os.environ['DEBUG'] == 'true':
  DEBUG = True
else:
  DEBUG = False

try:
  from winedora.settings_debug import *
except Exception as e:
  print e

TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Uncomment the next line to enable admin documentation:
    'django.contrib.admindocs',
    #'south',
    'debug_toolbar',
    'sorl.thumbnail',
    #'storages',
    's3_folder_storage',
    'gunicorn',
    'compressor',
    'djcelery',
    'django_tables2',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'familybridge.urls'

WSGI_APPLICATION = 'familybridge.wsgi.application'


# Database
# https://docs.djangoproject.com/en/dev/ref/settings/#databases
import dj_database_url

DATABASES = {'default': dj_database_url.config()}

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Allow all host headers
ALLOWED_HOSTS = ['*']

# Internationalization
# https://docs.djangoproject.com/en/dev/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/dev/howto/static-files/

DEFAULT_FILE_STORAGE = 's3_folder_storage.s3.DefaultStorage'
DEFAULT_S3_PATH = "media"
STATICFILES_STORAGE = 's3_folder_storage.s3.StaticStorage'
STATIC_S3_PATH = "static"
AWS_ACCESS_KEY_ID = 'AKIAJJICZZXZQAAJGRIA'
AWS_SECRET_ACCESS_KEY = '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'
if DEPLOY:
  AWS_STORAGE_BUCKET_NAME = 'cdn.prod.familybridge.redstar.com'
else:
  AWS_STORAGE_BUCKET_NAME = 'cdn.staging.familybridge.redstar.com'

MEDIA_ROOT = '/%s/' % DEFAULT_S3_PATH
MEDIA_URL = '//s3.amazonaws.com/%s/media/' % AWS_STORAGE_BUCKET_NAME
STATIC_ROOT = "/%s/" % STATIC_S3_PATH
STATIC_URL = '//s3.amazonaws.com/%s/static/' % AWS_STORAGE_BUCKET_NAME
ADMIN_MEDIA_PREFIX = STATIC_URL + 'admin/'

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
    'compressor.finders.CompressorFinder',
)

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
)
try:
  from winedora.settings_local import *
except Exception as e:
  print e

