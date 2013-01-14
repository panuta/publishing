# -*- encoding: utf-8 -*-

import os
base_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), os.path.pardir)

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('Panu Tangchalermkul', 'panuta@gmail.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'publishing',
        'USER': 'publishing',
        'PASSWORD': 'publishing',
        'HOST': '',
        'PORT': '',
    }
}

WEBSITE_NAME = 'Publishing'
WEBSITE_DOMAIN = 'http://127.0.0.1:8000'

TIME_ZONE = 'Asia/Bangkok'
LANGUAGE_CODE = 'en-us'

SITE_ID = 1
USE_I18N = True
USE_L10N = True
USE_TZ = True

MEDIA_ROOT = os.path.join(base_path, 'media')
MEDIA_URL = '/media/'

STATIC_ROOT = os.path.join(base_path, 'sitestatic/')
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(base_path, 'static'),
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

SECRET_KEY = 'THIS_IS_SECRET_KEY'

AUTH_USER_MODEL = 'domain.UserAccount'
LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL = 'view_my_library_room'

AUTHENTICATION_BACKENDS = (
    'publishing.backends.EmailAuthenticationBackend',
    'django.contrib.auth.backends.ModelBackend',
)

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.request',
    'django.core.context_processors.static',
    'django.core.context_processors.tz',
    'django.contrib.messages.context_processors.messages',
    'publishing.context_processors.settings',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.middleware.transaction.TransactionMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

ROOT_URLCONF = 'publishing.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'publishing.wsgi.application'

TEMPLATE_DIRS = (
    os.path.join(base_path, 'templates'),
)

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.messages',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.staticfiles',
    'django.contrib.markup',

    'easy_thumbnails',

    'accounts',
    'domain',
    'common',
    'presentation',
)

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

# EMAIL ################################################################################################################

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
NOREPLY_EMAIL = 'noreply@localhost'

"""
# THUMBNAILS ###########################################################################################################

THUMBNAIL_PRESERVE_EXTENSIONS = ('png',)

THUMBNAIL_ALIASES = {
    '': {
        'avatar_normal': {'size': (100, 100), 'crop': True},
        'avatar_small': {'size': (75, 75), 'crop': True},
        'avatar_smaller': {'size': (45, 45), 'crop': True},
        'avatar_tiny': {'size': (30, 30), 'crop': True},

        'publication_cover_large': {'size': (170, 170), 'crop': True},
        'publication_cover_normal': {'size': (140, 140), 'crop': True},
        'publication_cover_small': {'size': (70, 70), 'crop': True},
        },
    }

# PUBLISHING SETTINGS ##################################################################################################

# AVATAR

USER_AVATAR_ROOT = 'users'

USER_AVATAR_DEFAULT_NORMAL = 'avatar/default_normal.png'
USER_AVATAR_DEFAULT_SMALL = 'avatar/default_small.png'
USER_AVATAR_DEFAULT_SMALLER = 'avatar/default_smaller.png'
USER_AVATAR_DEFAULT_TINY = 'avatar/default_tiny.png'

# PUBLICATION

PUBLICATION_COVER_ROOT = 'publications'

PUBLICATION_COVER_DEFAULT_LARGE = 'publication/default_cover_large.png'
PUBLICATION_COVER_DEFAULT_NORMAL = 'publication/default_cover_normal.png'
PUBLICATION_COVER_DEFAULT_SMALL = 'publication/default_cover_small.png'
"""


try:
    from settings_local import *
except ImportError:
    pass