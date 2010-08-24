#coding=UTF-8

from django.shortcuts import render_to_response
from django.template import RequestContext
from django.db.models import Q
from coltrane.models import Resumen
import re
#from django.http import HttpResponse
from prensahoy.forms import SearchFormKeyword

def main_page(request):
    return render_to_response('main_page2.html', locals(), context_instance=RequestContext(request))

def search_page(request):
    
    if (request.method == 'GET') and 'tipobusqueda' in request.GET:
        id_keywords = request.GET['keywords'].strip()
        keywords = id_keywords.split()
        q1 = Q()
        for keyword in keywords:
            q1 = q1 | Q(cuerpo_html__icontains=keyword)
        resumenes = Resumen.objects.filter(q1)
        
        ## busqueda de parrafo add to check git
        resumenPattern = re.compile(r'<p>(.*?)</p>', re.U)
        substring_list=["CECA"]
        lista_resumenes = []
        if resumenes:
            for p in resumenes:
                resultados = resumenPattern.findall(p.cuerpo_html)
                for keyword in keywords:
                    fecha_parrafo = p.fecha_publicacion
                    enlace = p.get_absolute_url()
                    patt = r'%s' % '|'.join(substring_list)
                    for i in resultados:
                        if re.search(keyword, i):
                            parrafo = i
                            lista_resumenes.append([fecha_parrafo,parrafo,enlace])
        else:
            resumenes = None
            parrafo = None
        ## fin busqueda de parrafo
        #variables = {'rowcolor1': 'impar', 'rowcolor2': 'par', 'resumenes': resumenes, 'parrafos': parrafo}
        variables = {'lista_resumenes': lista_resumenes,}
        return render_to_response('resultados.html', variables, context_instance=RequestContext(request))
    
    form1 = SearchFormKeyword()
    variables = RequestContext(request, {
                'page_body': 'Filtre su búsqueda mediante palabras clave y período de búsqueda.',
                'form_key': form1
                })                
    return render_to_response('search_page.html', variables, context_instance=RequestContext(request))
        