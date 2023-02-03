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