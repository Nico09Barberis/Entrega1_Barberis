from django import forms

class FormAuto(forms.Form):
    marca = forms.CharField(max_length=30)
    modelo = forms.IntegerField()
    fecha_creacion = forms.DateField(required=False)
    
class BusquedaAuto(forms.Form):
    marca = forms.CharField(max_length=30, required=False)