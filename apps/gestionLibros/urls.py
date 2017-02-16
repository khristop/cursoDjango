from django.conf.urls import url

from views import inicio, gestionLibro, LibroCreate, LibroUpdate, LibroDelete, crearLibro, GestionTemplate

urlpatterns = [
    url(r'^$', inicio, name='inicioApp'),
    url(r'^gestionar/$', GestionTemplate.as_view(), name='gestion'),

    url(r'^libro/$', gestionLibro.as_view(), name='libros-list'),
    url(r'libro/add/$', LibroCreate.as_view(), name='libro-agregar'),
    url(r'libro/(?P<pk>[0-9]+)/$', LibroUpdate.as_view(), name='libro-update'),
    url(r'libro/(?P<pk>[0-9]+)/delete/$', LibroDelete.as_view(), name='libro-delete'),

    url(r'formulario/$', crearLibro),
]