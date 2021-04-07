from django.http import HttpResponse
import datetime
from django.template import Template, Context

def saludo(request):

    # CON VARIABLES
    nombre = "Juan"


    # IMPORTA LA RUTA DE LA PLANTILLA
    doc_externo = open('/Users/JulianLopera/Django/initDjango/vid06/vid06/plantilla/miplantilla.html')

    # SE CREA LA PLANTILLA Y SE CIERRA
    plantilla = Template(doc_externo)
    doc_externo.close()

    # SE CREA EL CONTEXTO QUE INCLUYE LAS VARIABLES COMO DICCIONARIO
    contexto = Context()

    # SE RENDERIZAN LA PLANTILLA Y EL CONTEXTO
    documento = plantilla.render(contexto)

    # SE CREA EL RETURN DE LA VISTA
    return HttpResponse(documento)

"""
def despedida(request):
    return HttpResponse("¡Hasta luego, alumnos de Django!")

def dame_fecha(request):
    fecha_actual = datetime.datetime.now()

"""