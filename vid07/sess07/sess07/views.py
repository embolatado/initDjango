from django.http import HttpResponse
from django.template import Template, Context
import datetime


# CONSTRUCTOR DE PERSONAS
class Persona(object):
    def __init__(self, nombre, apellido):
        self.name = nombre
        self.lname = apellido


#VISTA hola/
def saludo(request):
    

    # SE INDICA LA RUTA DE LA PLANTILLA
    var_a  = open('/Users/JulianLopera/Django/initDjango/vid07/sess07/templates/plantilla.html')

    # SE LEE EL TEMPLATE
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
    
    persona1 = Persona("Prof. Juan", "Díaz")
    persona2 = Persona("Dra. María", "Gómez")
    persona3 = Persona("Mlle. Emmanuelle", "Durant")

    ahora = datetime.datetime.now()

    temario = ["Plantillas", "Modelos", "Formularios",
               "Vistas", "Vistas Avanzadas", "Despliegue Aplicación"]

    # VISTA CON DICCIONARIO {} EN CONTEXTO
    # SE INICIA LA PLANTILLA

    var_uno = open('/Users/JulianLopera/Django/initDjango/vid07/sess07/templates/despedida.html')
    var_dos = Template(var_uno.read())
    var_uno.close()
    var_tri = Context({"nom_persona": persona1.name, "apell_persona": persona1.lname, "momento_actual": ahora, "temas": temario})
    var_qtr = var_dos.render(var_tri)
    
    return HttpResponse(var_qtr)

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

