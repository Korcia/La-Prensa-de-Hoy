from django.contrib.sitemaps import Sitemap

class EstaticasSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.5
    
    def items(self):
        return ['/buscar/', '/resumenes/', '/contacto/']
    def location(self, obj):
        return obj
    
SITEMAPS = {'estaticas': EstaticasSitemap }
