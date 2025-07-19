from django.db import models

from django.db import models
from personal.models import Trabajador
from fincas.models import Lote  # importante importar desde nueva app

class Labor(models.Model):
    FORMAS_MEDICION = [
        ('día', 'Por día'),
        ('hectarea', 'Por hectárea'),
        ('metro', 'Por metro'),
        ('unidad', 'Por unidad'),
    ]

    trabajador = models.ForeignKey(Trabajador, on_delete=models.CASCADE)
    fecha = models.DateField()
    tipo_labor = models.CharField(max_length=100)
    forma_medicion = models.CharField(max_length=20, choices=FORMAS_MEDICION)
    cantidad = models.DecimalField(max_digits=10, decimal_places=2)
    lote = models.ForeignKey(Lote, on_delete=models.SET_NULL, null=True, blank=True)

    observaciones = models.TextField(blank=True)

    def __str__(self):
        return f"{self.tipo_labor} - {self.trabajador} - {self.fecha}"
