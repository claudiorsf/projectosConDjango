"""projecto1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# agregas el nombre de def..... la , del path debe coincidir con , como del views ...edad, edad, saludos, saludo, padre, padre
from django.contrib import admin
from django.urls import path
from projecto1.views import saludo,despedida,dameFecha,edad,padre

# nota: path("nombre q se te ocurra"/,nombre def)
urlpatterns = [
    path('admin/', admin.site.urls),
    path("saludo/", saludo),
    path("cierre/", despedida),
    path("fecha/", dameFecha),
    path("edad/<int:edad>/<int:agno>", edad),
    path("hija/",padre),
]
