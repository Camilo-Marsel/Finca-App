from django.urls import path
from . import views

urlpatterns = [
    path('trabajadores/', views.listar_trabajadores, name='listar_trabajadores'),
    path('trabajadores/crear/', views.crear_trabajador, name='crear_trabajador'),
    path('trabajadores/editar/<int:pk>/', views.editar_trabajador, name='editar_trabajador'),
    path('trabajadores/eliminar/<int:pk>/', views.eliminar_trabajador, name='eliminar_trabajador'),
]

urlpatterns += [
    path('contratos/', views.listar_contratos, name='listar_contratos'),
    path('contratos/crear/', views.crear_contrato, name='crear_contrato'),
    path('contratos/editar/<int:pk>/', views.editar_contrato, name='editar_contrato'),
    path('contratos/eliminar/<int:pk>/', views.eliminar_contrato, name='eliminar_contrato'),
]