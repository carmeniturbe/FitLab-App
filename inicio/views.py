from django.shortcuts import render
from inicio.forms import CrearAtletaFormulario, CrearEntrenadorFormulario, CrearCompetenciaFormulario,  BuscarAtletaFormulario
from inicio.models import Atleta, Entrenador, Competencia

from django.views.generic.edit import UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy

# Create your views here.

def inicio(request):
    return render(request, 'inicio/inicio.html')

def crear_atleta(request):
    # mensaje = ''
    
    if request.method == 'POST':
        formulario = CrearAtletaFormulario(request.POST)
        if formulario.is_valid():
            info = formulario.cleaned_data
            atleta = Atleta(nombre= info['nombre'],edad= info['edad'],deporte= info['deporte'],)
            atleta.save()
            return render(request, 'inicio/listar_atletas.html')
            # mensaje = f'Se ha creado el atleta {atleta.nombre}' 
        else:
            return render(request, 'inicio/crear_atleta.html', {"formulario":formulario})
        
    formulario = CrearAtletaFormulario()
    return render(request, 'inicio/crear_atleta.html', {"formulario":formulario})
  
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

def listar_atletas(request):
    formulario = BuscarAtletaFormulario(request.GET)
    # listado_de_atletas = None
    # nombre_a_buscar = None
    if formulario.is_valid():
        nombre_a_buscar = formulario.cleaned_data.get('nombre', '')
        listado_de_atletas = Atleta.objects.filter(nombre__icontains= nombre_a_buscar)

        
    formulario = BuscarAtletaFormulario()
    return render(request, 'inicio/listar_atletas.html', {"formulario":formulario, "atletas": listado_de_atletas, "nombre_a_buscar": nombre_a_buscar})

class DetalleAtleta(DetailView):
    model = Atleta
    template_name = "inicio/detalle_atleta.html"

class ModificarAtleta(UpdateView):
    model = Atleta
    fields = ['nombre', 'edad', 'deporte']
    template_name = "inicio/modificar_atleta.html"
    success_url = reverse_lazy('inicio:listar_atletas')

class EliminarAtleta(DeleteView):
    model = Atleta
    template_name = "inicio/eliminar_atleta.html"
    success_url = reverse_lazy('inicio:listar_atletas')


