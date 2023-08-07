from typing import Any, Dict
from django.db.models.query import QuerySet
from django.shortcuts import render
from inicio.forms import CrearAtletaFormulario, CrearEntrenadorFormulario, CrearCompetenciaFormulario,  BuscarAtletaFormulario
from inicio.models import Atleta, Entrenador, Competencia

from django.views.generic.edit import UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView

# Create your views here.

def inicio(request):
    return render(request, 'inicio/inicio.html')

@login_required
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

@login_required
def listar_atletas(request):
    formulario = BuscarAtletaFormulario(request.GET)
    # listado_de_atletas = None
    # nombre_a_buscar = None
    if formulario.is_valid():
        nombre_a_buscar = formulario.cleaned_data.get('nombre', '')
        listado_de_atletas = Atleta.objects.filter(nombre__icontains= nombre_a_buscar)

        
    formulario = BuscarAtletaFormulario()
    return render(request, 'inicio/listar_atletas.html', {"formulario":formulario, "atletas": listado_de_atletas, "nombre_a_buscar": nombre_a_buscar})

class DetalleAtleta(LoginRequiredMixin, DetailView):
    model = Atleta
    template_name = "inicio/detalle_atleta.html"

class ModificarAtleta(LoginRequiredMixin, UpdateView):
    model = Atleta
    fields = ['nombre', 'edad', 'deporte', 'descripcion', 'imagen', 'fecha_nacimiento',]
    template_name = "inicio/modificar_atleta.html"
    success_url = reverse_lazy('inicio:listar_atletas')

class EliminarAtleta(LoginRequiredMixin, DeleteView):
    model = Atleta
    template_name = "inicio/eliminar_atleta.html"
    success_url = reverse_lazy('inicio:listar_atletas')
    
def about_us(request):
    return render(request, 'inicio/about_us.html')

class CrearAtleta(CreateView):
    model = Atleta
    template_name = 'inicio/CBV/crear_atleta_CBV.html'
    fields = ['nombre', 'edad', 'deporte', 'descripcion', 'imagen', 'fecha_nacimiento',]
    success_url = reverse_lazy('inicio:listar_atletas')
    

class ListarAtletas(ListView):
    model = Atleta
    template_name = 'inicio/CBV/listar_atletas_CBV.html'
    context_object_name = 'atletas'
    
    def get_queryset(self):
        listado_de_atletas = []
        formulario = BuscarAtletaFormulario(self.request.GET)
        if formulario.is_valid():
            nombre_a_buscar = formulario.cleaned_data.get('nombre')
            listado_de_atletas = Atleta.objects.filter(nombre__icontains= nombre_a_buscar)
        return listado_de_atletas
    
    def get_context_data(self, **kwargs):
        contexto = super().get_context_data(**kwargs)
        contexto['formulario'] = BuscarAtletaFormulario()
        return contexto
    


