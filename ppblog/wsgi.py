"""
WSGI config for ppblog project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/howto/deployment/wsgi/
"""

import os, sys

from django.core.wsgi import get_wsgi_application

path = '/home/ec2-user/webroot/blog'

if path not in sys.path:
   sys.path.append(path)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ppblog.settings")

application = get_wsgi_application()

from django.core.wsgi import get_wsgi_application
from django.contrib.staticfiles.handlers import StaticFilesHandler
application = StaticFilesHandler(get_wsgi_application())
