from django.urls import path
from inicio import views

app_name= 'inicio'

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('atleta/crear/', views.crear_atleta, name='crear_atleta'),
    path('entrenador/crear/', views.crear_entrenador, name='crear_entrenador'),
    path('competencia/crear/', views.crear_competencia, name='crear_competencia'),
    path('atletas', views.listar_atletas, name='listar_atletas'),
    path('atletas/<int:pk>/', views.DetalleAtleta.as_view(), name='detalle_atleta'),
    path('atletas/<int:pk>/modificar', views.ModificarAtleta.as_view(), name='modificar_atleta'),
    path('atletas/<int:pk>/eliminar', views.EliminarAtleta.as_view(), name='eliminar_atleta'),
]
