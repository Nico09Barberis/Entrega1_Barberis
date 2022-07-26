from django.db import models

# Create your models here.

class Auto(models.Model):
    marca = models.CharField(max_length=30)
    modelo = models.IntegerField()
    fecha_creacion = models.DateField(null=True)
    
    def __str__(self):
        return f'Marca: {self.marca}'