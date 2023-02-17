from django.urls import path
from . import views
from django.contrib.auth.views import LoginView
app_name ='isp'

urlpatterns = [
    path('isp/',views.prueba, name='index'),
    path('',views.login, name='login'),
    path('new_plan/',views.crear_plan, name='new_plan'),
    path('new_cliente/',views.crear_cliente, name='new_cliente'),
    path('new_personal/',views.crear_personal, name='new_personal'),
    path('new_vehiculo/',views.crear_vehiculo, name='new_vehiculo'),
    path('new_contrato/',views.crear_contrato, name='new_contrato'),
    path('new_infra/',views.crear_infra, name='new_infra'),
    

   # path('new_infraestructura/',views.crear_infraestrcutura, name='new_infraestructura'),


]
