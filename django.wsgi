import os
import sys
import site

basepath = "/".join(os.path.abspath(__file__).split("/")[0:-1])

sys.path.append(basepath)

for path in ['bin', 'archivist', 'lib/python2.7', 'lib/python2.7/site-packages']:
	sys.path.append(basepath + '/' + path)
	site.addsitedir(basepath + '/' + path)

os.environ['PYTHONPATH'] = basepath + '/lib/python2.7'
os.environ['DJANGO_SETTINGS_MODULE'] = 'archivist.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()

