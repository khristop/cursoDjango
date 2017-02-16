from __future__ import unicode_literals

from django.db import models


# Create your models here.
from ..gestionLibros.models import Libro


class Compra(models.Model):

    cantidad = models.IntegerField(blank=False)
    articulo = models.ForeignKey(Libro)
    total = models.FloatField(blank=False)



