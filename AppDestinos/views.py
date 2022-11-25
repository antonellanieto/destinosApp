from django.shortcuts import render
from django.http import HttpResponse
from .models import Paisajes, Paises
from .forms import CrearDestino
import email


# Create your views here.

def mostrar_index(request):

    return render(request, 'index.html')

def mostrar_contacto(request):

    return render(request, 'contact.html')


def crear_destino(request):
    

    if request.method == 'POST':

        formulario = CrearDestino(request.POST)

        if formulario.is_valid():

            formulario_limpio = formulario.cleaned_data

            destino = Paisajes(paisaje=formulario_limpio['paisaje'], lugar_historico=formulario_limpio['lugar_historico'])

            destino.save()

            return render(request, 'index.html')

    else:
        formulario = CrearDestino()

    context = {'formulario': formulario}

    return render(request, 'blog.html', context)


# def eliminar_destino(request, paisaje):

#     destino = Paisajes.objects.get(paisaje= paisaje)
#     destino.delete()