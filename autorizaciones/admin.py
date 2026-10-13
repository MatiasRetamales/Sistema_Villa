from django.contrib import admin

from django.contrib import admin

from .models import (
    AutorizacionAdministrativa,
    AutorizacionTrabajo,
    PersonaAutorizadaTrabajo,
)


class PersonaAutorizadaTrabajoInline(admin.TabularInline):
    model = PersonaAutorizadaTrabajo
    extra = 1


@admin.register(AutorizacionTrabajo)
class AutorizacionTrabajoAdmin(admin.ModelAdmin):
    list_display = (
        "registro",
        "tipo_trabajo",
        "fecha_inicio",
        "fecha_termino",
        "estado",
    )
    list_filter = (
        "estado",
        "tipo_trabajo",
    )
    search_fields = (
        "registro__numero",
        "tipo_trabajo",
    )
    inlines = [PersonaAutorizadaTrabajoInline]


@admin.register(AutorizacionAdministrativa)
class AutorizacionAdministrativaAdmin(admin.ModelAdmin):
    list_display = (
        "nombre_persona",
        "tipo",
        "registro",
        "fecha_inicio",
        "fecha_termino",
        "activa",
    )
    list_filter = (
        "tipo",
        "activa",
    )
    search_fields = (
        "nombre_persona",
        "rut_persona",
        "registro__numero",
    )