from django.urls import path
from inicio import views

app_name= 'inicio'

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('atleta/crear/', views.crear_atleta, name='crear_atleta'),
    path('entrenador/crear/', views.crear_entrenador, name='crear_entrenador'),
    path('competencia/crear/', views.crear_competencia, name='crear_competencia'),
    path('atletas', views.listar_atletas, name='listar_atletas'),
]
