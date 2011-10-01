import sys
import site
import os

vepath = '/usr/share/kinkajou/livescoop/website/livescoopwsenv/lib/python2.6/site-packages'

prev_sys_path = list(sys.path)
site.addsitedir(vepath)
sys.path.append('/usr/share/kinkajou/livescoop/website/livescoopws')
sys.path.append('/usr/share/kinkajou/livescoop/website/')

new_sys_path = [p for p in sys.path if p not in prev_sys_path]
for item in new_sys_path:
    sys.path.remove(item)
sys.path[:0] = new_sys_path

from django.core.handlers.wsgi import WSGIHandler
os.environ['DJANGO_SETTINGS_MODULE'] = 'livescoopws.settings'
application = WSGIHandler()
