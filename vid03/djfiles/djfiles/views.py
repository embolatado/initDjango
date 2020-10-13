# IMPORTAR PARA QUE ESTE ARCHIVO SEA DE VISTAS
from django.http import HttpResponse

#VISTA 1
def saludo(request):
    return HttpResponse("Saludos otra vez, Django")

# VISTA 2
def despedida(request):
    return HttpResponse("¡Hasta mañana, Django!")