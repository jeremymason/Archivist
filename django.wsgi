import os
import sys
import site

sys.path.append('/home/ubuntu/serve/weru/bin')
sys.path.append('/home/ubuntu/serve/weru')
sys.path.append('/home/ubuntu/serve/weru/archivist')
sys.path.append('/home/ubuntu/serve/weru/lib/python2.7')
sys.path.append('/home/ubuntu/serve/weru/lib/python2.7/site-packages')

site.addsitedir('/home/ubuntu/serve/weru/lib/python2.7')
site.addsitedir('/home/ubuntu/serve/weru/lib/python2.7/site-packages')

os.environ['PYTHONPATH'] = '/home/ubuntu/serve/weru/lib/python2.7'
os.environ['DJANGO_SETTINGS_MODULE'] = 'archivist.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()

