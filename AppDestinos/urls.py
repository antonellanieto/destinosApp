from django.urls import path
from AppDestinos import views

urlpatterns = [
   path('', views.mostrar_index, name='Home'),
   path('contacto', views.mostrar_contacto, name='Contacto'),
   path('CrearDestino', views.crear_destino, name='CrearDestino'),
   path('Buscar', views.buscar_destino, name='Buscar'),
   path('Destinos', views.mostrar_posteos, name='Publicaciones'),
]
