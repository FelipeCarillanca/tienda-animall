from dataclasses import field
from pyexpat import model
from socket import fromshare
from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import User
from django.contrib.auth import login as auth_login
from django.contrib.auth import authenticate, login
from .models import accesorio,comidagato,comidaperro,usuario

class accesorioForm(forms.ModelForm):
    class Meta:
        model = accesorio
        fields = '__all__'

class agregarcomidaPerroForm(forms.ModelForm):
    class Meta:
        model = comidaperro
        fields = '__all__'

class agregarcomidaGatoForm(forms.ModelForm):
    class Meta:
        model = comidagato
        fields = '__all__'

class formregistrousuario(UserCreationForm):
    pass