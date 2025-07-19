# views.py
from django.shortcuts import render, redirect
from .forms import TrabajadorForm
from .models import Trabajador
from django.shortcuts import get_object_or_404

def crear_trabajador(request):
    form = TrabajadorForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('listar_trabajadores')
    return render(request, 'personal/crear_trabajador.html', {'form': form})

def listar_trabajadores(request):
    trabajadores = Trabajador.objects.all()
    return render(request, 'personal/listar_trabajadores.html', {'trabajadores': trabajadores})



def editar_trabajador(request, pk):
    trabajador = get_object_or_404(Trabajador, pk=pk)
    form = TrabajadorForm(request.POST or None, instance=trabajador)
    if form.is_valid():
        form.save()
        return redirect('listar_trabajadores')
    return render(request, 'personal/editar_trabajador.html', {'form': form})

def eliminar_trabajador(request, pk):
    trabajador = get_object_or_404(Trabajador, pk=pk)
    if request.method == 'POST':
        trabajador.delete()
        return redirect('listar_trabajadores')
    return render(request, 'personal/eliminar_trabajador.html', {'trabajador': trabajador})



#------------------Contratos------------------------------

from .models import Contrato
from .forms import ContratoForm

def listar_contratos(request):
    contratos = Contrato.objects.select_related('trabajador').all()
    return render(request, 'contratos/listar_contratos.html', {'contratos': contratos})

def crear_contrato(request):
    form = ContratoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('listar_contratos')
    return render(request, 'contratos/crear_contrato.html', {'form': form})

def editar_contrato(request, pk):
    contrato = get_object_or_404(Contrato, pk=pk)
    form = ContratoForm(request.POST or None, instance=contrato)
    if form.is_valid():
        form.save()
        return redirect('listar_contratos')
    return render(request, 'contratos/editar_contrato.html', {'form': form})

def eliminar_contrato(request, pk):
    contrato = get_object_or_404(Contrato, pk=pk)
    if request.method == 'POST':
        contrato.delete()
        return redirect('listar_contratos')
    return render(request, 'contratos/eliminar_contrato.html', {'contrato': contrato})
