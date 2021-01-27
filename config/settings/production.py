from config.settings.base import *

# Production specific settings

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

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
MANAGERS = ADMINS

# Add INSTALLED_APPS on top
INSTALLED_APPS = [] + INSTALLED_APPS
# Add INSTALLED_APPS at bottom
INSTALLED_APPS += ['admin_honeypot', ]

# Add MIDDLEWARE on top
MIDDLEWARE = ['django.middleware.cache.UpdateCacheMiddleware', ] + MIDDLEWARE
# Add MIDDLEWARE at bottom
MIDDLEWARE += ['django.middleware.cache.FetchFromCacheMiddleware', ]

ROOT_URLCONF = 'config.urls.production'

# django-allauth config
# FIX-URGENT: Change to production specific email backend
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Cache config
CACHE_MIDDLEWARE_ALIAS = 'default'
CACHE_MIDDLEWARE_SECONDS = 604800
CACHE_MIDDLEWARE_KEY_PREFIX = ''

# Security config
SECURE_SSL_REDIRECT = env.bool("DJANGO_SECURE_SSL_REDIRECT", default=True)
SECURE_HSTS_SECONDS = env.int("DJANGO_SECURE_HSTS_SECONDS", default=2592000)
SECURE_HSTS_INCLUDE_SUBDOMAINS = env.bool(
    "DJANGO_SECURE_HSTS_INCLUDE_SUBDOMAINS", default=True)
SECURE_HSTS_PRELOAD = env.bool("DJANGO_SECURE_HSTS_PRELOAD", default=True)
SESSION_COOKIE_SECURE = env.bool("DJANGO_SESSION_COOKIE_SECURE", default=True)
CSRF_COOKIE_SECURE = env.bool("DJANGO_CSRF_COOKIE_SECURE", default=True)
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Admin Honeypot config
ADMIN_HONEYPOT_EMAIL_ADMINS = True
