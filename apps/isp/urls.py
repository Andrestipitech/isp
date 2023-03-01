from django.urls import path
from . import views
from django.contrib.auth.views import LoginView
from django.contrib.auth import views as auth_views
app_name ='isp'

urlpatterns = [
    path('login/',LoginView.as_view(template_name ='login.html'), name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name ='login.html'), name='logout'),
    path('isp/',views.prueba, name='index'),
    path('new_plan/',views.crear_plan, name='new_plan'),
    path('new_cliente/',views.crear_cliente, name='new_cliente'),
    path('new_personal/',views.crear_personal, name='new_personal'),
    path('new_vehiculo/',views.crear_vehiculo, name='new_vehiculo'),
    path('new_contrato/',views.crear_contrato, name='new_contrato'),
    path('new_infra/',views.crear_infra, name='new_infra'),
    # listat los elementos
    path('list_contrato/',views.listar_contratos, name='list_contrato'),
    path('list_cliente/',views.listar_cliente, name='list_cliente'),

    # actualizar elementos
    path('up_cliente/<str:id_clie>',views.actualizar_cliente, name='up_cliente'),
    path('up_c/<str:pk>',views.Actualizar_client.as_view(), name='up_c'),
    path('up_contr/<int:pk>',views.Actualizar_contrato.as_view(), name='up_contr'),


   # path('new_infraestructura/',views.crear_infraestrcutura, name='new_infraestructura'),

]
