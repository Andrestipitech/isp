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
            'descripcion',
            'velocidad',
            'tipo',
            
        ]

        labels = {
            'descripcion':'Descripcion',
            'velocidad':'Velocidad',
            'tipo': 'Tipo',
            
            
        }
        widgets={
            'descripcion':forms.TextInput(attrs={'class':'form-control'}),
            'velocidad':forms.NumberInput(attrs={'class':'form-control'}),
            'tipo':forms.Select(attrs={'class':'form-control'}),
            
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
class ContratoForm(forms.ModelForm):
    class Meta:
        model = Contrato
        fields=[
            'fecha',
            'cliente',
            'plan'
        ]

        labels = {
           
            'fecha':'Fecha',
            'cliente':'Cliente',
            'plan':'Plan'
            
        }
        widgets={
            
            'fecha':forms.DateTimeInput(attrs={'class':'form-control', 'type':'date'}),
            'cliente':forms.Select(attrs={'class':'form-control'}),
            'plan':forms.Select(attrs={'class':'form-control'}),
            
        
        }

class InfraestructuraForm(forms.ModelForm):
    class Meta:
        model = Infraestructura
        fields=[
            'tipo_t',
            'contrato',
            'fecha',
            'observacion'
        ]

        labels = {
            'tipo_t':'Tipo Trabajo',
            'contrato':'contrato',
            'fecha':'Fecha',
            'observacion':'Observacion'
            
        }
        widgets={
            'tipo_t':forms.Select(attrs={'class':'form-control'}),
            'contrato':forms.Select(attrs={'class':'form-control'}),
            'fecha':forms.DateTimeInput(attrs={'class':'form-control', 'type':'date'}),
            'observacion':forms.Textarea(attrs={'class':'form-control'})
            
        
        }
