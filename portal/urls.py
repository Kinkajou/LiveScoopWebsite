from django.conf.urls.defaults import patterns, url, include
from django.views.generic.simple import direct_to_template

urlpatterns = patterns(
    'portal.urls',
    url(r'^downloads$', direct_to_template, {'template': 'portal/downloads.html'}),
    url(r'^about$', direct_to_template, {'template': 'portal/about.html'}),
    url(r'^$', direct_to_template, {'template': 'portal/home.html'}),
    )
