from django.db import models
from django import forms
from django.contrib.auth.models import User

class BaseProfileInfo(models.Model):
    class Meta:
        abstract = True        
    #informacion de contacto
    email = models.EmailField(max_length=50)
    telefono = models.CharField(max_length=20)
    usuario_nombre = models.CharField(max_length=50)
    usuario_direccion = models.CharField(max_length=50)
    usuario_ciudad = models.CharField(max_length=50)
    usuario_pais = models.CharField(max_length=50)
    usuario_cpostal = models.CharField(max_length=10)
   
class UserProfile(BaseProfileInfo):
    """ stores customer order information used with the last order placed; can be attached to the checkout order form
    as a convenience to registered customers who have placed an order in the past.
    
    """
    user = models.ForeignKey(User, unique=True)

    class Meta:
        ordering = ['usuario_ciudad']
        verbose_name_plural = "CuentasUsuarios"    
    def __unicode__(self):
        return 'User Profile for: ' + self.user.username