"""
WSGI config for cloudtesting project.

"""
import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "elemeproject.settings.dev")

application = get_wsgi_application()
