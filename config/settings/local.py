from config.settings.base import *

# Development specific settings

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env.bool("DEBUG", default=False)

ALLOWED_HOSTS = env.str("DJANGO_ALLOWED_HOSTS").split(" ")

ADMINS = [
    (
        env.str("WEBMASTER_NAME", default="Webmaster"),
        env.str("WEBMASTER_EMAIL", default="webmaster@test.infroid.com")
    ),
    (
        env.str("ADMINISTRATOR_NAME", default="Administrator"),
        env.str("ADMINISTRATOR_EMAIL", default="administrator@test.infroid.com")
    )
]

# Add INSTALLED_APPS on top
INSTALLED_APPS = [] + INSTALLED_APPS
# Add INSTALLED_APPS at bottom
INSTALLED_APPS += ['django_extensions', ]

# Add MIDDLEWARE on top
MIDDLEWARE = [] + MIDDLEWARE
# Add MIDDLEWARE at bottom
MIDDLEWARE += []

ROOT_URLCONF = 'config.urls.local'

WSGI_APPLICATION = 'config.wsgi.application'

# django-allauth config
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
