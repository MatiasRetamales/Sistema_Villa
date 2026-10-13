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