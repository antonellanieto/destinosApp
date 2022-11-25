from django.urls import path
from AppUsers.views import *


urlpatterns = [
    
    path('accounts/login/', login_request, name='CrearUser'),

]