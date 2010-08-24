#===============================================================================
# from django import forms
# from registration.forms import RegistrationForm
# from django.utils.translation import ugettext_lazy as _
# from prensahoy.models import UsuarioPrensaHoyPerfil
# from registration.models import RegistrationProfile
# 
# class RegistrationFormPdH(RegistrationForm):
#    email_autorizado1 = forms.EmailField(label="Primer correo autorizado")
#    telefono_usuario = forms.CharField()
#    ciudad_usuario = forms.CharField()
#===============================================================================

#===============================================================================
#    def save(self, profile_callback=None):
#        new_user = RegistrationProfile.objects.create_inactive_user(username=self.cleaned_data['username'],
#        password=self.cleaned_data['password1'],
#        email=self.cleaned_data['email']
#        )
# 
#        new_profile = UsuarioPrensaHoyPerfil(user=new_user,
#                                             email_auth_1=self.cleaned_data['email_autorizado1'],
#                                             telefono= self.cleaned_data['telefono_usuario'],
#                                             ciudad= self.cleaned_data['ciudad_usuario']
#                                             )
#        new_profile.save()
# 
#        return new_user
#===============================================================================

#coding=UTF-8

from django import forms
from registration.backends.default import DefaultBackend
from registration.forms import RegistrationForm
import re

class RegistrationFormPdH(RegistrationForm):
    ciudad_usuario = forms.CharField(label="I'm a human")
    
class RegistrationFormPdHBackend(DefaultBackend):
    def get_form_class(self, request):
        return RegistrationFormPdH

class SearchFormKeyword(forms.Form):
    RADIO_PERIODO_CHOICES = (
        ('DI', 'Diario'),
        ('SE', 'Semanal'),
        ('ME', 'Mensual'),
        ('AN', 'Anual'),
    )
    keywords = forms.CharField(label='Palabras Clave', max_length=40, required=False, widget=forms.TextInput(attrs={'size':'30'}))
    fecha_periodo = forms.ChoiceField(label='Periodo de Busqueda', choices=RADIO_PERIODO_CHOICES)
    def clean_keywords(self):
        keywords = self.cleaned_data['keywords']
        if not re.search(r'^\w+$', keywords):
            raise forms.ValidationError(u'Las palabras solo pueden tener caracteres alfanumericos y guion bajo.')
