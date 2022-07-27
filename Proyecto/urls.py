from django.urls import path
from .views import primera_vista, crear_auto, listado_autos, editar_auto, eliminar_auto, mostrar_auto

urlpatterns = [
    path('', primera_vista, name='index'),
    path('autos/', listado_autos, name='listado_autos'),
    path('crear-auto/', crear_auto, name='crear_auto'),
    path('editar-auto/<int:id>/', editar_auto, name='editar_auto'),
    path('eliminar-auto/<int:id>/', eliminar_auto, name='eliminar_auto'),
    path('mostrar-auto/<int:id>/', mostrar_auto, name='mostrar_auto'),
    
    
]
