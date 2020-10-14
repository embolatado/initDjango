from django.http import HttpResponse
import datetime


def saludo(request):
    documento = """<html>
    <body>
        <h3>Con <code>html</code> dentro de la vista - <i>¡horrible!</i></h3>
    </body>
    </html>"""

    return HttpResponse(documento)


def adios(request):
    return HttpResponse("¡Hasta pronto, alumnos Django!")


# CONTENIDO DINÁMICO CON MARCADORES DE POSICIÓN %s
def dameFecha(request):
    fecha_actual = datetime.datetime.now()

    documento = """<html>
    <body>
        <h3>Fecha y hora GMT actual: %s</h3>
    </body>
    </html>""" %fecha_actual

    return HttpResponse(documento)


# PASAR PARÁMETROS EN URL - Django es URL friendly para SEO
def calculaEdad(request, jahre):

    edad_actual = 20
    periodo = jahre-2020
    edadFutura = edad_actual + periodo
    
    documento = """<html><body><h3>En el año %s tendrás %s años.</h3></body></html>""" %(jahre, edadFutura)

    return HttpResponse(documento)