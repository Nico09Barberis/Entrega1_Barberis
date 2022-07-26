from django.http import HttpResponse
from .forms import BusquedaAuto, FormAuto
from .models import Auto
from django.template import loader
from django.shortcuts import redirect, render
from datetime import datetime

# Create your views here.

def primera_vista(request):
    return render(request, 'index.html')

def crear_auto(request):
    
    # print(request.GET)
    # marca = request.GET.get('marca')
    # modelo = request.GET.get('modelo')
    
    # auto = Auto(marca=marca, modelo=modelo, fecha_creacion=datetime.now())
    # auto.save()
    
    if request.method == 'POST':
        form = FormAuto(request.POST)
        
        if form.is_valid():
            data = form.cleaned_data
            
            fecha = data.get('fecha_creacion')
            if not fecha:
                fecha = datetime.now()
    
            auto = Auto(marca=data.get('marca'), 
                        modelo=data.get('modelo'),
                        fecha_creacion = fecha
                        ) 
            
            auto.save()
            
            # listado_autos = Auto.objects.all()
            
            # return render(request, 'listado_autos.html', {'listado_autos': listado_autos})
            return redirect('listado_autos')

        else:
            return render(request, 'crear_auto.html', {'form': form})
    
    form_auto = FormAuto()
    return render(request, 'crear_auto.html', {'form': form_auto})

def listado_autos(request):
    
    marca_busqueda = request.GET.get('marca')
    
    if marca_busqueda:
        listado_autos = Auto.objects.filter(marca__icontains=marca_busqueda) 
    else:
        listado_autos = Auto.objects.all()
        
    form = BusquedaAuto()
    return render(request, 'listado_autos.html', {'listado_autos': listado_autos, 'form': form})
        
    

