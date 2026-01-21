from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
def vista_pagina_inicio(request):
    context = { # nuevo​
        "lista_inventario": ["Memoria", "Discos Duros", "Placas Base"],
        "saludo": "GRACias por VISitarnos",
    }
    return render(request, "home.html", context)

class VistaAcercaDe(TemplateView): # nuevo​
    template_name = "about.html"

    def get_context_data(self, **kwargs):
    # nuevo​
        context = super().get_context_data(**kwargs)
        context["direccion"] = "Calle Blas Cabrera 90. Madrid, España"
        context["telefono"] = "678987898"
        return context