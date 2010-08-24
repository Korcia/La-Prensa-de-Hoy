# coding=UTF-8
from django import forms

class ContactForm(forms.Form):
    TIPO_CHOICES = (
        ('', '--- Elija tipo de asunto ---'),
        ('SUGERENCIA', 'Sugerencias'),
        ('INFORMACIÓN', 'Información'),
        ('PROBLEMAS', 'Problemas'),
        ('OTROS', 'Otros'),
    )
    tipo = forms.ChoiceField(label='', choices=TIPO_CHOICES)    
    asunto = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'size':'30'}))
    email = forms.EmailField(required=False, max_length=30, widget=forms.TextInput(attrs={'size':'25'}))
    mensaje = forms.CharField(widget=forms.Textarea(attrs={'cols':'35','rows':'10' }), max_length=200)

