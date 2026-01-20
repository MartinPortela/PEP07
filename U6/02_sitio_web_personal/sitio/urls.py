# paginas/urls.py​
from django.urls import path

from .views import vista_pagina_inicio, vista_acercade

urlpatterns = [
    path("about/", vista_acercade),
    path("", vista_pagina_inicio),
]