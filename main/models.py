from django.db import models
#from django.template.defaultfilters import slugify
#from django.contrib.auth.models import User

# Create your models here.
class courses_tiendas(models.Model):
    id = models.AutoField(primary_key=True)
    name=models.CharField(max_length=140)
class courses_cajas(models.Model):
    identificador = models.AutoField(primary_key=True)
    certificada=models.BooleanField(default=True)
    tienda= models.ForeignKey(courses_tiendas, on_delete=models.CASCADE)
#es una factura no un curso
class courses_courses(models.Model):
    #tiene que tener identificador guaches :v
    fecha= models.DateTimeField()
    cantidad=models.IntegerField()
    tipo=models.CharField(max_length=100)
    registradora=models.ForeignKey(courses_cajas, on_delete=models.CASCADE)

class courses_productos(models.Model):
    identificador = models.AutoField(primary_key=True)
    precio = models.IntegerField()
    cantidad = models.IntegerField()
    fact= models.ForeignKey(courses_courses, on_delete=models.CASCADE)