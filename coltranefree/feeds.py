#coding=UTF-8
from django.contrib.syndication.feeds import Feed
from django.contrib.sites.models import Site
from coltrane.models import Entry, Article

current_site = Site.objects.get_current()

class NoticiasConcerts(Feed):
    title = u'ClasiAgenda: Últimas Noticias'
    link = '/rss/noticias/'
    description = u'Últimas noticias enviadas a ClasiAgenda'
    def items(self):
        return Entry.objects.filter(status=Entry.LIVE_STATUS)[:10]

class ArticulosConcerts(Feed):
    title = u'ClasiAgenda: Artículos'
    link = '/rss/articulos/'
    description = u'Últimas artículos publicados en ClasiAgenda'
    def items(self):
        return Article.objects.filter(status=Article.LIVE_STATUS)[:10]
