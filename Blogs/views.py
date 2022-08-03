from .forms import BusquedaBlog, FormBlog
from .models import Blog
from django.shortcuts import redirect, render
from datetime import datetime
from django.contrib.auth.decorators import login_required


def crear_blog(request):
        
    if request.method == 'POST':
        form = FormBlog(request.POST)
        
        if form.is_valid():
            data = form.cleaned_data
            
            fecha = data.get('fecha_creacion')
            if not fecha:
                fecha = datetime.now()
    
            blog = Blog(titulo = data.get('titulo'), 
                        subtitulo = data.get('subtitulo'),
                        contenido = data.get('contenido'),
                        autor = data.get('autor'),
                        fecha_creacion = fecha
                        ) 
            
            blog.save()
            
            return redirect('listado_blogs')

        else:
            return render(request, 'blog/crear_blog.html', {'form': form})
    
    form_blog = FormBlog()
    return render(request, 'blog/crear_blog.html', {'form': form_blog})

 

def listado_blogs(request):
    
    titulo_busqueda = request.GET.get('titulo')
    
    if titulo_busqueda:
        listado_blogs = Blog.objects.filter(titulo__icontains=titulo_busqueda) 
    else:
        listado_blogs = Blog.objects.all()
        
    form = BusquedaBlog()
    return render(request, 'blog/listado_blogs.html', {'listado_blogs': listado_blogs, 'form': form})

@login_required
def editar_blog(request, id):
    
    blog = Blog.objects.get(id=id)
    
    if request.method == 'POST':
        form = FormBlog(request.POST)
        if form.is_valid():
            blog.titulo = form.cleaned_data.get('titulo')
            blog.subtitulo = form.cleaned_data.get('subtitulo')
            blog.contenido = form.cleaned_data.get('contenido')
            blog.autor = form.cleaned_data.get('autor')
            blog.fecha_creacion = form.cleaned_data.get('fecha_creacion')
            blog.save()
         
            return redirect('listado_blogs')
        
        else:
            return render(request, 'blog/editar_blog.html', {'form': form, 'blog': blog})
    
    form_blog = FormBlog(
        initial={'titulo': blog.titulo, 
                 'subtitulo': blog.subtitulo,
                 'contenido': blog.contenido,
                 'autor': blog.autor,
                 'fecha_creacion': blog.fecha_creacion})
    
    return render(request, 'blog/editar_blog.html', {'form': form_blog, 'blog': blog })

@login_required
def eliminar_blog(request, id):
    blog = Blog.objects.get(id=id)
    blog.delete()
    
    return redirect('listado_blogs')

def mostrar_blog(request, id):
    blog = Blog.objects.get(id=id)
    return render(request, 'blog/mostrar_blog.html', {'blog': blog})
    
    
    
    
 