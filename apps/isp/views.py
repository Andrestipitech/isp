from django.shortcuts import render, redirect
from apps.isp.forms import *
from django.urls import reverse_lazy
from django.views.generic import FormView
from django.views.generic import CreateView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from apps.isp.models import *
class Home(LoginRequiredMixin, TemplateView):
    template_name ='index.html'
    login_url = 'isp:login'
@login_required(login_url="/login/")
def prueba(request):
    return render(request,'index.html')



@login_required(login_url="/login/")
def crear_plan(request):
    if request.method == 'POST':
        form = PlanForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('isp:index')
    else:
        form = PlanForm()
    return render(request, 'planes.html', {'form':form})
@login_required(login_url="/login/")
def crear_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('isp:index')
    else:
        form = ClienteForm()
    return render(request, 'cliente.html', {'form':form})
@login_required(login_url="/login/")
def crear_personal(request):
    if request.method == 'POST':
        form = PersonalForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('isp:index')
    else:
        form = PersonalForm()
    return render(request, 'personal.html', {'form':form})
@login_required(login_url="/login/")
def crear_vehiculo(request):
    if request.method == 'POST':
        form = VehiculoForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('isp:index')
    else:
        form = VehiculoForm()
    return render(request, 'vehiculos.html', {'form':form})
@login_required(login_url="/login/")
def crear_contrato(request):
    if request.method == 'POST':
        form = ContratoForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('isp:index')
    else:
        form = ContratoForm()
    return render(request, 'contrato.html', {'form':form})
@login_required(login_url="/login/")
def crear_infra(request):
    if request.method == 'POST':
        form = InfraestructuraForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('isp:index')
    else:
        form = InfraestructuraForm()
    return render(request, 'infraestructura.html', {'form':form})


# listar elementos 
def listar_contratos(request):
    obj_contrato = Contrato.objects.all()

    return render(request,'listar_contratos.html',{'contrato':obj_contrato})



def listar_cliente(request):
    obj_cliente = clientes.objects.all()

    return render(request,'listar_clientes.html',{'cliente':obj_cliente})


def actualizar_form_cliente(request):

    context = {
        'actualiza':clientes.objects.get(id=request.POST["idCliente"])
        }
    return render(request, 'cliente.html',context)

    
def actualizar_cliente(request):
    a_dni_cli = request.POST["dni"]
 