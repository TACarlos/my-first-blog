from django.shortcuts import render, redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.models import User
from django.views.generic import CreateView
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth import login,logout,authenticate
from apps.materia.models import userProfile


from apps.usuario.forms import RegistroForm,CompletRegisterForm

# Create your views here.
def RegistroUsuario (request):
	if request.user.is_authenticated():
		return HttpResponseRedirect('/')
	else: 
		form = RegistroForm()
		if request.method == "POST":
			form = RegistroForm(request.POST)
			if form.is_valid():
				usuario = form.cleaned_data['username']
				email = form.cleaned_data['email']
				password_one = form.cleaned_data['password_one']
				password_two = form.cleaned_data['password_two']
				u = User.objects.create_user(username=usuario,email=email,password=password_one)
				u.save()
				us  = authenticate(username=usuario,password=password_one)
				if us is not None and us.is_active:
					login(request,us)
					return HttpResponseRedirect('/usuario/completRegister/%s'%(us.id))
				else:
					return render(request, 'usuario/registrar.html',ctx)
			else:
				ctx = {'form':form}
				return render(request, 'usuario/registrar.html',ctx)
		ctx = {'form': form}     
		return render(request, 'usuario/registrar.html',ctx)

def CompletRegister(request,id_usa):
	user = User.objects.get(id=id_usa)
	if request.method == "POST":
		form = CompletRegisterForm(request.POST,request.FILES)
		if form.is_valid():
			add = form.save(commit=False)
			add.user_id = id_usa
			form.save()
			return HttpResponseRedirect('/usuario/%s'%(id_usa))
		else:
			form = CompletRegisterForm()
	else:
		form=CompletRegisterForm()
	ctx = {'form':form, 'user':user}
	return render(request, 'usuario/completRegister.html',ctx)

def Usuario (request,id_usa):
	if request.user.is_authenticated():
		usa = User.objects.get(id=id_usa)
		userP= userProfile.objects.filter(user_id=id_usa)
		ctx = {'usa': usa,'userp':userP,'idus':id_usa}
		return render(request, 'usuario/usuario.html',ctx)
	else:
		return HttpResponseRedirect('/')
