from django.contrib import admin
from apps.isp.models import *

class DataPlanes(admin.ModelAdmin):
    search_fields =['id_plan']
    list_display =('id_plan', 'velocidad', 'descripcion')
admin.site.register(clientes)
admin.site.register(planes, DataPlanes)
admin.site.register(personal)
admin.site.register(vehiculos)