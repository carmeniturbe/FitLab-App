from django import forms

class CrearAtletaFormulario(forms.Form):
    nombre = forms.CharField(max_length=20)
    edad = forms.IntegerField()
    deporte = forms.CharField(max_length=20)
    
class CrearEntrenadorFormulario(forms.Form):
    nombre = forms.CharField(max_length=20)
    edad = forms.IntegerField()
    deporte = forms.CharField(max_length=20)
    
class CrearCompetenciaFormulario(forms.Form):
    nombre = forms.CharField(max_length=20)
    fecha = forms.DateField()


