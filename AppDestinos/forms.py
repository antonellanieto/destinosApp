from django import forms

class CrearDestino(forms.Form):
    paisaje = forms.CharField(max_length=150)
    nombre_pais = forms.CharField(max_length=150)
    continente = forms.CharField(max_length=40)
    descripcion = forms.CharField(max_length=900)
    cantidad_poblacion = forms.IntegerField()
