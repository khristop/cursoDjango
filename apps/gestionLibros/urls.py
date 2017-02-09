from django.conf.urls import url

from views import inicio, gestionLibro

urlpatterns = [
    url(r'^$', inicio, name='inicioApp'),
    url(r'^libro/', gestionLibro.as_view(), name='listaDeLibros')
]
