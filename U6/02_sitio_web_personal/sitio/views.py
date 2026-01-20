from django.shortcuts import render
from django.http import HttpResponse


def vista_pagina_inicio(request):
    return HttpResponse("Soy Martín wachin")
def vista_acercade(request): # new​
    return render(request, "sitio/templates/about.html")
# Create your views here.
