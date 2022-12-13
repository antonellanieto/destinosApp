from django.shortcuts import render
from django.http import HttpResponse
from .models import Destinos
from .forms import CrearDestino
import email

from django.views.generic.edit import CreateView, UpdateView, DeleteView



# Create your views here.

def mostrar_index(request):

    return render(request, 'index.html')

def mostrar_contacto(request):

    return render(request, 'contact.html')

def buscar_destino(request):

    if request.GET.get('nombre', False): 
        nombre_pais = request.GET['nombre']
        destinos = Destinos.objects.filter(nombre__icontains=nombre_pais)

        return render(request, 'buscar_destino.html', {'destinos': destinos})
    else:
        respuesta = 'No hay datos'
    return render(request, 'buscar_destino.html', {'respuesta': respuesta})


def crear_destino(request):

    if request.method == 'POST':

        formulario = CrearDestino(request.POST)

        if formulario.is_valid():

            formulario_limpio = formulario.cleaned_data

            destino = Destinos(nombre=formulario_limpio['nombre'], paisaje=formulario_limpio['paisaje'], continente=formulario_limpio['continente'], descripcion=formulario_limpio['descripcion'], poblacion = formulario_limpio['poblacion'], imagenes= formulario_limpio['imagenes'])

            destino.save()

            return render(request, 'index.html')

    else:
        formulario = CrearDestino()
    return render(request, 'crear_destino.html', {'formulario': CrearDestino})


def mostrar_posteos(request):

    destinos = Destinos.objects.all()

    context = {'destinos': destinos}

    return render(request, 'mostrar_posteos.html', context=context)


def eliminar(request, destino_nombre):

    destino = Destinos.objects.get(nombre=destino_nombre)

    destino.delete()

    destino = Destinos.objects.all()

    context = {'destino': destino}

    return render(request, 'mostrar_posteos.html', context=context)