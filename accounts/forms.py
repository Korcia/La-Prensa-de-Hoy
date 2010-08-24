#coding=UTF-8
from django import forms
from django.contrib.auth.forms import UserCreationForm
from accounts.models import UserProfile

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ('user',)
        
class RegistrationForm(UserCreationForm):
    """ subclass of Django's UserCreationForm, to handle customer registration with a required minimum length
    and password strength. Also contains an additional field for capturing the email on registration.
    
    """
    password1 = forms.RegexField(label="Clave", regex=r'^(?=.*\W+).*$', 
                                 help_text='La Clave debe tener un mínimo de 6 caracteres y contener al menos un caracter no alfanumérico(@.+-_).',
                                 widget=forms.PasswordInput, min_length=6)
    password2 = forms.RegexField(label="Confirme Clave", regex=r'^(?=.*\W+).*$',
                                 widget=forms.PasswordInput, min_length=6)
    email = forms.EmailField(max_length="50")