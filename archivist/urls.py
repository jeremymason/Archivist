from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # url(r'^myapp/', include('myapp.urls')),
    (r'^programs/$', 'web.views.programs'),
    (r'^genres/$', 'web.views.genres'),
    (r'^subjects/$', 'web.views.subjects'),
    (r'^program/(?P<program_id>\d+)/$', 'web.views.program'),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'web.views.index'),
)
