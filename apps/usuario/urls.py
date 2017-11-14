from django.conf.urls import url
from apps.usuario.views import RegistroUsuario,Usuario,CompletRegister,singleGrupo,search

urlpatterns = [
	url(r'^registrar/', RegistroUsuario, name='registro'),
	url(r'^completRegister/(?P<id_usa>[0-9]+)/$',CompletRegister, name='completRegister'),
	url(r'^(?P<id_usa>[0-9]+)/$',Usuario, name='usuariosingle'),
	url(r'^grupos/(?P<id_mst>[0-9]+)/(?P<id_grupo>[0-9]+)/$',singleGrupo, name='singleGrupo'),
	url(r'^search/$',search, name='search'),

]
