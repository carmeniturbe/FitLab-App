from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class Atleta(models.Model):
    nombre = models.CharField(max_length=20)
    edad = models.IntegerField()
    deporte = models.CharField(max_length=30)
    descripcion = RichTextField(null=True)
    
    def __str__(self):
        return f'Nombre: {self.nombre} - Edad: {self.edad}'
    
class Entrenador(models.Model):
    nombre = models.CharField(max_length=20)
    edad = models.IntegerField()
    deporte = models.CharField(max_length=30)
    
class Competencia(models.Model):
    nombre = models.CharField(max_length=20)
    fecha = models.DateField()