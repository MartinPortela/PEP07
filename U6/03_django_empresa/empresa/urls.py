# empresa/urls.py​
from django.urls import path
from .views import vista_pagina_inicio, VistaAcercaDe

urlpatterns = [
    path("about/", VistaAcercaDe.as_view(), name="about"),
    path("",vista_pagina_inicio, name="inicio"),
]