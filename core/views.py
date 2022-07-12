from ast import parse
from email import message
from gc import get_objects
from pyexpat.errors import messages
from venv import create
from django.shortcuts import render, redirect, get_object_or_404
from .models import comidagato, comidaperro, accesorio
from rest_framework import viewsets
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required, permission_required
from django.http import HttpResponse 
from .serializers import comidagatoSerializer, comidaperroSerializer, accesorioSerializer
from .forms import accesorioForm, agregarcomidaPerroForm,agregarcomidaGatoForm,formregistrousuario
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password
from rest_framework.authtoken.models import Token


class comidagatoViewset(viewsets.ModelViewSet):
    queryset = comidagato.objects.all()
    serializer_class = comidagatoSerializer

class comidaperroViewset(viewsets.ModelViewSet):
    queryset = comidaperro.objects.all()
    serializer_class = comidaperroSerializer

class accesorioViewset(viewsets.ModelViewSet):
    queryset = accesorio.objects.all()
    serializer_class = accesorioSerializer




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

def carro(request):
    return render(request, 'core/carro.html')

@permission_required('core.view_comidagato')
def listarproductos(request):
    comidaGA = comidagato.objects.all()
    datos ={
        'comidaGa': comidaGA
    }
    return render(request, 'core/listarproductos.html',datos)

@permission_required('core.view_comidaperro')
def listarperro(request):
    comidaPERRO = comidaperro.objects.all()
    datos ={
        'comidaPERRO': comidaPERRO
    }
    return render(request, 'core/listarperro.html',datos)

@permission_required('core.view_accesorio')
def listaraccesorios(request):
    accesorios = accesorio.objects.all()
    datos ={
        'accesorio': accesorios
    }
    return render(request, 'core/listaraccesorios.html',datos)

"""AGREGAR ACCESORIOS"""
@permission_required('core.add_accesorio')
@permission_required('core.change_accesorio')
@permission_required('core.delete_accesorio')
def form_accesorio(request):
    data = {
        'form': accesorioForm()
    }

    if request.method == 'POST':
        formulario = accesorioForm(request.POST)
        if formulario.is_valid:
            formulario.save()
            data['mensaje'] = "Guardados Correctamente"
        else:
            data ['form'] = formulario
    return render (request, 'core/form_accesorio.html', data)

"""AGREGAR LOS PRODUCTOS COMIDA PARA PERRO"""
@permission_required('core.add_comidaperro')
@permission_required('core.change_comidaperro')
@permission_required('core.delete_comidaperro')
def form_agregar_comida_perro(request):
    data = {
        'form': agregarcomidaPerroForm()
    }

    if request.method == 'POST':
        formulario = agregarcomidaPerroForm(request.POST)
        if formulario.is_valid:
            formulario.save()
            data['mensaje'] = "Guardados Correctamente"
        else:
            data ['form'] = formulario
    return render (request, 'core/form_agregar_comida_perro.html', data)


"""AGREGAR LOS PRODUCTOS COMIDA PARA GATO"""
@permission_required('core.add_comidagato')
@permission_required('core.change_comidagato')
@permission_required('core.delete_comidagato')
def form_agregar_comida_gato(request):
    data = {
        'form': agregarcomidaGatoForm()
    }

    if request.method == 'POST':
        formulario = agregarcomidaGatoForm(request.POST)
        if formulario.is_valid:
            formulario.save()
            data['mensaje'] = "Guardados Correctamente"
        else:
            data ['form'] = formulario
    return render (request, 'core/form_agregar_comida_gato.html', data)

"""MODIFICAR LOS PRODUCTOS ACCESORIOS"""

def form_modi_productos(request, id):

    accesorios =  accesorio.objects.get(idAccesorio=id)
    datos = {
        'form': accesorioForm(instance=accesorios)
    }
    if request.method == 'POST':
        formulario = accesorioForm(data=request.POST, instance=accesorios)
        if formulario.is_valid():
            formulario.save()
            datos['mensaje'] = "Modificado Correctamente"
            return redirect (to="listaraccesorios")
        else:
            datos ['form'] = formulario

    return render(request, 'core/form_modi_productos.html',datos)

"""MODIFICAR LOS PRODUCTOS DE COMIDA PARA PERRO"""
def form_modi_perro(request, id):

    produccomidaperro = comidaperro.objects.get(idPerro=id)
    datos = {
        'form': agregarcomidaPerroForm(instance=produccomidaperro)
    }
    if request.method == 'POST':
        formulario = agregarcomidaPerroForm(data=request.POST, instance=produccomidaperro)
        if formulario.is_valid():
            formulario.save()
            datos['mensaje'] = "Modificado Correctamente"
            return redirect (to="listarperro")
        else:
            datos ['form'] = formulario

    return render(request, 'core/form_modi_perro.html',datos)

"""MODIFICAR LOS PRODUCTOS COMIDA PARA GATO"""

def form_modi_gato(request, id):

    produccomidagato = comidagato.objects.get(idGato=id)
    datos = {
        'form': agregarcomidaGatoForm(instance=produccomidagato)
    }
    if request.method == 'POST':
        formulario = agregarcomidaGatoForm(data=request.POST, instance=produccomidagato)
        if formulario.is_valid():
            formulario.save()
            datos['mensaje'] = "Modificado Correctamente"
            return redirect (to="listarproductos")
        else:
            datos ['form'] = formulario

    return render(request, 'core/form_modi_gato.html',datos)

"""ELIMINAR PRODUCTOS"""

def eliminar_accesorio(request, id):
    accesorios =  accesorio.objects.get(idAccesorio=id)
    accesorios.delete()
    return redirect (to="listaraccesorios")


"""ELIMINAR COMIDA GATO"""

def eliminar_comida_gato(request, id):
    comidagatos =  comidagato.objects.get(idGato=id)
    comidagatos.delete()
    return redirect (to="listaraccesorios")


"""ELIMINAR COMIDA PERRO"""

def eliminar_comida_perro(request, id):
    comidaperros =  comidaperro.objects.get(idPerro=id)
    comidaperros.delete()
    return redirect (to="listarperro")

def registro (request):
    data = {
        'form': formregistrousuario()
    } 
    if request.method == 'POST':
        formulario = formregistrousuario(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(usarname=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            return redirect(to="index")
        data["form"] = formulario
    return render (request, 'registration/registrarse.html',data)



@csrf_exempt
@api_view(['GET','POST'])
def listar_accesorios_api(request):

    if request.method =='GET':
        accesorios = accesorio.objects.all()
        serializer = accesorioSerializer(accesorios, many=True)
        return Response(serializer.data)
    elif  request.method =='POST':
        data = JSONParser().parse(request)
        serializer = accesorioSerializer(data=data)
        if serializer.is_valid():

            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def login_api(request):
    data = JSONParser().parse(request)

    username = data ['username']
    password = data ['password']

    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        return Response("Usuario invalido")
    pass_valido = check_password(password, user.password)
    if not pass_valido:
        return Response("password incorrecta")

    token, created = Token.objects.get_or_create(user=user)
    return Response(token.key)
    
