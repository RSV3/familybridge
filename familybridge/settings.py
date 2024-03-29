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
  from familybridge.settings_debug import *
except Exception as e:
  print e

TEMPLATE_DEBUG = DEBUG

# For testing real send
#EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
#EMAIL_HOST = 'smtp.gmail.com'
#EMAIL_PORT = 587
#EMAIL_HOST_USER = 'tech@vinely.com'
#EMAIL_HOST_PASSWORD = ''
#EMAIL_USE_TLS = True

if DEPLOY:
  # SENDGRID
  EMAIL_HOST = 'smtp.sendgrid.net'
  EMAIL_PORT = '587'
  EMAIL_HOST_USER = os.environ.get('SENDGRID_USERNAME')
  EMAIL_HOST_PASSWORD = os.environ.get('SENDGRID_PASSWORD')
  EMAIL_USE_TLS = True
else:
  EMAIL_BACKEND = 'core.backends.EmailSinkBackend'
  EMAIL_HOST = 'smtp.gmail.com'
  EMAIL_PORT = 587
  EMAIL_HOST_USER = 'familybridge@redstar.com'
  EMAIL_HOST_PASSWORD = 'bridge2elderly'
  EMAIL_USE_TLS = True
  EMAIL_TEST_ACCOUNT = 'familybridgetesting@gmail.com'

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
  'django.contrib.humanize',
  #'south',
  'sorl.thumbnail',
  #'storages',
  's3_folder_storage',
  'gunicorn',
  'compressor',
  'djcelery',
  'django_tables2',
  'core',
  'mobile',
  'expense',
  'setup',
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

DEFAULT_FROM_EMAIL = 'familybridge@redstar.com'

# Database
# https://docs.djangoproject.com/en/dev/ref/settings/#databases
import dj_database_url

DATABASES = {'default': dj_database_url.config(default="sqlite:///./familybridge.sqlite")}

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

import django.conf.global_settings as DEFAULT_SETTINGS

TEMPLATE_CONTEXT_PROCESSORS = DEFAULT_SETTINGS.TEMPLATE_CONTEXT_PROCESSORS + (
  "django.core.context_processors.request",
)

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
  # assets for staging server
  AWS_STORAGE_BUCKET_NAME = 'cdn.staging.familybridge.redstar.com'

if DEPLOY:
  # for handling https static file serving
  from boto.s3.connection import OrdinaryCallingFormat
  AWS_S3_CALLING_FORMAT = OrdinaryCallingFormat()
else:
  # for static files to serve from http
  AWS_S3_SECURE_URLS = False

MEDIA_ROOT = '/%s/' % DEFAULT_S3_PATH
MEDIA_URL = '//s3.amazonaws.com/%s/media/' % AWS_STORAGE_BUCKET_NAME
STATIC_ROOT = "/%s/" % STATIC_S3_PATH
STATIC_URL = '//s3.amazonaws.com/%s/static/' % AWS_STORAGE_BUCKET_NAME
ADMIN_MEDIA_PREFIX = STATIC_URL + 'admin/'

STATICFILES_FINDERS = (
  'django.contrib.staticfiles.finders.FileSystemFinder',
  'django.contrib.staticfiles.finders.AppDirectoriesFinder',
  #'django.contrib.staticfiles.finders.DefaultStorageFinder',
  'compressor.finders.CompressorFinder',
)

STATICFILES_DIRS = (
  os.path.join(BASE_DIR, "static"),
)

ADMINS = (
  ('Kwan Lee', 'kwan@redstar.com'),
  ('David Rabinowitz', 'david@redstar.com'),
  ('Gemma Sole', 'gemma@redstar.com'),
)

AUTH_USER_MODEL = 'core.EmailUser'
LOGIN_REDIRECT_URL = '/home/'

# keep this at the bottom
try:
  from familybridge.settings_local import *
  print "Imported local settings"
  INSTALLED_APPS += ADDITIONAL_APPS
except Exception as e:
  print e

try:
  from familybridge.settings_project import *
  print "Imported project specific settings"
except Exception as e:
  print e
