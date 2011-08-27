import os
import sys
import site

basepath = "/".join(os.path.abspath(__file__).split("/")[0:-1])

sys.path.append(basepath)
sys.path.append(basepath + '/bin')
sys.path.append(basepath + '/archivist')
sys.path.append(basepath + '/lib/python2.7')
sys.path.append(basepath + '/lib/python2.7/site-packages')
                 
site.addsitedir(basepath + '/lib/python2.7')
site.addsitedir(basepath + '/lib/python2.7/site-packages')

os.environ['PYTHONPATH'] = basepath + '/lib/python2.7'
os.environ['DJANGO_SETTINGS_MODULE'] = 'archivist.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()

