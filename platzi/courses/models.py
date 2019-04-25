

# Create your models here.
from django.db import models


class Courses(models.Model):
    fecha = models.DateTimeField()
    cantidad = models.IntegerField()
    tipo = models.CharField(max_length=140)


class Cajas(models.Model):
    identificador = models.CharField(max_length=100)
    certificada = models.BooleanField(default=True)


class Productos(models.Model):
    identificador = models.CharField(max_length=100)
    precio = models.FloatField()
    cantidad = models.IntegerField()
