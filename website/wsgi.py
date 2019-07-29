"""
WSGI config for website project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/howto/deployment/wsgi/
"""

import os
import platform

from django.core.wsgi import get_wsgi_application

# Lazy to changing from dev to prod and verse so i added if statment
if platform.system() == 'Linux':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'website.settings.prod')
else:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'website.settings.local')

application = get_wsgi_application()

if os.getcwd() == '/app':
    from whitenoise.django import DjangoWhiteNoise
    application = DjangoWhiteNoise(application)
