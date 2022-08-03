from django import forms
from ckeditor.fields import RichTextFormField

class FormBlog(forms.Form):
    titulo = forms.CharField(max_length=30)
    subtitulo = forms.CharField(max_length=40)
    contenido = RichTextFormField(required=False)
    autor = forms.CharField(max_length=30)
    fecha_creacion = forms.DateField(required=False)
    
    
     
class BusquedaBlog(forms.Form):
    titulo = forms.CharField(max_length=30, required=False) 
    