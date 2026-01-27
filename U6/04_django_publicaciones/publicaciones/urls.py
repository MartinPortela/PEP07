# publicaciones/urls.py​
from django.urls import path
from .views import ListaPublicaciones

urlpatterns = [
    path("", ListaPublicaciones.as_view(), name="home"),
]