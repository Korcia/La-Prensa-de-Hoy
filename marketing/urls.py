from django.conf.urls.defaults import *
from laprensadehoy.marketing.sitemaps import SITEMAPS


urlpatterns = patterns('laprensadehoy.marketing.views',
    (r'^robots\.txt$', 'robots'),
    #(r'^google_base\.xml$', 'google_base'),
)

urlpatterns += patterns('',
    (r'^sitemap\.xml$', 'django.contrib.sitemaps.views.sitemap', {'sitemaps': SITEMAPS }),
)
