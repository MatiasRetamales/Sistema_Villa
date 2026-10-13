from django.shortcuts import render, redirect

from accesos.forms import AccesoForm, SalidaForm
from .models import Acceso

from django.shortcuts import render, redirect

from accesos.forms import AccesoForm, SalidaForm
from .models import Acceso


def ingresos(request):

    accesos = Acceso.objects.filter(estado="DENTRO").order_by("-fecha_hora_ingreso")

    form = AccesoForm()
    salida_form = SalidaForm()

    return render(
        request,
        "accesos/ingresos.html",
        {
            "accesos": accesos,
            "form": form,
            "salida_form": salida_form,
        },
    )


def registrar_ingreso(request):

    if request.method == "POST":
        form = AccesoForm(request.POST)

        if form.is_valid():
            form.save()

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
