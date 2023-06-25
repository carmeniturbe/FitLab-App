from django.shortcuts import render
from inicio.forms import CrearAtletaFormulario, CrearEntrenadorFormulario, CrearCompetenciaFormulario
from inicio.models import Atleta, Entrenador, Competencia

# Create your views here.

def inicio(request):
    return render(request, 'inicio/inicio.html')

def crear_atleta(request):
    mensaje = ''
    
    if request.method == 'POST':
        formulario = CrearAtletaFormulario(request.POST)
        if formulario.is_valid():
            info = formulario.cleaned_data
            atleta = Atleta(nombre= info['nombre'],edad= info['edad'],deporte= info['deporte'],)
            atleta.save()
            mensaje = f'Se ha creado el atleta {atleta.nombre}' 
        else:
            return render(request, 'inicio/crear_atleta.html', {"formulario":formulario})
        
    formulario = CrearAtletaFormulario()
    return render(request, 'inicio/crear_atleta.html', {"formulario":formulario, 'mensaje': mensaje})
    
    
def crear_entrenador(request):

    mensaje = ''
    
    if request.method == 'POST':
        formulario = CrearEntrenadorFormulario(request.POST)
        if formulario.is_valid():
            info = formulario.cleaned_data
            entrenador = Entrenador(nombre= info['nombre'],edad= info['edad'],deporte= info['deporte'],)
            entrenador.save()
            mensaje = f'Se ha creado el entrenador {entrenador.nombre}' 
        else:
            return render(request, 'inicio/crear_entrenador.html', {"formulario":formulario})
        
    formulario = CrearEntrenadorFormulario()
    return render(request, 'inicio/crear_entrenador.html', {"formulario":formulario, 'mensaje': mensaje})
    

def crear_competencia(request):
    

    mensaje = ''
    
    if request.method == 'POST':
        formulario = CrearCompetenciaFormulario(request.POST)
        if formulario.is_valid():
            info = formulario.cleaned_data
            competencia = Competencia(nombre= info['nombre'],fecha= info['fecha'],)
            competencia.save()
            mensaje = f'Se ha creado la competencia {competencia.nombre}' 
        else:
            return render(request, 'inicio/crear_competencia.html', {"formulario":formulario})
        
    formulario = CrearCompetenciaFormulario()
    return render(request, 'inicio/crear_competencia.html', {"formulario":formulario, 'mensaje': mensaje})
    