import datetime
from coltrane.models import Resumen
from django.conf import settings
from django import template

register = template.Library()

@register.tag(name="get_archivos")
def do_archivos(parser, token):
    return ArchivosNode()

class ArchivosNode(template.Node):
    def render(self, context):
        #context['latest_entries']=Entry.objects.all()
        #noticias = Resumen.objects.filter(status=Resumen.LIVE_STATUS)
        noticias = Resumen.objects.all()
        #noticias = Entry.objects.filter(status=Entry.LIVE_STATUS)
        year_range = []
        for x in noticias.dates('fecha_publicacion', 'year'):
            if x not in year_range:
                year_range.append(x)

        year_range.sort(reverse=True)

        month_range = []
        for x in noticias.dates('fecha_publicacion', 'month'):
            if x not in month_range:
                month_range.append(x)

        month_range.sort(reverse=True)

        context['year_range'] = year_range
        context['month_range'] = month_range
        return ''   
