from django.urls import path
from .views import crear_blog, listado_blogs, editar_blog, eliminar_blog, mostrar_blog

urlpatterns = [
    path('blog/', listado_blogs, name='listado_blogs'),
    path('crear-blog/', crear_blog, name='crear_blog'),
    path('editar-blog/<int:id>/', editar_blog, name='editar_blog'),
    path('eliminar-blog/<int:id>/', eliminar_blog, name='eliminar_blog'),
    path('mostrar-blog/<int:id>/', mostrar_blog, name='mostrar_blog'),
]