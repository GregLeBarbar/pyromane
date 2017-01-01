import os
import sys
from django.core.wsgi import get_wsgi_application

path = '/home/GregLeBarbar/pyromane/src'
if path not in sys.path:
    sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'config.settings.prod'

application = get_wsgi_application()
