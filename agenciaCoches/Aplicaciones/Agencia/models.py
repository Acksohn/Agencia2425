from django.db import models

# Create your models here.

class Ciudad(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=250,default="Desconocido")
    def __str__(self):
        return self.nombre


class Modelo(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=250,default="Desconocido")
    def __str__(self):
        return self.nombre


class Propietario(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=250,default="Desconocido")
    apellido = models.CharField(max_length=250,default="Desconocido")
    email = models.CharField(max_length=250,default="Desconocido")
    telefono = models.CharField(max_length=250,default="Desconocido")
    ciudad =  models.ForeignKey(Ciudad, on_delete=models.CASCADE)
    def __str__(self):
        return self.nombre


class Vehiculo(models.Model):
    id = models.AutoField(primary_key=True)
    fabricacion = models.CharField(max_length=250,default="Desconocido")
    precio = models.CharField(max_length=250,default="Desconocido")
    placa = models.CharField(max_length=250,default="Desconocido")
    modelo = models.ForeignKey(Modelo, on_delete=models.CASCADE)
    propietario = models.ForeignKey(Propietario, on_delete=models.CASCADE)
    def __str__(self):
        return self.placa
    