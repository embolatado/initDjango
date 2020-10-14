from django.http import HttpResponse

def saludo(request):
    return HttpResponse("Hola, alumnos Django")

def adios(request):
    return HttpResponse("Hasta pronto, alumnos Django")


