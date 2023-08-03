from django.db import models

# Create your models here.

class Mantenimiento(models.Model):

    numero_operacion = models.IntegerField()
    descripcion = models.CharField(max_length=100)
    #planificado = models.BooleanField()
    planificado = models.CharField(max_length=10)
    fecha = models.CharField(max_length=10)

class Equipo(models.Model):

    nombre = models.CharField(max_length=50)
    marca = models.CharField(max_length=50)
    sector = models.CharField(max_length=50)
    referencia = models.CharField(max_length=6)
    

class Empleado(models.Model):

    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    rol = models.CharField(max_length=50)
    email = models.EmailField()
    telefono = models.CharField(max_length=50)
