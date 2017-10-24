from django import forms
from apps.materia.models import Grado,GradoNivel, Materia,Temas,ContentTema

class ContactForm(forms.Form):
    Email = forms.EmailField(widget=forms.TextInput())
    Titulo = forms.CharField(widget=forms.TextInput())
    Texto = forms.CharField(widget=forms.Textarea())

class AddNivelForm(forms.ModelForm):

	class Meta:
		model = Grado

		fields = [
			'nombre',
			'Descripcion',
			'status',
		]
		labels = {
			'nombre': 'Escribe el nombre del nivel',
			'Descripcion': 'Escribe una descripcion del nivel',
			'status': '¿Esta activo el nivel?',			
		}
		widgets = {
			'nombre' : forms.TextInput(attrs={'class':'form-control'}),
			'Descripcion' : forms.Textarea(attrs={'class':'form-control'}),
			'status' : forms.NullBooleanSelect(attrs={'class':'form-control'}),			
		}
	  
class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','style':'color:black;'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','style':'color:black;'},render_value=False))


class AddGrado(forms.ModelForm):

	class Meta:
		model = GradoNivel

		fields = [
			'grado',
			'nombre',
			'Descripcion',
			'status',
		]

		exclude = {'grado'}

		labels = {
			'nombre': 'Escribe el nombre del Grado',
			'Descripcion': 'Escribe una descripcion del grado',
			'status': '¿Esta activo el grado?',			
		}

		widgets = {
			'nombre' : forms.TextInput(attrs={'class':'form-control'}),
			'Descripcion' : forms.Textarea(attrs={'class':'form-control'}),
			'status' : forms.NullBooleanSelect(attrs={'class':'form-control'}),			
		}


class AddMateria(forms.ModelForm):

	class Meta:
		model = Materia

		fields = [
			'grado',
			'nombre',
			'Descripcion',
			'status',
			'photo',
		]

		exclude = {'grado'}

		labels = {
			'nombre': 'Escribe el nombre de la Materia',
			'Descripcion': 'Escribe una descripcion de la materia',
			'status': '¿Esta activa la materia?',
			'photo':'Agregar una imagen'			
		}

		widgets = {
			'nombre' : forms.TextInput(attrs={'class':'form-control'}),
			'Descripcion' : forms.Textarea(attrs={'class':'form-control'}),
			'status' : forms.NullBooleanSelect(attrs={'class':'form-control'}),			
		}

class AddTemas(forms.ModelForm):

	class Meta:
		model = Temas

		fields = [
			'materia',
			'nombre',
			'Descripcion',
			'status',
			'photo',
		]

		exclude = {'materia'}

		labels = {
			'nombre': 'Escribe el nombre de el tema',
			'Descripcion': 'Escribe una descripcion de el tema ',
			'status': '¿Esta activa el tema?',
			'photo':'elige una imagen',		
		}

		widgets = {
			'nombre' : forms.TextInput(attrs={'class':'form-control'}),
			'Descripcion' : forms.Textarea(attrs={'class':'form-control'}),
			'status' : forms.NullBooleanSelect(attrs={'class':'form-control'}),			
		}

class AddContentTema(forms.ModelForm):

	class Meta:
		model = ContentTema

		fields = [
			'tema',
			'Descripcion',
			'status',
			'photo',
			'video',
		]

		exclude = {'tema'}

		labels = {
			'Contenido': 'Escribe el contenido del tema',
			'status': '¿Es visible el Contenido?',
			'photo':'elige una imagen',
			'video':'pega la url de un video',		
		}

		widgets = {
			'nombre' : forms.TextInput(attrs={'class':'form-control'}),
			'Descripcion' : forms.Textarea(attrs={'class':'form-control'}),
			'status' : forms.NullBooleanSelect(attrs={'class':'form-control'}),			
		}
