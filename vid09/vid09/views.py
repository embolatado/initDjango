from django.http import HttpResponse
from django.template import Template, Context
from django.template.loader import get_template


class Persona(object):
    def __init__(self, prenom, nom):
        self.nombre = prenom
        self.apelli = nom


def saludo(request):
    persona1 = Persona("Juán", "Díaz")
    
    # CON loader
    var_a = get_template('plantilla1.html')
    var_b = var_a.render({"el_nombre": persona1.nombre, "el_apell": persona1.apelli.upper})

    return HttpResponse(var_b)

