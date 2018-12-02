from __future__ import absolute_import, unicode_literals
from whitenoise.django import DjangoWhiteNoise
from django.core.wsgi import get_wsgi_application

import os


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "craigfyfe.settings.dev")

application = get_wsgi_application()
application = DjangoWhiteNoise(application)
