from django.conf.urls import patterns, include, url
from tweet_engine.views import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'campus.views.home', name='home'),
    # url(r'^campus/', include('campus.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^listener/', listener, name='listener'),
    url(r'^monitor/', monitor, name='monitor'),
)
