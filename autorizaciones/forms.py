
from django import forms
from residentes.models import Registro
from .models import AutorizacionTrabajo, PersonaAutorizadaTrabajo


class AutorizacionTrabajoForm(forms.ModelForm):
    class Meta:
        model = AutorizacionTrabajo
        fields = [
            "registro",
            "tipo_trabajo",
            "fecha_inicio",
            "fecha_termino",
            "observaciones",
        ]

        labels = {
            "registro": "Casa",
            "tipo_trabajo": "Tipo de trabajo",
            "fecha_inicio": "Fecha de inicio",
            "fecha_termino": "Fecha de término",
            "observaciones": "Observaciones",
        }

        widgets = {
            "fecha_inicio": forms.DateInput(
                attrs={"type": "date"},
                format="%Y-%m-%d",
            ),
            "fecha_termino": forms.DateInput(
                attrs={"type": "date"},
                format="%Y-%m-%d",
            ),
            "observaciones": forms.Textarea(
                attrs={
                    "rows": 3,
                    "placeholder": "Observaciones adicionales...",
                }
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["registro"].queryset = Registro.objects.order_by(
            "numero"
        )

        self.fields["fecha_termino"].required = False


class PersonaAutorizadaTrabajoForm(forms.ModelForm):
    class Meta:
        model = PersonaAutorizadaTrabajo
        fields = ["nombre", "rut"]

        labels = {
            "nombre": "Nombre completo",
            "rut": "RUT",
        }

        widgets = {
            "nombre": forms.TextInput(
                attrs={"placeholder": "Nombre y apellidos"}
            ),
            "rut": forms.TextInput(
                attrs={"placeholder": "12.345.678-9"}
            ),
        }
