#coding=UTF-8
from django.shortcuts import render_to_response


def entrada_servicio(request):
    return render_to_response('iphone.html')

def servicio(request):
    return render_to_response('iphone2.html')
