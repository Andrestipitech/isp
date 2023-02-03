from django.urls import path
from . import views
app_name ='isp'

urlpatterns = [
    path('isp/',views.prueba, name='index'),
    path('new_plan/',views.crear_plan, name='new_plan'),
]
