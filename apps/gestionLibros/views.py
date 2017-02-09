import json
from django.http import HttpResponse
from django.shortcuts import render, render_to_response, redirect
from django.core import serializers

# modelos
from .models import Libro, ReviewLibro, Genero

# Create your views here.
from django.views.generic import View


def inicio(request):

    if request.method == 'GET':
        listaObjetos = Libro.objects.all()
        return render_to_response('gestionLibros/index.html',
                                  {
                                      'titulo':'Libros+',
                                      'lista':listaObjetos,
                                      'listaCat': Genero.objects.all()
                                   })
    else:
        return redirect('/')

class gestionLibro(View):

    def get(self, request):
        listaObjetos = Libro.objects.all()
        print listaObjetos

        return HttpResponse(listaObjetos)