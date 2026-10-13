from django.contrib import admin

from .models import Acceso, Movimiento


@admin.register(Acceso)
class AccesoAdmin(admin.ModelAdmin):
    list_display = (
        "nombre_ingreso",
        "vivienda",
        "tipo_acceso",
        "patente",
        "fecha_hora_ingreso",
        "estado",
    )
    list_filter = ("tipo_acceso", "estado")
    search_fields = (
        "nombre_ingreso",
        "rut_ingreso",
        "patente",
    )


@admin.register(Movimiento)
class MovimientoAdmin(admin.ModelAdmin):
    list_display = (
        "acceso",
        "tipo",
        "fecha_hora",
    )
    list_filter = ("tipo",)
    search_fields = (
        "acceso__nombre_ingreso",
        "acceso__patente",
    )