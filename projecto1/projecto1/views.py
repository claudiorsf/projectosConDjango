from django.http import HttpResponse

def saludo(request):
    return HttpResponse("Hola Jose estoy de un host local saludando gracias a Django")


