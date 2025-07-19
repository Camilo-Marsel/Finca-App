from django.db import models
from fincas.models import Finca

# Create your models here.
class Trabajador(models.Model):
    TIPO_DOCUMENTO_CHOICES = [
        ('CC', 'Cédula de ciudadanía'),
        ('CE', 'Cédula de extranjería'),
        ('TI', 'Tarjeta de identidad'),
    ]

    nombre_completo = models.CharField(max_length=100)
    finca = models.ForeignKey(Finca, on_delete=models.SET_NULL, null=True, blank=True)
    tipo_documento = models.CharField(max_length=2, choices=TIPO_DOCUMENTO_CHOICES)
    numero_documento = models.CharField(max_length=20, unique=True)
    telefono = models.CharField(max_length=15, blank=True, null=True)
    correo = models.EmailField(blank=True, null=True)
    direccion = models.TextField(blank=True, null=True)
    fecha_nacimiento = models.DateField(blank=True, null=True)
    fecha_ingreso = models.DateField()
    activo = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.nombre_completo} ({self.numero_documento})'


#-------------contratos------------------------------------

class Contrato(models.Model):
    trabajador = models.ForeignKey(Trabajador, on_delete=models.CASCADE, related_name='contratos')
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    tipo = models.CharField(max_length=50)  # Por ejemplo: fijo, temporal, etc.
    salario = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'Contrato de {self.trabajador} ({self.fecha_inicio} a {self.fecha_fin})'
