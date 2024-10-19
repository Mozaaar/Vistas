"""
URL configuration for vistas project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include


#Sirve para redirecionar despues de una acción revertiendo
# patrones de expresiones regulares
from django.urls import reverse

# Habilitamos el uso de mensajes en Django
from django.contrib import messages

# Habilitamos los mensajes para class-based views
from django.contrib.messages.views import SuccessMessageMixin

# Habilitamos los formularios en Django
from django import forms

from vistasweb.views import ListarLibros, DetalleLibro, ActualizarLibros, CrearLibro, EliminarLibro

urlpatterns = [
    path('admin/', admin.site.urls),
    path('listar/', ListarLibros.as_view(template_name = "index.html"), name='leer'),
    path('detalles/<int:pk>', DetalleLibro.as_view(template_name = "detalles.html"), name ='detalles'),
    path('actualizar/<int:pk>', ActualizarLibros.as_view(template_name = "actualizar.html"), name='actualizar'),
    path('eliminar/<int:pk>', EliminarLibro.as_view(template_name = "elimina.html"), name='elimina'),
    path('crear/', CrearLibro.as_view(template_name = "crear.html"), name='crea'),
]