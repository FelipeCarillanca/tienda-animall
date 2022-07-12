from django.urls import path, include
from rest_petshop.views import listar_accesorios_api
from . import views


urlpatterns = [
    path('listar_accesorios_api', listar_accesorios_api, name="listar_accesorios_api"),

]