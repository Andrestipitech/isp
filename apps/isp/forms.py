from django import forms
from .models import *

class ClienteForm(forms.ModelForm):
    class Meta:
        model = clientes
        fields=[
            'dni',
            'nombre',
            'apellido',
            'edad',
            'genero',
            'domicilio',
            'correo'
        ]

        labels = {
            'dni':'cedula',
            'nombre':'Nombre',
            'apellido':'Apellido',
            'edad':'Edad',
            'genero':'Genero',
            'domicilio':'Domicilio',
            'correo':'email'
        }
        widgets={
            'dni':forms.TextInput(attrs={'class':'form-control'}),
            'nombre':forms.TextInput(attrs={'class':'form-control'}),
            'apellido':forms.TextInput(attrs={'class':'form-control'}),
            'edad':forms.NumberInput(attrs={'class':'form-control'}),
            'genero':forms.Select(attrs={'class':'form-control'}),
            'domicilio':forms.TextInput(attrs={'class':'form-control'}),
            'correo':forms.TextInput(attrs={'class':'form-control'}),
        }

class PlanForm(forms.ModelForm):
    class Meta:
        model = planes
        fields=[
            'velocidad',
            'descripcion'
        ]

        labels = {
            'velocidad':'Velocidad',
            'descripcion':'Descripcion'
            
        }
        widgets={
            'velocidad':forms.Select(attrs={'class':'form-control'}),
            'descripcion':forms.TextInput(attrs={'class':'form-control'})
        }

class PersonalForm(forms.ModelForm):
    class Meta:
        model = personal
        fields=[
            'dni',
            'nombre',
            'apellido',
            'edad',
            'genero',
            'domicilio',
            'correo',
            'cargo'
        ]

        labels = {
            'dni':'cedula',
            'nombre':'Nombre',
            'apellido':'Apellido',
            'edad':'Edad',
            'genero':'Genero',
            'domicilio':'Domicilio',
            'correo':'email',
            'cargo':'Cargo'
        }
        widgets={
            'dni':forms.TextInput(attrs={'class':'form-control'}),
            'nombre':forms.TextInput(attrs={'class':'form-control'}),
            'apellido':forms.TextInput(attrs={'class':'form-control'}),
            'edad':forms.NumberInput(attrs={'class':'form-control'}),
            'genero':forms.Select(attrs={'class':'form-control'}),
            'domicilio':forms.TextInput(attrs={'class':'form-control'}),
            'correo':forms.TextInput(attrs={'class':'form-control'}),
            'cargo':forms.Select(attrs={'class':'form-control'})

        }

class VehiculoForm(forms.ModelForm):
    class Meta:
        model = vehiculos
        fields=[
            'placa',
            'tipo',
            'modelo'
        ]

        labels = {
            'placa':'Placa',
            'tipo':'Tipo',
            'modelo':'Modelo'
            
        }
        widgets={
            'placa':forms.TextInput(attrs={'class':'form-control'}),
            'tipo':forms.TextInput(attrs={'class':'form-control'}),
            'modelo':forms.TextInput(attrs={'class':'form-control'})
        
        }