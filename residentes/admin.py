from django.contrib import admin

from .models import Persona, Registro


@admin.register(Registro)
class RegistroAdmin(admin.ModelAdmin):
    list_display = ("numero",)
    search_fields = ("numero",)


@admin.register(Persona)
class PersonaAdmin(admin.ModelAdmin):
    list_display = ("nombre", "apellido", "rut", "tipo_persona", "registro", "activa")
    list_filter = ("tipo_persona", "activa")
    search_fields = ("nombre", "apellido", "rut")