from django.conf.urls import patterns, include, url
from views import *
import os
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', home),
    url(r'^phase$', phase),
    url(r'^upload$', upload),
    
    url(r'^images/(?P<path>.*)$', 'django.views.static.serve', {'document_root': os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates/images/')}),
    url(r'^css/(?P<path>.*)$', 'django.views.static.serve', {'document_root': os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates/css/')}),
    url(r'^js/(?P<path>.*)$', 'django.views.static.serve', {'document_root': os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates/js/')}),
    url(r'^fonts/(?P<path>.*)$', 'django.views.static.serve', {'document_root': os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates/fonts/')}),
    url(r'^bootstrap/(?P<path>.*)$', 'django.views.static.serve', {'document_root': os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates/bootstrap/')}),

    # Examples:
    # url(r'^$', 'y86.views.home', name='home'),
    # url(r'^y86/', include('y86.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
