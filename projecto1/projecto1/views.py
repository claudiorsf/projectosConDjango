from django.http import HttpResponse
import datetime
from django.template import Template, Context
from django.template import loader
from django.shortcuts import render 







class persona(object):
    def __init__(self, nombre,apellido):
        self.nombre=nombre
        self.apellido=apellido
""" luego voy a vista def (saludo) """



def saludo(request):
# para usar el metodo open acordarse de buscar la ruta en windows y de ahi dar vuelta las barras 
    p1=persona("Estudiante Claudio", "Sandoval")
    temas_varios=["plantillas","modelos", "formularios","listas", "despligue"]
    #nombre="Claudio"
   # apellido="Sandoval"

    ahora=datetime.datetime.now()
    #acordarse de dar vuelta las barras#

# cuando usamos pocas plantillas ponemos usar el metodo open, read, close.... pero cuando son vias plantillas(usadas en proyectos medianos en adelante
# conviene usar e importar plantillas y trabajar con ellas

   # doc_externo=open("C:/Users/jose/Documents/GitHub/DjangoProyectos/projectosConDjango/projecto1/projecto1/plantillas/plantilla1.html")
   # plt=Template(doc_externo.read())
    #doc_externo.close()
    #para comenzar a trabajar con las plantillas debemos especificar donde estas las plantillas....vamos a settings--->templates y de ahi en doc[ aca metemos al ruta de donde esta plantilla......"C:/Users/jose/Documents/GitHub/DjangoProyectos/projectosConDjango/projecto1/projecto1/plantillas"] #

   # doc_externo=loader.get_template ("plantilla1.html")


# para creas contexto se usan los diccionarios{}
   # ctx= Context({"nombre_persona":p1.nombre, "apellido": p1.apellido,"tiempo": ahora, "temas":["plantillas","modelos", "formularios","listas", "despligue"],"temario":temas_varios})

   # documento=doc_externo.render({"nombre_persona":p1.nombre, "apellido": p1.apellido,"tiempo": ahora, "temas":["plantillas","modelos", "formularios","listas", "despligue"],"temario":temas_varios})

   # return HttpResponse(documento)
    return render(request,"plantilla1.html",{"nombre_persona":p1.nombre, "apellido": p1.apellido,"tiempo": ahora, "temas":["plantillas","modelos", "formularios","listas", "despligue"],"temario":temas_varios})

def despedida(request):
    return HttpResponse("Nos vemos en la proxima ")

def dameFecha(request):
    fechaActual=datetime.datetime.now()

    documento="""
    <html>
    <body>
    <h1>
    Esta es la hora y fecha actual %s
    </h1>
    </body>
    </html>""" % fechaActual

    return HttpResponse(documento)

def edad(request,edad,agno):
   
    periodo=agno-2021
    edadResultado= edad+periodo
    documento="<html><body><h3>El año %s tendras %s años" %(agno, edadResultado)
    
    return HttpResponse(documento)

def padre(request):
    fechaActual=datetime.datetime.now()

    return render (request, "hija.html")