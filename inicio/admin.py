from django.contrib import admin
from .models import Atleta, Entrenador, Competencia

class AtletaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'edad', 'deporte', 'fecha_nacimiento', 'imagen')
    search_fields = ('nombre', 'deporte', 'fecha_nacimiento')

class EntrenadorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'edad', 'deporte')
    search_fields = ('nombre', 'deporte')

class CompetenciaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'fecha')
    search_fields = ('nombre', 'fecha')

admin.site.register(Atleta, AtletaAdmin)
admin.site.register(Entrenador, EntrenadorAdmin)
admin.site.register(Competencia, CompetenciaAdmin)
