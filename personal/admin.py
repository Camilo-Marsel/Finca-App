from django.contrib import admin
from .models import Trabajador


@admin.register(Trabajador)
class TrabajadorAdmin(admin.ModelAdmin):
    list_display = ('nombre_completo', 'numero_documento', 'fecha_ingreso', 'activo')
    search_fields = ('nombre_completo', 'numero_documento')

from .models import Contrato

admin.site.register(Contrato)
