from django.urls import path
from AppUsers.views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    
    path('login/', login_request, name='Login'),
    path('registro/', register_request, name='CrearUsuario'),
    path('logout/', LogoutView.as_view(template_name='AppUsers/templates/logout.html'), name='Logout'),

]