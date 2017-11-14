from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserGrupo(models.Model):
    def url(self,filename):
        ruta = "static/MultimediaData/Grupos/%s/%s/%s"%(self.maestro.username,self.nombre,str(filename))
        return ruta
    maestro = models.ForeignKey(User,null=True,)
    nombre = models.CharField(max_length=50)
    Descripcion = models.TextField(max_length=200)
    status = models.BooleanField(default = True)
    photo = models.ImageField(upload_to=url,null=True)

    def __str__(self):
        return self.nombre