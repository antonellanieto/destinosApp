from django.db import models

# Create your models here.


class Paises(models.Model):
    nombre_pais = models.CharField(max_length=150)
    continente = models.CharField(max_length=40)
    descripcion = models.CharField(max_length=900)

class Paisajes(models.Model):
    paisaje = models.CharField(max_length=150)
    lugar_historico = models.CharField(max_length=150)


    
    