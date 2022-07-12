from django.db import models

class comidagato(models.Model):
    idGato = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID comida Gato')
    nombre = models.CharField(max_length=50, null=False)
    precio = models.CharField(max_length=7, null=False)
    descripcion = models.CharField(max_length=50, null=False)

class comidaperro(models.Model):
    idPerro = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID comida Perro')
    nombre = models.CharField(max_length=50, null=False)
    precio = models.CharField(max_length=7, null=False)
    descripcion = models.CharField(max_length=50, null=False)

class accesorio(models.Model):
    idAccesorio = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID accesorio')
    nombre = models.CharField(max_length=50, null=False)
    precio = models.CharField(max_length=7, null=False)
    descripcion = models.CharField(max_length=50, null=False)

class usuario(models.Model):
    idusuario = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID accesorio')
    nombre = models.CharField(max_length=50, null=False)
    apellido = models.CharField(max_length=50, null=False)
    correo = models.CharField(max_length=50, null=False)
    nro_telefono = models.CharField(max_length=7, null=False)
    contrasena = models.CharField(max_length=7, null=False)

    





