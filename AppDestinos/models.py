from django.db import models

# Create your models here.


class Destinos(models.Model):
    nombre_pais = models.CharField(max_length=150)
    continente = models.CharField(max_length=40)
    descripcion = models.CharField(max_length=900)
    paisaje = models.CharField(max_length=150)
    cantidad_poblacion = models.IntegerField()




    
    