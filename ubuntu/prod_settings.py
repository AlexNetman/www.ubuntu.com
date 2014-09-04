"""
Django settings for ubuntu project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Keep it secret, keep it safe!
SECRET_KEY = 'g@=8y0p%v6hsk6n1p*^tqb@)g1#v7r!#e1x5^x!$bvm#u9hal4'

# See https://docs.djangoproject.com/en/dev/ref/contrib/
INSTALLED_APPS = [
    'django.contrib.staticfiles',  # Needed for STATICFILES_DIRS to work
    'template_extensions'
]

DEBUG = True
ROOT_URLCONF = 'ubuntu.urls'
WSGI_APPLICATION = 'ubuntu.wsgi.application'
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = False
USE_L10N = False
USE_TZ = False
STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]
TEMPLATE_DIRS = [os.path.join(BASE_DIR, "templates")]

MIDDLEWARE_CLASSES = []

# See http://tinyurl.com/django-context-processors
TEMPLATE_CONTEXT_PROCESSORS = [
    "django.core.context_processors.static",     # {{ STATIC_URL }}
    "django.core.context_processors.request",    # {{ request }} object
    "template_extensions.asset_server_url",  # {{ ASSET_SERVER_URL }}
]