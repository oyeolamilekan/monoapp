"""
    This is local dev setting for the backend
"""

from .base import *

DEBUG = False

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "siten",
        "USER": "oyeolalekan",
        "PASSWORD": "oyeolamilekan",
        "HOST": "127.0.0.1",
        "PORT": "",
    }
}
FRONTEND_URL = "http://myapp.local:3000"
