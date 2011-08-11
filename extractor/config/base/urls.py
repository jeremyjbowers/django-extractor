from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
admin.autodiscover()
from feed.api import v1

urlpatterns = patterns('',
    url(r'^extractor/api/', include(v1.urls)),    
    url(r'^extractor/grappelli/', include('grappelli.urls')),
    url(r'^extractor/admin/chronograph/job/(?P<pk>\d+)/run/$',
        'chronograph.views.job_run', name="chronograph_job_run"),
    url(r'^extractor/admin/', include(admin.site.urls)),
)