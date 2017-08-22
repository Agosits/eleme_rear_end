import os

from django.http import HttpResponse
from django.views.generic import View



class IndexView(View):
    """Render main page."""

    def get(self, request):
        """Return html for main application page."""

        abspath = open(os.path.join(os.environ.get("STATIC_DIST"), 'index.html'), 'r')
        return HttpResponse(content=abspath.read())
