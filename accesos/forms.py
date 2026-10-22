
from django import forms

from .models import Acceso, Movimiento


class AccesoForm(forms.ModelForm):

    class Meta:
        model = Acceso
        fields = (
            "vivienda",
            "nombre_ingreso",
            "tipo_acceso",
            "patente",
            "cantidad_acompanantes",
        )
        widgets = {
            "vivienda": forms.Select(
                attrs={
                    "class": "buscador-viviendas",
                    "data-placeholder": "Busca el número de casa...",
                }
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["vivienda"].queryset = (
            self.fields["vivienda"].queryset.order_by("numero")
        )

        # Limitar la cantidad de acompañantes por ingreso.
        self.fields["cantidad_acompanantes"].max_value = 20

        # Al recibir el formulario, crear los campos que corresponden
        # a la cantidad de acompañantes indicada.
        if self.is_bound:
            try:
                cantidad = int(
                    self.data.get("cantidad_acompanantes", 0)
                )
            except (TypeError, ValueError):
                cantidad = 0

            if 0 <= cantidad <= 20:
                for numero in range(1, cantidad + 1):
                    self.fields[f"acompanante_nombre_{numero}"] = (
                        forms.CharField(
                            label=f"Nombre completo del acompañante {numero}",
                            max_length=150,
                            required=True,
                        )
                    )
                    self.fields[f"acompanante_rut_{numero}"] = (
                        forms.CharField(
                            label=f"RUT del acompañante {numero}",
                            max_length=12,
                            required=True,
                        )
                    )


class SalidaForm(forms.ModelForm):

    nombre_quien_retira = forms.CharField(
        label="Nombre de quien registra la salida",
        max_length=150,
        required=True,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Ingrese el nombre",
            }
        ),
    )

    class Meta:
        model = Movimiento
        fields = (
            "nombre_quien_retira",
        )
