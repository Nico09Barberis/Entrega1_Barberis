from django.db import models
from ckeditor.fields import RichTextField


class Blog(models.Model):
    titulo = models.CharField(max_length=30)
    subtitulo = models.CharField(max_length=40)
    contenido = RichTextField(null=True)
    autor = models.CharField(max_length=30)
    fecha_creacion = models.DateField(null=True)
    
    def __str__(self):
        return f'Titulo: {self.titulo}'
     