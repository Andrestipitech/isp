from django.urls import path
from . import views
app_name ='isp'

urlpatterns = [
    path('isp/',views.prueba, name='index'),
    path('new_plan/',views.crear_plan, name='new_plan'),
    path('new_cliente/',views.crear_cliente, name='new_cliente'),
    path('new_personal/',views.crear_personal, name='new_personal'),
    path('new_vehiculo/',views.crear_vehiculo, name='new_vehiculo'),


]
