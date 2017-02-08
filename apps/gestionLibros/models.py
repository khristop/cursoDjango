from __future__ import unicode_literals

from django.db import models

# Create your models here.


class ArticuloAbstract(models.Model):

    titulo= models.CharField(max_length=50, blank=False)
    descripcion = models.CharField(max_length=200, blank=True)
    fechaIngreso = models.DateField(auto_now_add=True)
    ultimaFechaIngreso = models.DateField(auto_now=True)
    cantidad = models.IntegerField(default=0)
    precio = models.DecimalField(decimal_places=2, max_digits=6, default=0.00)

    def __str__(self):
        return self.titulo

    class Meta:
        abstract = True


class Genero(models.Model):

    nombre = models.CharField(max_length=25, blank=False, unique=True)
    descripcion = models.CharField(max_length=150, blank=True)
    categSimilares = models.ManyToManyField("self")

    def __str__(self):
        return self.nombre


class Libro(ArticuloAbstract):

    autor= models.CharField(max_length=50, blank=False, default='Anonimo')
    edicion= models.IntegerField(blank=False, default=1)
    pubDate = models.DateField(blank=False)
    genero = models.ForeignKey(Genero)


class Revista(ArticuloAbstract):

    genero = models.ForeignKey(Genero)
    editor = models.CharField(max_length=50, blank=False)
    fecha = models.DateField()
