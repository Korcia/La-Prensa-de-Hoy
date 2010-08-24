from django.conf.urls.defaults import *
#from coltrane.views import limited_archive_index
from coltrane.models import Resumen
#from django.views.generic.simple import direct_to_template
from django.contrib.auth.decorators import login_required
#from django.contrib.auth import authenticate, login

from django.views.generic.date_based import object_detail

entry_info_dict = {
    'queryset': Resumen.live.all(),
    'date_field': 'fecha_publicacion',
}
privado_info_dict = {
    'queryset': Resumen.objects.all(),
    'date_field': 'fecha_publicacion',
}

urlpatterns = patterns('',
     (r'^$',
     #'coltrane.views.limited_archive_index',
     'django.views.generic.date_based.archive_index',
     privado_info_dict,
     'coltrane_resumen_archive_index'),
     (r'^mi_cuenta/$',
     #'coltrane.views.limited_archive_index',
     'coltrane.views.limited_archive_index',
     privado_info_dict,
     'archive_index'),
    (r'^(?P<year>\d{4})/$',
     'coltrane.views.limited_archive_year',
     privado_info_dict,
     'coltrane_resumen_archive_year'),
    (r'^(?P<year>\d{4})/(?P<month>\w{3})/$',
     'coltrane.views.limited_archive_month',
     privado_info_dict,
     'coltrane_resumen_archive_month'),
    (r'^(?P<year>\d{4})/(?P<month>\w{3})/(?P<day>\d{2})/$',
     'coltrane.views.limited_archive_day',
     privado_info_dict,
     'coltrane_resumen_archive_day'),
    (r'^(?P<year>\d{4})/(?P<month>\w{3})/(?P<day>\d{2})/(?P<slug>[-\w]+)/$',
     'django.views.generic.date_based.object_detail',
     privado_info_dict,
     'coltrane_resumen_detail'),
)
