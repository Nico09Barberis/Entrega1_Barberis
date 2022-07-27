from django.db import models

# Create your models here.

class Moto(models.Model):
    nombre = models.CharField(max_length=30)
    modelo = models.IntegerField()
    fecha_creacion = models.DateField(null=True)
    
    def __str__(self):
        return f'Marca: {self.nombre}'