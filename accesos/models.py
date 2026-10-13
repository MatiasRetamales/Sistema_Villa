from django.db import models

from residentes.models import Persona, Registro


class Acceso(models.Model):
    TIPOS_ACCESO = (
        ("RESIDENTE", "Residente"),
        ("VISITA", "Visita"),
        ("TRABAJO", "Trabajo"),
        ("OTRO", "Otro"),
    )

    ESTADOS = (
        ("DENTRO", "Dentro"),
        ("FUERA", "Fuera"),
    )

    vivienda = models.ForeignKey(
        Registro,
        on_delete=models.CASCADE,
        related_name="accesos",
    )

    persona = models.ForeignKey(
        Persona,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="accesos",
    )

    patente = models.CharField(
        max_length=10,
        blank=True,
    )

    tipo_acceso = models.CharField(
        max_length=20,
        choices=TIPOS_ACCESO,
    )

    cantidad_acompanantes = models.PositiveIntegerField(default=0)

    fecha_hora_ingreso = models.DateTimeField(auto_now_add=True)

    estado = models.CharField(
        max_length=10,
        choices=ESTADOS,
        default="DENTRO",
    )

    nombre_ingreso = models.CharField(max_length=150)

    def __str__(self):
        return f"{self.nombre_ingreso} - Casa {self.vivienda.numero}"


class Movimiento(models.Model):
    TIPOS_MOVIMIENTO = (("SALIDA", "Salida"),)

    acceso = models.ForeignKey(
        Acceso,
        on_delete=models.CASCADE,
        related_name="movimientos",
    )

    tipo = models.CharField(
        max_length=10,
        choices=TIPOS_MOVIMIENTO,
    )

    fecha_hora = models.DateTimeField(auto_now_add=True)
    nombre_quien_retira = models.CharField(max_length=150, blank=True)

    def __str__(self):
        return f"{self.get_tipo_display()} - {self.acceso}"
