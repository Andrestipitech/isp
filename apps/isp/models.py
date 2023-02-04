from django.db import models
from .choices import generos, tipo_planes, tipo_cargo

# Create your models here.
class clientes(models.Model):
    dni = models.CharField(max_length=10, primary_key=True)
    nombre = models.CharField(max_length=70)
    apellido = models.CharField(max_length=70)
    edad = models.IntegerField()
    genero = models.CharField(max_length=10,choices=generos, default = 'Femenino' )
    domicilio = models.CharField(max_length=70)
    correo = models.EmailField()

    def __str__(self):
        return self.dni
class planes(models.Model):
    id_plan=models.AutoField(primary_key=True)
    descripcion = models.TextField(max_length=100)
    velocidad = models.IntegerField()
    tipo = models.TextField(max_length=65,choices=tipo_planes, default = 'Fibra Optica')

    def __str__(self):
        return self.descripcion

class personal(models.Model):
    dni = models.CharField(max_length=10, primary_key=True)
    nombre = models.CharField(max_length=70)
    apellido = models.CharField(max_length=70)
    edad = models.IntegerField()
    genero = models.CharField(max_length=10,choices=generos, default = 'Femenino')
    domicilio = models.CharField(max_length=70)
    correo = models.EmailField()
    cargo = models.CharField(max_length=70, choices=tipo_cargo, default = 'Tecnico 1')

    def __str__(self):
        return self.cargo

class vehiculos(models.Model):
    placa = models.CharField(max_length=10, primary_key=True)
    tipo = models.CharField(max_length=70)
    modelo = models.CharField(max_length=75)
    
    
    def __str__(self):
        return self.placa
    
class Contrato(models.Model):
    id_contrato=models.AutoField(primary_key=True)
    fecha = models.DateField()
    cliente = models.ForeignKey(clientes, null=False, on_delete=models.CASCADE)
    plan = models.ForeignKey(planes, null=False, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id_contrato)