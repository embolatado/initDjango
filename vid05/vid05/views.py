from django.http import HttpResponse
import datetime
from django.template import Template, Context

def saludo(request):

    doc_externo = open(
        '/Users/JulianLopera/Django/initDjango/vid05/vid05/plantillas/miplantilla.html')

    # 1. 
    plantilla = Template(doc_externo.read())
    doc_externo.close()

    contexto = Context()

    # RENDERIZAR 
    documento =  plantilla.render(contexto)

    return HttpResponse(documento)
