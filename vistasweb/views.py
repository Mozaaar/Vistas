from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from .models import libro


# Definimos las vistas que invoquen las librerias que permitan
# Listar, Detallar, Modiicar, Crear y Borrar libros
class CrearLibro(SuccessMessageMixin, CreateView):
    model = libro 
    form = libro
    fields = "__all__"
    success_message = 'Libro Creado Correctamente!'

class ListarLibros(ListView):
    model = libro 

class DetalleLibro(DetailView):
    model = libro 

class ActualizarLibros(SuccessMessageMixin, UpdateView):
    model = libro 
    form = libro 
    fields = '__all__'
    success_message = 'Libro Actualizado Correctamente!'

    def get_success_url(self):
        return reverse('leer')
    
class EliminarLibro(SuccessMessageMixin, DeleteView):
    model = libro 
    form = libro 
    fields = '__all__'

    def get_success_url(self):
        success_message = 'Libro Eliminado Correctamente!'
        messages.success (self.request, (success_message))
        return reverse('leer')