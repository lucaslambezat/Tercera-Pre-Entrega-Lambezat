from django.db import models
from django.contrib.auth.models import User

# Create your models here.

#Voy a crear los modelos que escribimos la clase anterior. Son las tablas o modelos que van a componer nuestro proyecto.

class Mantenimiento(models.Model):

    numero_operacion = models.IntegerField()
    descripcion = models.CharField(max_length=100)
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

class Avatar(models.Model):
    imagen = models.ImageField(upload_to="avatares")
    user = models.ForeignKey(User, on_delete= models.CASCADE)

    def __str__(self):
        return f"{self.user} [{self.imagen}]"