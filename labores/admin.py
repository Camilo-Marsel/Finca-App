from django.contrib import admin

from django.contrib import admin
from .models import Labor

@admin.register(Labor)
class LaborAdmin(admin.ModelAdmin):
    list_display = ('tipo_labor', 'trabajador', 'fecha', 'forma_medicion', 'cantidad', 'lote')
    list_filter = ('fecha', 'forma_medicion', 'trabajador')
    search_fields = ('tipo_labor', 'trabajador__nombre')
