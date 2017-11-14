from django.shortcuts import render, redirect, render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.models import User
from django.views.generic import CreateView
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth import login,logout,authenticate
from apps.materia.models import userProfile,Materia,Grado
from apps.usuario.models import UserGrupo


from apps.usuario.forms import RegistroForm,CompletRegisterForm,CreateGroupForm

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
		userP= userProfile.objects.get(user_id=id_usa)
		mst = "2"
		mygrupo = UserGrupo.objects.filter(maestro_id=id_usa) 
		if request.method == "POST":
			form = CreateGroupForm(request.POST,request.FILES)
			if form.is_valid():
				add = form.save(commit=False)
				add.maestro_id = id_usa
				form.save()
				return HttpResponseRedirect('/usuario/%s'%(id_usa))
			else:
				form = CreateGroupForm()
		else:
			form=CreateGroupForm()
		if Materia.objects.filter(usuarios=id_usa):
			mensaje = 'true'
			mat = Materia.objects.filter(usuarios=id_usa)
			msj2 = userP.Tipo
			ctx = {'usa': usa,'userp':userP,'idus':id_usa,'mat':mat,'msj':mensaje,'msj2':msj2,'mst':mst,'form':form,'myg':mygrupo}
		else:
			msj2 = userP.Tipo
			mensaje = 'false'
			ctx = {'usa': usa,'userp':userP,'idus':id_usa,'msj':mensaje,'form':form,'myg':mygrupo,'msj2':msj2}


		return render(request, 'usuario/usuario.html',ctx)
	else:
		return HttpResponseRedirect('/')

def singleGrupo(request,id_mst,id_grupo):
    if request.user.is_authenticated():
        grupo = UserGrupo.objects.get(id=id_grupo)     
        ctx = {'grupo':grupo}
        return render(request, 'usuario/grupo.html', ctx)
    else:
        return HttpResponseRedirect('/login')

def search(request):
	if request.method == "POST":
		search_text = request.POST['search_text']
	else:
		search_text = ""
	if search_text:
		grupos = UserGrupo.objects.filter(nombre__contains=search_text)
	else:
		grupos = ""
	ctx = {'grupos':grupos}
	print()
	return render_to_response('usuario/ajax_search.html',ctx)

