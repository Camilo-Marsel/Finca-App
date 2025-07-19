from django.urls import path
from .views import (
    LaborListView,
    LaborDetailView,
    LaborCreateView,
    LaborUpdateView,
    LaborDeleteView,
)

app_name = 'labores'

urlpatterns = [
    path('', LaborListView.as_view(), name='listar_labores'),
    path('<int:pk>/', LaborDetailView.as_view(), name='detalle_labor'),
    path('crear/', LaborCreateView.as_view(), name='crear_labor'),
    path('<int:pk>/editar/', LaborUpdateView.as_view(), name='editar_labor'),
    path('<int:pk>/eliminar/', LaborDeleteView.as_view(), name='eliminar_labor'),
]
