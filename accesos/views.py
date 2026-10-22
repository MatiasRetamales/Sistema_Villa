
from django.shortcuts import render, redirect

from accesos.forms import AccesoForm, SalidaForm
from .models import Acceso
from autorizaciones.models import AutorizacionTrabajo
from autorizaciones.models import AutorizacionAdministrativa
from .models import Acceso, AcompananteAcceso



def ingresos(request):
    accesos = (
        Acceso.objects
        .filter(estado="DENTRO")
        .select_related("vivienda")
        .prefetch_related("vivienda__personas", "acompanantes")
        .order_by("-fecha_hora_ingreso")
    )

    autorizaciones = (
        AutorizacionTrabajo.objects
        .select_related("registro")
        .prefetch_related("personas_autorizadas")
        .order_by("-fecha_creacion")
    )

    permisos_administrativos = (
        AutorizacionAdministrativa.objects
        .select_related("registro")
        .order_by("-fecha_creacion")
    )

    form = AccesoForm()
    salida_form = SalidaForm()

    return render(
        request,
        "accesos/ingresos.html",
        {
            "accesos": accesos,
            "form": form,
            "salida_form": salida_form,
            "autorizaciones": autorizaciones,
            "permisos_administrativos": permisos_administrativos,
        },
    )



def registrar_ingreso(request):
    if request.method == "POST":
        form = AccesoForm(request.POST)

        if form.is_valid():
            acceso = form.save()

            cantidad = acceso.cantidad_acompanantes

            for numero in range(1, cantidad + 1):
                AcompananteAcceso.objects.create(
                    acceso=acceso,
                    nombre=form.cleaned_data[
                        f"acompanante_nombre_{numero}"
                    ].strip(),
                    rut=form.cleaned_data[
                        f"acompanante_rut_{numero}"
                    ].strip(),
                )

    return redirect("ingresos")


def registrar_salida(request):
    if request.method == "POST":
        acceso_id = request.POST.get("acceso_id")

        acceso = Acceso.objects.get(id=acceso_id)

        salida_form = SalidaForm(request.POST)

        if salida_form.is_valid():
            movimiento = salida_form.save(commit=False)
            movimiento.acceso = acceso
            movimiento.tipo = "SALIDA"
            movimiento.save()

            acceso.estado = "FUERA"
            acceso.save()

    return redirect("ingresos")
