from .forms import BusquedaAuto, FormAuto
from .models import Auto
from django.shortcuts import redirect, render
from datetime import datetime
from django.contrib.auth.decorators import login_required

# Create your views here.

def primera_vista(request):
    return render(request, 'index.html')

def crear_auto(request):
        
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
            
            return redirect('listado_autos')

        else:
            return render(request, 'auto/crear_auto.html', {'form': form})
    
    form_auto = FormAuto()
    return render(request, 'auto/crear_auto.html', {'form': form_auto})

def listado_autos(request):
    
    marca_busqueda = request.GET.get('marca')
    
    if marca_busqueda:
        listado_autos = Auto.objects.filter(marca__icontains=marca_busqueda) 
    else:
        listado_autos = Auto.objects.all()
        
    form = BusquedaAuto()
    return render(request, 'auto/listado_autos.html', {'listado_autos': listado_autos, 'form': form})

@login_required
def editar_auto(request, id):
    
    auto = Auto.objects.get(id=id)
    
    if request.method == 'POST':
        form = FormAuto(request.POST)
        if form.is_valid():
            auto.marca = form.cleaned_data.get('marca')
            auto.modelo = form.cleaned_data.get('modelo')
            auto.fecha_creacion = form.cleaned_data.get('fecha_creacion')
            auto.save()
            
            return redirect('listado_autos')
        
        else:
            return render(request, 'auto/editar_auto.html', {'form': form, 'auto': auto})
    
    form_auto = FormAuto(initial={'marca': auto.marca, 'modelo': auto.modelo,'fecha_creacion': auto.fecha_creacion})
    return render(request, 'auto/editar_auto.html', {'form': form_auto, 'auto': auto})

@login_required
def eliminar_auto(request, id):
    auto = Auto.objects.get(id=id)
    auto.delete()
    
    return redirect('listado_autos')

def mostrar_auto(request, id):
    auto = Auto.objects.get(id=id)
    return render(request, 'auto/mostrar_auto.html', {'auto': auto})
    
    
    
    
