
from django.shortcuts import render
from .models import AutorizacionTrabajo


def permisos_trabajo(request):
    autorizaciones = (
        AutorizacionTrabajo.objects
        .select_related("registro")
        .prefetch_related("personas_autorizadas")
        .order_by("-fecha_creacion")
    )

    return render(
        request,
        "autorizaciones/permisos_trabajo.html",
        {
            "autorizaciones": autorizaciones,
        },
    )
