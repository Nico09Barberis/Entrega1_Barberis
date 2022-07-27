from django.views.generic.list import ListView
from django.views.generic.edit import DeleteView, CreateView, UpdateView
from django.views.generic import DetailView 
from.models import Moto



class ListadoMotos(ListView):
    model = Moto
    template_name = 'moto/listado_motos.html'

    

class CrearMoto(CreateView):
    model = Moto
    template_name = 'moto/crear_moto.html'
    success_url = '/moto/motos'
    fields = ['nombre', 'modelo', 'fecha_creacion']
    
    

class EditarMoto(UpdateView):
    model = Moto
    template_name = 'moto/editar_moto.html'
    success_url = '/moto/motos'
    fields = ['nombre', 'modelo', 'fecha_creacion']

    
    
class EliminarMoto(DeleteView):
    model = Moto
    template_name = 'moto/eliminar_moto.html'
    success_url = '/moto/motos'
    
    

class MostrarMoto(DetailView):
    model = Moto
    template_name =  "moto/mostrar_moto.html"
