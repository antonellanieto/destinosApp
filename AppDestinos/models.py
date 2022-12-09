from django.db import models

# Create your models here.


class Destinos(models.Model):
    nombre = models.CharField(max_length=150)
    continente = models.CharField(max_length=40)
    descripcion = models.CharField(max_length=900)
    paisaje = models.CharField(max_length=150)
    poblacion = models.IntegerField()
    imagenes = models.ImageField(upload_to='subidas', null=True, blank=True)

    def __str__(self):
        return f'Nombre: {self.nombre}, Continente: {self.continente}, Descripción: {self.descripcion}, Paisaje: {self.paisaje}, poblacion: {self.poblacion}, Imagenes: {self.imagenes}'




    
    