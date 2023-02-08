from django.contrib import admin
from apps.isp.models import *

class DataPlanes(admin.ModelAdmin):
    search_fields =['id_plan']
    list_display =('id_plan', 'velocidad', 'descripcion')
    
class DataContrato(admin.ModelAdmin):
    search_fields =['id_contrato']
    list_display =('id_contrato', 'fecha', 'cliente', 'plan')

admin.site.register(clientes)
admin.site.register(planes, DataPlanes)
admin.site.register(personal)
admin.site.register(vehiculos)
admin.site.register(Contrato, DataContrato)
admin.site.register(Infraestructura)