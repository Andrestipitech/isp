from django.shortcuts import render, redirect
from apps.isp.forms import *
# Create your views here.
def prueba(request):
    return render(request,'index.html')

def crear_plan(request):
    if request.method == 'POST':
        form = PlanForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('isp:index')
    else:
        form = PlanForm()
    return render(request, 'planes.html', {'form':form})

def crear_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('isp:index')
    else:
        form = ClienteForm()
    return render(request, 'clientes.html', {'form':form})

def crear_personal(request):
    if request.method == 'POST':
        form = PersonalForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('isp:index')
    else:
        form = PersonalForm()
    return render(request, 'personal.html', {'form':form})

def crear_vehiculo(request):
    if request.method == 'POST':
        form = VehiculoForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('isp:index')
    else:
        form = VehiculoForm()
    return render(request, 'vehiculos.html', {'form':form})

def crear_contrato(request):
    if request.method == 'POST':
        form = ContratoForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('isp:index')
    else:
        form = ContratoForm()
    return render(request, 'contrato.html', {'form':form})

def crear_infra(request):
    if request.method == 'POST':
        form = InfraestructuraForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('isp:index')
    else:
        form = InfraestructuraForm()
    return render(request, 'infraestructura.html', {'form':form})