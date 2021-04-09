from django.http import HttpResponse
from django.template import Template, Context
import datetime

#VISTA hola/
def saludo(request):
    
    # SE INDICA LA RUTA DE LA PLANTILLA
    var_a  = open('/Users/JulianLopera/Django/initDjango/vid07/sess07/templates/plantilla.html')

    # SE CREA EL TEMPLATE
    var_b = Template(var_a.read())

    # SE CIERRA LA CONEXIÓN A LA PLANTILLA PARA NO GASTAR RECURSOS EXTRA
    var_a.close()

    # SE CREA EL CONTEXTO – AUNQUE VACÍO
    var_c = Context()

    # SE RENDERIZA EL DOCUMENTO
    var_d = var_b.render(var_c)

    # SE LLAMA AL RENDERIZADO return
    return HttpResponse(var_d)


# VISTA chao/
def despedida(request):
    return HttpResponse("Hasta pronto, alumnos Django.")

# VISTA ahora/
def fecha_hora(request):
    ahora = datetime.datetime.now()

    return HttpResponse("Ahora es %s" % ahora)

# VISTA edades/
def calcula_edad(request, edad, annee):
    este = datetime.date.today().year
    dife = annee - este
    calc = edad + dife
    mensaje = "En el año %s tendrás %s años." % (annee, calc)

    return HttpResponse(mensaje)

