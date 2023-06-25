from django.urls import path
from inicio import views

app_name= 'inicio'

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('atletas/crear/', views.crear_atleta, name='crear_atleta'),
    path('entrenadores/crear/', views.crear_entrenador, name='crear_entrenador'),
    path('competencias/crear/', views.crear_competencia, name='crear_competencia'),
]
