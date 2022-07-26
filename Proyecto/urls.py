from django.urls import path
from .views import primera_vista, crear_auto, listado_autos

urlpatterns = [
    path('', primera_vista, name='index'),
    path('autos/', listado_autos, name='listado_autos'),
    path('crear-auto/', crear_auto, name='crear_auto'),
]
