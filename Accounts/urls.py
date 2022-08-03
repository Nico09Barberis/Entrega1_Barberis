from django.conf import settings
from django.urls import path
from.views import login, register, perfil, editar_perfil, ChangePasswordView, acerca_nos
from django.contrib.auth.views import LogoutView

 
urlpatterns = [
    path('login/', login, name='login'),
    path('register/', register, name='register'),
    path('perfil/', perfil, name='perfil'),
    path('perfil/editar/', editar_perfil, name='editar_perfil'),
    path('logout/', LogoutView.as_view(template_name='accounts/logout.html'), name='logout'),
    path('perfil/cambiar-password/', ChangePasswordView.as_view(), name='cambiar_password'),
    path('acerca-nos/', acerca_nos, name='acerca_nos'),
    
]

