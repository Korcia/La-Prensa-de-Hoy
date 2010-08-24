#coding=UTF-8
import os.path

from django.conf.urls.defaults import *
from prensahoy.views import main_page, search_page
from contacto.views import contact
from servicios.views import entrada_servicio, servicio

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

static = os.path.join(os.path.dirname(__file__), 'static')



urlpatterns = patterns('',
    (r'^$', main_page),
    (r'^resumenes/', include('coltranefree.urls.resumenes')),
    (r'^usuarios/', include('coltrane.urls.resumenes')),
    (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': static}),
    #(r'^usuarios/', include('prensahoy.urls')),
    (r'^contacto/$', contact),
    (r'^entrada_servicios/$', entrada_servicio),
    (r'^servicios/$', servicio),
    (r'^buscar/$', search_page),
    #(r'^usuarios/', include('registration.backends.default.urls')),
    (r'^usuarios/', include('accounts.urls')),
    (r'^usuarios/', include('django.contrib.auth.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
)
