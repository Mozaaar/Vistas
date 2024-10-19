from django.db import models



# Clase libro
class libro(models.Model):
    titulo = models.CharField(max_length=100)
    precio = models.CharField(max_length=100)
    stock = models.CharField(max_length=100)
    autor = models.CharField(max_length=100)
    genero = models.CharField(max_length=100)
    año_publicacion = models.CharField(max_length=100)
    