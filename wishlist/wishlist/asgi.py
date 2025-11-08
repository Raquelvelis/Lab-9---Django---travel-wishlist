# ASGI config: lets Django talk to asynchronous servers (e.g., Daphne/Uvicorn)
# You usually don't need to change this file.
import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'wishlist.settings')

application = get_asgi_application()
