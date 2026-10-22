from django.contrib import admin
from django.urls import path, include
from accesos import views

urlpatterns = [
    path("admin/", admin.site.urls),
    # Control de accesos
    path("ingresos/", views.ingresos, name="ingresos"),
    path(
        "ingresos/registrar/",
        views.registrar_ingreso,
        name="registrar_ingreso",
    ),
    path(
        "salidas/registrar/",
        views.registrar_salida,
        name="registrar_salida",
    ),
    # Permisos de trabajo
    path("autorizaciones/", include("autorizaciones.urls")),
]
