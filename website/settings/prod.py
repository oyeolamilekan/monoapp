"""
    This is production environment setting for the backend
"""
from .base import *

DEBUG = False

ALLOWED_HOSTS = ["https://kirr.xyz"]

SECURE_SSL_REDIRECT = True

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "siten",
        "USER": "oyeolalekan",
        "PASSWORD": "oyeolamilekan",
        "HOST": "127.0.0.1",
        "PORT": "5432",
    }
}
FRONTEND_URL = "https://shopstack.co"