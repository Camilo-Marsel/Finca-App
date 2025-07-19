from django.db import models

from django.db import models

class Finca(models.Model):
    nombre = models.CharField(max_length=100)
    ubicacion = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre

class Lote(models.Model):
    finca = models.ForeignKey(Finca, on_delete=models.CASCADE, related_name="lotes")
    nombre = models.CharField(max_length=100)
    tamaño_m2 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    descripcion = models.TextField(blank=True)

    def __str__(self):
        return f"{self.nombre} ({self.finca.nombre})"
