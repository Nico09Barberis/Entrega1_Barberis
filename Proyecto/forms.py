from django import forms
from ckeditor.fields import RichTextFormField

class FormAuto(forms.Form):
    marca = forms.CharField(max_length=30)
    modelo = forms.IntegerField()
    descripcion = RichTextFormField(required=False)
    fecha_creacion = forms.DateField(required=False)
    
    
    
class BusquedaAuto(forms.Form):
    marca = forms.CharField(max_length=30, required=False) 