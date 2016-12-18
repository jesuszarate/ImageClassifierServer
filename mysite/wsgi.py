"""
WSGI config for mysite project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/howto/deployment/wsgi/
"""

import os


#from django.core.wsgi import get_wsgi_application
#from whitenoise.django import DjangoWhiteNoise

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")

import django.core.handler.wsgi

from whitenoise.django import DjangoWhiteNoise

application = DjangoWhiteNoise(get_wsgi_application())

application = django.core.handlers.wsgi.WSGIHandler()

#application = get_wsgi_application()
from dj_static import Cling
application = Cling(get_wsgi_application())
application = DjangoWhiteNoise(application)
