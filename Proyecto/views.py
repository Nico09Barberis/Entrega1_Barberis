from django.http import HttpResponse
from .models import Prueba
from django.template import loader
from django.shortcuts import render

# Create your views here.

def primera_vista(request):
    return HttpResponse('<h1>PERRO DINAMITA</h1>')

def un_template(request):
   
    # template = loader.get_template('índex.html')
    
    prueba1 = Prueba(nombre='Pepito')
    prueba2= Prueba(nombre='Pito')
    prueba3 = Prueba(nombre='Tito')
    prueba1.save()
    prueba2.save()
    prueba3.save()
    
    # render = template.render({'lista_objetos': [prueba1, prueba2, prueba3]})
    
    return render(request, 'índex.html', {'lista_objetos': [prueba1, prueba2, prueba3]})
