from django.db import models


class Registro(models.Model):
    numero = models.PositiveIntegerField(unique=True)

    def __str__(self):
        return f"Casa {self.numero}"


class Persona(models.Model):
    TIPOS_PERSONA = (
        ("SOCIO", "Socio"),
        ("REPRESENTANTE", "Representante"),
        ("ADICIONAL", "Adicional"),
    )

    registro = models.ForeignKey(Registro,on_delete=models.CASCADE,related_name="personas",)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    rut = models.CharField(max_length=12, null=True, blank=True)
    tipo_persona = models.CharField( max_length=20,choices=TIPOS_PERSONA,)
    activa = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"
    
