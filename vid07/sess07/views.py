from django.http import HttpResponse
import datetime

#VISTA hola/
def saludo(request):
    documento = "Hola, alumnos Django."

    return HttpResponse(documento)

# VISTA chao/
def despedida(request):
    return HttpResponse("Hasta pronto, alumnos Django.")

# VISTA 
def fecha_hora(request):
    ahora = datetime.datetime.now()
