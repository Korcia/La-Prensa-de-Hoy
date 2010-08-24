#coding=UTF-8
from django.core.mail import send_mail
#from django.core.context_processors import csrf
from django.shortcuts import render_to_response
from django.template import RequestContext
from contacto.forms import ContactForm
from django.views.decorators.csrf import csrf_exempt 
#from django.template import RequestContext

@csrf_exempt
def contact(request):
    #c = {}
    #c.update(csrf(request))
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            send_mail(
                cd['asunto'],
                cd['mensaje'],
                cd.get('email', 'noreply@example.com'),
                ['jmgmontes@gmail.com'],
            )
            return render_to_response('gracias.html')
    else:
        form = ContactForm()
    return render_to_response('contacto.html', {'form': form}, context_instance=RequestContext(request))

