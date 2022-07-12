from email import message
from gc import get_objects
from django.shortcuts import render, redirect, get_object_or_404
from core.models import comidagato, comidaperro, accesorio
from rest_framework import viewsets
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse 
from .serializers import comidagatoSerializer, comidaperroSerializer, accesorioSerializer




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