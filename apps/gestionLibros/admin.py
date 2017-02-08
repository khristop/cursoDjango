from django.contrib import admin

# Register your models here.
from models import Libro, Revista, Genero

admin.site.register(Libro)
admin.site.register(Revista)
admin.site.register(Genero)