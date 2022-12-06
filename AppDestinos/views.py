from django.shortcuts import render
from django.http import HttpResponse
from .models import Destinos
from .forms import CrearDestino
import email


# Create your views here.

def mostrar_index(request):

    return render(request, 'index.html')

def mostrar_contacto(request):

    return render(request, 'contact.html')


# def crear_destino(request):
    

#     if request.method == 'POST':

#         formulario = CrearDestino(request.POST)

#         if formulario.is_valid():

#             formulario_limpio = formulario.cleaned_data
#             destino = Destinos(paisaje=formulario_limpio['paisaje'], nombre_pais=formulario_limpio['nombre_pais'],cantidad_poblacion=formulario_limpio['cantidad_poblacion'], descripcion=formulario_limpio['descripcion'],  continente=formulario_limpio['continente'])

#             destino.save()

#             return render(request, 'index.html')

#     else:
#         formulario = CrearDestino()

#     context = {'formulario': formulario}

#     return render(request, 'blog.html', context)


# def eliminar_destino(request, paisaje):

#     destino = Paisajes.objects.get(paisaje= paisaje)
#     destino.delete()


