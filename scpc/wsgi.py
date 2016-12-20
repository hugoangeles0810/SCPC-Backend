"""
WSGI config for scpc project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

import config

os.environ.setdefault("DJANGO_SETTINGS_MODULE", config.settings_profile)

application = get_wsgi_application()
