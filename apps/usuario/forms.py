from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from apps.materia.models import userProfile


class RegistroForm(forms.Form):
	username = forms.CharField(label= "Nombre de Usuario", widget=forms.TextInput(attrs={'class':'form-control','style':'color:black;'}))
	email = forms.EmailField(label= "Correo electronico", widget=forms.TextInput(attrs={'class':'form-control','style':'color:black;'}))
	password_one = forms.CharField(label= "Contraseña", widget=forms.PasswordInput(render_value=False,attrs={'class':'form-control','style':'color:black;'}))
	password_two = forms.CharField(label= "Confirmar contraseña", widget=forms.PasswordInput(render_value=False,attrs={'class':'form-control','style':'color:black;'}))
	
	def clean_username(self):
		username = self.cleaned_data['username']
		try:
			u = User.objects.get(username=username)
		except User.DoesNotExist:
			return username
		raise forms.ValidationError('El Usuario ya existe')

	def clean_email(self):
		email = self.cleaned_data['email']
		try:
			u = User.objects.get(email=email)
		except User.DoesNotExist:
			return email
		raise forms.ValidationError('El correo ya existe')

	def clean_password_two(self):
		password_one =self.cleaned_data['password_one']
		password_two =self.cleaned_data['password_two']
		if password_one == password_two:
			pass
		else:
			raise forms.ValidationError('Las contraseñas no coinciden')

class CompletRegisterForm(forms.ModelForm):

	class Meta:
		model = userProfile

		fields = [
			'user',
			'photo',
			'telefono',
			'Tipo',
		]

		exclude = {'user'}

		labels = {
			'photo': 'Elige una foto de perfil',
			'telefono': 'Escribe tu telefono ',
			'Tipo': 'Eres alumno o profesror',	
		}

		widgets = {
			'telefono' : forms.TextInput(attrs={'class':'form-control'}),			
		}