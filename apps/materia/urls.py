from django.conf.urls import url
from django.contrib import admin
from apps.materia.views import index, grado_view, about_view, contacto_view, login_view, Logout_view,singleGradoNivel,singleGrado,singleMateria,singleTema

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^nivel/$', grado_view, name='nivel'),
    url(r'^nivel/(?P<id_niv>[0-9]+)/$', singleGradoNivel, name='singleNivel'),
    url(r'^nivel/(?P<id_niv>[0-9]+)/(?P<id_grado>[0-9]+)/$', singleGrado, name='singleGrado'),
    url(r'^nivel/(?P<id_niv>[0-9]+)/(?P<id_grado>[0-9]+)/(?P<id_mat>[0-9]+)/$', singleMateria, name='singleMateria'),
    url(r'^nivel/(?P<id_niv>[0-9]+)/(?P<id_grado>[0-9]+)/(?P<id_mat>[0-9]+)/(?P<id_tema>[0-9]+)/$', singleTema, name='singleTema'),
    url(r'^about/$', about_view, name='about'),
    url(r'^contacto/$', contacto_view, name='contacto'),
    url(r'^login/$', login_view, name='login'),
    url(r'^logout/$', Logout_view, name='logout'),

]
