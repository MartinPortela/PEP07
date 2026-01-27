#from django.shortcuts import render
from django.views.generic import ListView
from .models import Publicacion

# Create your views here.

#def lista_publicaciones(request):
 #   publicaciones = Publicacion.objects.all()
  #  return render(request, "lista_publicaciones.html", {"publicaciones":
   # publicaciones})

class ListaPublicaciones(ListView): # nuevo​
    model = Publicacion
    template_name = "lista_publicaciones.html"