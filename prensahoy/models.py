#coding=UTF-8
from django.db import models
from django.contrib.auth.models import User

class UsuarioPrensaHoyPerfil(models.Model):
    user = models.ForeignKey(User, unique=True)
    email_auth_1= models.EmailField(blank=True)
    email_auth_2= models.EmailField(blank=True)
    email_auth_3= models.EmailField(blank=True)
    email_auth_4= models.EmailField(blank=True)
    email_auth_5= models.EmailField(blank=True)
    telefono = models.CharField(max_length=20, blank=True)
    ciudad = models.CharField(max_length=40, blank=True)
    class Meta:
        ordering = ['ciudad']
        verbose_name_plural = "PerfilesUsuarios"
    def __unicode__(self):
        return u'%s' % str(self.user__username) + '-' + str(self.ciudad)
        #return u'%s' % self.get_nombre_display()
    
