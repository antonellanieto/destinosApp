from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class SignUpForm(UserCreationForm):

    email = forms.EmailField()
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirme su contraseña", widget=forms.PasswordInput)

    first_name = forms.CharField(label="Nombre")
    last_name = forms.CharField(label="Apellido")

    class Meta:
        
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'first_name', 'last_name']
        help_text = {k: "" for k in fields}

class EditForm(UserCreationForm):

    email = forms.EmailField(label="Modificar E-mail")
    first_name = forms.CharField(label="Nombre", required=False)
    last_name = forms.CharField(label="Apellido", required=False)
    password1 = forms.CharField(label='Nueva contraseña', widget=forms.PasswordInput, required=False)
    password2 = forms.CharField(label='Confirme su contraseña', widget=forms.PasswordInput, required=False)

    class Meta:
        
        model = User
        fields = ['email', 'password1', 'password2', 'first_name', 'last_name']
        help_text = {k: "" for k in fields}

class AvatarForm(forms.Form):

    img = forms.ImageField()
        