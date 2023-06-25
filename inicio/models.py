from django.db import models

# Create your models here.

class Atleta(models.Model):
    nombre = models.CharField(max_length=20)
    edad = models.IntegerField()
    deporte = models.CharField(max_length=30)
    
class Entrenador(models.Model):
    nombre = models.CharField(max_length=20)
    edad = models.IntegerField()
    deporte = models.CharField(max_length=30)
    
class Competencia(models.Model):
    nombre = models.CharField(max_length=20)
    fecha = models.DateField()