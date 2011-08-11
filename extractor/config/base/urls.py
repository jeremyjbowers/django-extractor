from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
admin.autodiscover()
from feed.api import v1

urlpatterns = patterns('',
    url(r'^api/', include(v1.urls)),    
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/', include(admin.site.urls)),
)