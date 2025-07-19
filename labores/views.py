from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .models import Labor

class LaborListView(ListView):
    model = Labor
    template_name = 'labores/labor_list.html'
    context_object_name = 'labores'

class LaborDetailView(DetailView):
    model = Labor
    template_name = 'labores/labor_detail.html'
    context_object_name = 'labor'

class LaborCreateView(CreateView):
    model = Labor
    template_name = 'labores/labor_form.html'
    fields = ['trabajador', 'fecha', 'tipo_labor', 'forma_medicion', 'cantidad', 'lote', 'observaciones']
    success_url = reverse_lazy('labores:lista_labores')

class LaborUpdateView(UpdateView):
    model = Labor
    template_name = 'labores/labor_form.html'
    fields = ['trabajador', 'fecha', 'tipo_labor', 'forma_medicion', 'cantidad', 'lote', 'observaciones']
    success_url = reverse_lazy('labores:lista_labores')

class LaborDeleteView(DeleteView):
    model = Labor
    template_name = 'labores/labor_confirm_delete.html'
    success_url = reverse_lazy('labores:lista_labores')
