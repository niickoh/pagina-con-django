from django.db import models

# Create your models here.

class Login(models.Model):
    correo = models.CharField(max_length=50)
    contrasena = models.CharField(max_length=20)
    
    def __str__(self):
        return self.correo

class Producto(models.Model):
    codigo = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=100)
    cantidad = models.IntegerField()
    precio = models.IntegerField()

    def __str__(self):
        return self.codigo

