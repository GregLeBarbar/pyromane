import os
import sys

path = '/home/GregLeBarbar/pyromane/src'
if path not in sys.path:
    sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'config.settings.prod'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
