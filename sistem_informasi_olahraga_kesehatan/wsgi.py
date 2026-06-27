"""
WSGI config for sistem_informasi_olahraga_kesehatan project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/6.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sistem_informasi_olahraga_kesehatan.settings')

application = get_wsgi_application()
