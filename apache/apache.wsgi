import os
import sys

path = '/srv/www'
if path not in sys.path:
    sys.path.insert(0, '/srv/www/carmaniadealer.com/car_mania')
    sys.path.append('/srv/www/carmaniadealer.com/car_mania/car_mania')

from django.core.wsgi import get_wsgi_application
from mezzanine.utils.conf import real_project_name

os.environ.setdefault("DJANGO_SETTINGS_MODULE",
                      "%s.settings" % real_project_name("car_mania"))

application = get_wsgi_application()
