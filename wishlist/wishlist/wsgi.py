"""
WSGI config for wishlist project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""

# WSGI config: entry point for traditional web servers (Gunicorn, uWSGI)
# You usually don't need to change this file for development.
import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'wishlist.settings')

application = get_wsgi_application()
