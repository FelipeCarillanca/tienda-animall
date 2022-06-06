from django.shortcuts import render
from .models import comidagatos

# Create your views here.

def index(request):
    return render(request, 'core/index.html')

def gatos(request):
    return render(request, 'core/gatos.html')

def accesorios(request):
    return render(request, 'core/accesorios.html')

def formulariocontacto(request):
    return render(request, 'core/formulariocontacto.html')

def login(request):
    return render(request, 'core/login.html')

def mostrarperros(request):
    return render(request, 'core/mostrarperros.html')

def perros(request):
    return render(request, 'core/perros.html')

def listarproductos(request):
    comidaGA = comidagatos.objects.all()
    datos ={
        'comida': comidaGA
    }
    return render(request, 'core/listarproductos.html',datos)