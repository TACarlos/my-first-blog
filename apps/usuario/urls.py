from django.conf.urls import url
from apps.usuario.views import RegistroUsuario,Usuario,CompletRegister

urlpatterns = [
	url(r'^registrar/', RegistroUsuario, name='registro'),
	url(r'^completRegister/(?P<id_usa>[0-9]+)/$',CompletRegister, name='completRegister'),
	url(r'^(?P<id_usa>[0-9]+)/$',Usuario, name='usuariosingle'),
]
