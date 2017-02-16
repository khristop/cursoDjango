from django.conf.urls import url

from views import inicio, gestionLibro, LibroCreate, LibroUpdate, LibroDelete, crearLibro, GestionTemplate, verLibro

urlpatterns = [
    url(r'^$', inicio, name='inicioApp'),
    url(r'^gestionar/$', GestionTemplate.as_view(), name='gestion'),

    url(r'^libro/(?P<id_libro>[0-9]+)/$', verLibro, name='verlibro'),

    url(r'^gestionar/libro/$', gestionLibro.as_view(), name='libros-list'),
    url(r'gestionar/libro/add/$', LibroCreate.as_view(), name='libro-agregar'),
    url(r'gestionar/libro/(?P<pk>[0-9]+)/$', LibroUpdate.as_view(), name='libro-update'),
    url(r'gestionar/libro/(?P<pk>[0-9]+)/delete/$', LibroDelete.as_view(), name='libro-delete'),

    url(r'formulario/$', crearLibro),
]