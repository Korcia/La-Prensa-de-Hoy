from django.conf.urls.defaults import *

from coltrane.models import Article


article_info_dict = {
    'queryset': Article.live.all(),
    'date_field': 'pub_date',
}

urlpatterns = patterns('django.views.generic.date_based',
     (r'^$',
     'archive_index',
     article_info_dict,
     'coltrane_article_archive_index'),
    (r'^(?P<year>\d{4})/$',
     'archive_year',
     article_info_dict,
     'coltrane_article_archive_year'),
    (r'^(?P<year>\d{4})/(?P<month>\w{3})/$',
     'archive_month',
     article_info_dict,
     'coltrane_article_archive_month'),
    (r'^(?P<year>\d{4})/(?P<month>\w{3})/(?P<day>\d{2})/$',
     'archive_day',
     article_info_dict,
     'coltrane_article_archive_day'),
    (r'^(?P<year>\d{4})/(?P<month>\w{3})/(?P<day>\d{2})/(?P<slug>[-\w]+)/$',
     'object_detail',
     article_info_dict,
     'coltrane_article_detail'),
)
