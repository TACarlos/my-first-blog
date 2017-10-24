from django.contrib import admin
from apps.materia.models import Materia, Grado, userProfile, TipoUsuario, GradoNivel,Temas,ContentTema

# Register your models here.
admin.site.register(Materia)
admin.site.register(Grado)
admin.site.register(userProfile)
admin.site.register(TipoUsuario)
admin.site.register(GradoNivel)
admin.site.register(Temas)
admin.site.register(ContentTema)
