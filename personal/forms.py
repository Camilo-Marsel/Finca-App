# forms.py
from django import forms
from .models import Trabajador

class TrabajadorForm(forms.ModelForm):
    class Meta:
        model = Trabajador
        fields = '__all__'

#--------------contratos------------------

from django import forms
from .models import Contrato

class ContratoForm(forms.ModelForm):
    class Meta:
        model = Contrato
        fields = ['trabajador', 'fecha_inicio', 'fecha_fin', 'tipo', 'salario']
