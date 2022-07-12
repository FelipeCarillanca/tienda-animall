from urllib.parse import urlparse
from django.urls import path, include
from .views import *
from rest_framework import routers
from django.contrib import admin


router = routers.DefaultRouter()
router.register('comidaGato', comidagatoViewset)
router.register('comidaPerro', comidaperroViewset)
router.register('accesorios', accesorioViewset)


urlpatterns = [
   path('', index,name="index") ,
   path('gatos/', gatos,name="gatos"),
   path('accesorios/', accesorios,name="accesorios"), 
   path('login/', login,name="login"),
   path('mostrarperros/', mostrarperros,name="mostrarperros"),
   path('perros/', perros,name="perros"),
   path('listarproductos/', listarproductos,name="listarproductos"),
   path('listarperro/', listarperro,name="listarperro"),
   path('listaraccesorios/', listaraccesorios,name="listaraccesorios"),
   path('carro/', carro,name="carro"),
   path('form_accesorio/', form_accesorio, name="form_accesorio"),
   path('form_agregar_comida_perro/', form_agregar_comida_perro, name="form_agregar_comida_perro"),
   path('form_agregar_comida_gato/', form_agregar_comida_gato, name="form_agregar_comida_gato"),
   path('form_modi_productos/<id>/', form_modi_productos, name="form_modi_productos"),
   path('form_modi_perro/<id>/',     form_modi_perro,     name="form_modi_perro"),
   path('form_modi_gato/<id>/',     form_modi_gato,     name="form_modi_gato"),
   path('eliminar_accesorio/<id>/',     eliminar_accesorio,     name="eliminar_accesorio"),
   path('eliminar_comida_gato/<id>/',     eliminar_comida_gato,     name="eliminar_comida_gato"),
   path('eliminar_comida_perro/<id>/',     eliminar_comida_perro,     name="eliminar_comida_perro"),
   path('registro/', registro, name="registro"),



   path('api/', include(router.urls)),
   
  
   
]