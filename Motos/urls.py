from django.urls import path
from . import views

urlpatterns = [
    path('motos/',views.ListadoMotos.as_view(), name='listado_motos'),
    path('crear-moto/', views.CrearMoto.as_view(), name='crear_moto'),
    path('editar-moto/<int:pk>/', views.EditarMoto.as_view(), name='editar_moto'),
    path('eliminar-moto/<int:pk>/', views.EliminarMoto.as_view(), name='eliminar_moto'),
    path('mostrar-moto/<int:pk>/', views.MostrarMoto.as_view(), name='mostrar_moto'),
    
]
