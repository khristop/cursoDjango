from django.http import HttpResponse
from django.shortcuts import render, render_to_response


# Create your views here.

def inicio(request):

    return render(request,'gestionLibros/index.html', {'titulo':'estion de Bibliotecas'})