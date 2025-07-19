# labores/forms.py
from django import forms
from .models import Labor

class LaborForm(forms.ModelForm):
    class Meta:
        model = Labor
        fields = '__all__'
