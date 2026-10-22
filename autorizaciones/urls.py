
from django.urls import path
from . import views

urlpatterns = [
    path(
        "permisos-trabajo/",
        views.permisos_trabajo,
        name="permisos_trabajo",
    ),
]
