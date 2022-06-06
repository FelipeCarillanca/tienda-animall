from django.db import models

# Create your models here.
class comidagatos(models.Model):
    codigo = models.CharField(max_length=11, unique=True)
    nombre = models.CharField(max_length=50)

class comidaperro(models.Model):
    codigo = models.CharField(max_length=11, unique=True)
    nombre = models.CharField(max_length=50)


