from django.urls import path
from .views import primera_vista, un_template

urlpatterns = [
    path('', primera_vista),
    path('mi-template/', un_template),
    
]
