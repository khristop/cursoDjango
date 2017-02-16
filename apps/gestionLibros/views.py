import json

from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponse
from django.shortcuts import render, render_to_response, redirect
from django.core import serializers

# modelos
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .forms import LibroForm
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

class GestionTemplate(View):

    def get(self, request):
        return render_to_response('gestionLibros/gestion.html', {'lista':Libro.objects.all()})


def crearLibro(request):

    if request.method=='get' :
        formulario = LibroForm
        return render_to_response('gestionLibros/libro_form.html',{'form':formulario})

    elif request.method=='post':

        precio =request.body.precio;

        return HttpResponse(precio)

class LibroCreate(CreateView):
    model = Libro
    form_class = LibroForm
    success_url = reverse_lazy('inicioApp')



class LibroUpdate(UpdateView):
    model = Libro
    form_class = LibroForm
    success_url = reverse_lazy('inicioApp')



class LibroDelete(DeleteView):
    model = Libro
    success_url = reverse_lazy('inicioApp')


class gestionLibro(View):

    def get(self, request):
        listaObjetos = serializers.serialize('json',Libro.objects.all())
        return HttpResponse(listaObjetos)