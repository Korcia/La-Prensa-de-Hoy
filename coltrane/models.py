#coding=UTF-8
import datetime
import locale
locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')

from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from django.db.models import permalink
from django.utils.translation import ugettext_lazy as _

from markdown import markdown

MARKUP_HTML = 'h'
MARKUP_MARKDOWN = 'm'
MARKUP_REST = 'r'
MARKUP_TEXTILE = 't'
MARKUP_OPTIONS = getattr(settings, 'ARTICLE_MARKUP_OPTIONS', (
        (MARKUP_HTML, _('HTML/Plain Text')),
        (MARKUP_MARKDOWN, _('Markdown')),
        (MARKUP_REST, _('ReStructured Text')),
        (MARKUP_TEXTILE, _('Textile'))
    ))
MARKUP_DEFAULT = getattr(settings, 'ARTICLE_MARKUP_DEFAULT', MARKUP_HTML)

class LiveResumenManager(models.Manager):
    def get_query_set(self):
        return super(LiveResumenManager, self).get_query_set().filter(status=self.model.LIVE_STATUS)

class PrivadoResumenManager(models.Manager):
    def get_query_set(self):
        return super(PrivadoResumenManager, self).get_query_set().filter(status=self.model.HIDDEN_STATUS)

class Resumen(models.Model):
    LIVE_STATUS = 1
    DRAFT_STATUS = 2
    HIDDEN_STATUS = 3
    STATUS_CHOICES = (
        (LIVE_STATUS, 'Publico'),
        (DRAFT_STATUS, 'Draft'),
        (HIDDEN_STATUS, 'Privado'),
    )

    # Core fields.
    titulo = models.CharField(max_length=250,
                             help_text="Máximo 250 caracteres.")
    extracto = models.TextField(blank=True,
                               help_text="Un resumen corto de la noticia. Opcional.")
    cuerpo = models.TextField()
    fecha_publicacion = models.DateTimeField(default=datetime.datetime.now)

    # Fields to store generated HTML.
    extracto_html = models.TextField(editable=False, blank=True)
    cuerpo_html = models.TextField(editable=False, blank=True)

    # Metadata.
    autor = models.ForeignKey(User)
    slug = models.SlugField(unique_for_date='fecha_publicacion',
                            help_text="Valor sugerido generado automaticamente por el título. Debe ser único para la fecha de publicación.")
    status = models.IntegerField(choices=STATUS_CHOICES, default=LIVE_STATUS,
                                 help_text="Sólo noticias con estado Publica serán mostradas.")


    objects = models.Manager()
    live = LiveResumenManager()
    privado = PrivadoResumenManager()

    class Meta:
        ordering = ['-fecha_publicacion']
        verbose_name_plural = "Resúmenes"

    def __unicode__(self):
        return self.titulo

    def save(self, force_insert=False, force_update=False):
        self.cuerpo_html = markdown(self.cuerpo, ['tables'])
        if self.extracto:
            self.extracto_html = markdown(self.extracto)
        super(Resumen, self).save(force_insert, force_update)

    @permalink
    def get_absolute_url(self):
        return ('coltrane_resumen_detail', (), { 'year': self.fecha_publicacion.strftime("%Y"),
                                               'month': self.fecha_publicacion.strftime("%b").lower(),
                                               'day': self.fecha_publicacion.strftime("%d"),
                                               'slug': self.slug })
