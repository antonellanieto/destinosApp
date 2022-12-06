from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import SignUpForm
from .models import User, Avatar
from django.contrib.auth.forms import AuthenticationForm
# Redireccion
from django.urls import reverse_lazy
# Auth
from django.contrib.auth.views import LoginView, LogoutView

#Los decoradores sirven para funciones > vistas basadas en funciones
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login

#ejemplo
# @decorador
# def funcion_a_proteger

#Los mixins sirven para clases > vistas basadas en clases
from django.contrib.auth.mixins import LoginRequiredMixin

#ejemplo
# class ClaseAProteger(MixinParaProteger)





# Create your views here.
def login_request(request):

    if request.method == "POST":

        loginform = AuthenticationForm(request, data=request.POST)

        if loginform.is_valid():
            data = loginform.cleaned_data

            nombre_usuario = data.get("username")
            contrasenia = data.get("password")

            usuario = authenticate(username=nombre_usuario, password=contrasenia)

            if usuario is not None:
                login(request, usuario)

                avatar = Avatar.objects.filter(user=request.user)
                if len(avatar) > 0:
                    img = avatar[0].imagen.url

                else:

                    img = None

                return render(request, 'AppDestinos/templates/index.html', {'user': usuario, 'img':img})

            else:
                return render(request, 'AppUsers/templates/login.html', {"errors": ['El usuario no existe.']})

        else:

            loginform= AuthenticationForm()
            return render(request, 'AppUsers/templates/login.html', {"loginform": loginform, "errors": ['Usuario o contraseña incorrectos']})

    else:
        
        loginform = AuthenticationForm()

        return render(request, 'AppUsers/templates/login.html', {"loginform": loginform})

def register_request(request):
    
    if request.method == "POST":

        registerform = SignUpForm(request.POST)

        if registerform.is_valid():

            registerform.save()
            user = registerform.cleaned_data.get("username")

            return redirect('Login')

        else:

            registerform= SignUpForm()
            return render(request, 'AppUsers/templates/registro.html', {"registerform": registerform, "errors": ['Datos de registro inválidos.']})

    else:

        registerform = SignUpForm()
        return render(request, 'AppUsers/templates/registro.html', {"registerform": registerform})





# class SignUpView(CreateView):

#     form_class = SignUpForm
#     success_url = reverse_lazy('Home')
#     template_name = 'registro.html'