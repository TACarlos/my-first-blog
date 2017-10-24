from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Grado(models.Model):
    nombre = models.CharField(max_length=50)
    Descripcion = models.TextField(max_length=50)
    status = models.BooleanField(default = True)

    def __str__(self):
        return self.nombre

class TipoUsuario(models.Model):
    tipo = models.CharField(max_length=50)
    def __str__(self):
        return self.tipo  

class userProfile(models.Model):

    def url(self,filename):
        ruta = "static/MultimediaData/Users/%s/%s"%(self.user.username,filename)
        return ruta

    user = models.OneToOneField(User)
    photo = models.ImageField(upload_to=url)
    telefono = models.CharField(max_length=10,null=True)
    Tipo = models.ForeignKey(TipoUsuario, null=True,)
    
    def __str__(self):
        return self.user.username

class GradoNivel(models.Model):
    grado = models.ForeignKey(Grado)
    nombre = models.CharField(max_length=50)
    Descripcion = models.TextField(max_length=50)
    status = models.BooleanField(default = True)
    def __str__(self):
        return self.nombre

class Materia(models.Model):
    def url(self,filename):
        ruta = "static/MultimediaData/Materias/%s/%s/%s"%(self.grado.nombre,self.nombre,str(filename))
        return ruta
    grado = models.ForeignKey(GradoNivel,null=True,)
    nombre = models.CharField(max_length=50)
    Descripcion = models.TextField(max_length=200)
    status = models.BooleanField(default = True)
    photo = models.ImageField(upload_to=url,null=True)

    def __str__(self):
        return self.nombre

class Temas(models.Model):
    def url(self,filename):
        ruta = "static/MultimediaData/Materias/%s/%s/%s"%(self.materia.nombre,self.nombre,str(filename))
        return ruta
    materia = models.ForeignKey(Materia,null=True,)
    nombre = models.CharField(max_length=50)
    Descripcion = models.TextField(max_length=200)
    status = models.BooleanField(default = True)
    photo = models.ImageField(upload_to=url,null=True)


    def __str__(self):
        return self.nombre

class ContentTema(models.Model):
    def url(self,filename):
        ruta = "static/MultimediaData/Materias/%s/%s"%(self.tema.nombre,str(filename))
        return ruta
    tema = models.OneToOneField(Temas,null=True)
    Descripcion = models.TextField(max_length=200)
    status = models.BooleanField(default = True)
    photo = models.ImageField(upload_to=url,null=True)
    video = models.URLField()
    def __str__(self):
        return self.tema.nombre