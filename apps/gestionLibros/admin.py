from django.contrib import admin

# Register your models here.
from models import Libro, Revista, Genero, ReviewLibro

admin.site.register(Libro)
admin.site.register(Revista)
admin.site.register(Genero)
admin.site.register(ReviewLibro)