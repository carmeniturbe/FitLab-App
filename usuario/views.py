from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login as django_login
from usuario.forms import MiFormularioDeCreacionDeUsuarios, MiFormularioDeEdicionDeDatosDeUsuario
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

# Create your views here.

def login(request):
    
    if request.method  == 'POST':
        formulario = AuthenticationForm(request, data=request.POST)
        if formulario.is_valid():
            usuario = formulario.cleaned_data['username']
            contrasenia = formulario.cleaned_data['password']
            user = authenticate(username= usuario, password= contrasenia)
            django_login(request,user)
            return redirect('inicio:inicio')
        else:
            return render(request, 'usuario/login.html', {'formulario': formulario})
    
    formulario = AuthenticationForm()
    return render(request, 'usuario/login.html', {'formulario': formulario})

def registrarse(request):
    
    if request.method == 'POST':
        formulario = MiFormularioDeCreacionDeUsuarios(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('usuario:login')
        else: 
            return render(request, 'usuario/registro.html', {'formulario': formulario})
    
    formulario = MiFormularioDeCreacionDeUsuarios()
    return render(request, 'usuario/registro.html', {'formulario': formulario})

@login_required
def edicion_pefil(request):
    
    if request.method == 'POST':
        formulario = MiFormularioDeEdicionDeDatosDeUsuario(request.POST, instance =request.user)
        if formulario.is_valid():
            formulario.save()
            return redirect('inicio:inicio')
        else:
            return render(request, 'usuario/edicion_pefil.html', {'formulario': formulario})
        
    formulario = MiFormularioDeEdicionDeDatosDeUsuario(instance=request.user)
    return render(request, 'usuario/edicion_pefil.html', {'formulario': formulario})

class ModificarPass(LoginRequiredMixin, PasswordChangeView):
    template_name = 'usuario/modificar_pass.html'
    success_url = reverse_lazy('usuario:editar_pefil')