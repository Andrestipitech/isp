from django.db import models

# Create your models here.
class clientes(models.Model):
    dni = models.IntegerField(unique=True,max_length=10)
    nombre = models.CharField()
    apellido = models.CharField()
    edad = models.IntegerField()
    genero = models.CharField(choices=['masculino','femenino'])
    domicilio = models.CharField()
    correo = models.EmailField()

    def __str__(self):
        return self.dni
class planes(models.Model):
    velocidad = models.CharField(choices=['50','100','200'])
    descripcion = models.TextField(max_length=100)

    def __str__(self):
        return self.velocidad

class personal(models.Model):
    genero = (('Femenino', 'Femenino'), ('Masculino', 'Masculino'))
    dni = models.IntegerField(unique=True,max_length=10)
    nombre = models.CharField()
    apellido = models.CharField()
    edad = models.IntegerField()
    genero = models.CharField(choices=genero, default = 'Femenino')
    domicilio = models.CharField()
    correo = models.EmailField()
    cargo = models.CharField()

    def __str__(self):
        return self.cargo

class vehiculos(models.Model):
    tipo = models.CharField()
    modelo = models.CharField()
    placa = models.CharField()
    
    def __str__(self):
        return self.placa
    