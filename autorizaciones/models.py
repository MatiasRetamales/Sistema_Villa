from django.db import models
from residentes.models import Registro


class AutorizacionTrabajo(models.Model):
    ESTADOS = (
        ("ACTIVA", "Activa"),
        ("FINALIZADA", "Finalizada"),
        ("CANCELADA", "Cancelada"),
    )

    registro = models.ForeignKey(
        Registro,
        on_delete=models.CASCADE,
        related_name="autorizaciones_trabajo",
    )
    tipo_trabajo = models.CharField(max_length=150)
    fecha_inicio = models.DateField()
    fecha_termino = models.DateField(
        null=True,
        blank=True,
    )
    estado = models.CharField(
        max_length=15,
        choices=ESTADOS,
        default="ACTIVA",
    )
    observaciones = models.TextField(blank=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.tipo_trabajo} - Casa {self.registro.numero}"


class PersonaAutorizadaTrabajo(models.Model):
    autorizacion = models.ForeignKey(
        AutorizacionTrabajo,
        on_delete=models.CASCADE,
        related_name="personas_autorizadas",
    )
    nombre = models.CharField(max_length=150)
    rut = models.CharField(max_length=12, blank=True)

    def __str__(self):
        return f"{self.nombre} - {self.autorizacion}"


class AutorizacionAdministrativa(models.Model):
    registro = models.ForeignKey(
        Registro,
        on_delete=models.CASCADE,
        related_name="autorizaciones_administrativas",
        null=True,
        blank=True,
    )
    tipo = models.CharField(max_length=150)
    nombre_persona = models.CharField(max_length=150)
    rut_persona = models.CharField(max_length=12, blank=True)
    fecha_inicio = models.DateTimeField()
    fecha_termino = models.DateTimeField(
        null=True,
        blank=True,
    )
    observaciones = models.TextField(blank=True)
    activa = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.tipo} - {self.nombre_persona}"
