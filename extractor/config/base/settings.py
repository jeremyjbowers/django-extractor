import os
'''
Identify the project and its location on the filesystem.
'''
PROJECT_SLUG                = 'django-extractor'
PROJECT_MODULE              = 'extractor'
ROOT_URLCONF                = 'extractor.config.base.urls'
PROJECT_DIR                 = os.path.abspath(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
'''
Below is the generic project stuff. This shouldn't change between environments.
'''
TIME_ZONE                   = 'America/New_York'
LANGUAGE_CODE               = 'en-us'
SITE_ID                     = 1
USE_L10N                    = True

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.request',
    'django.core.context_processors.i18n',
    'django.contrib.messages.context_processors.messages',
)

INSTALLED_APPS = (
    'grappelli',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.admin',
    'apps.feed',
)