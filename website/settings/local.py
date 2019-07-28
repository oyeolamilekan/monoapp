from .base import *

DEBUG = True

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
