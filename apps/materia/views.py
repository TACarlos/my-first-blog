from django.shortcuts import render, redirect
from django.http import HttpResponse,HttpResponseRedirect
from apps.materia.models import Materia, Grado, GradoNivel,Temas, ContentTema,temaProblema,proresuletos
from apps.materia.forms import ContactForm, AddNivelForm, LoginForm, AddGrado,AddMateria,AddTemas,AddContentTema,ProblemaForm,proresultForm
from django.core.mail import EmailMultiAlternatives
from django.contrib.auth import login,logout,authenticate
import simplejson,random
# Create your views here.
def index (request):
    return render(request, 'materias/index.html')

def grado_view (request):
    if request.user.is_authenticated():
        grado = Grado.objects.filter(status= True)
        if request.method == "POST":
            form = AddNivelForm(request.POST)
            if form.is_valid():
                form.save()
            return redirect('materia:nivel')
        else:
            form = AddNivelForm()     
        contexto = {'grados':grado,'form':form}
        return render(request, 'materias/nivel.html', contexto)
    else:
        return HttpResponseRedirect('/login')
def about_view (request):
    mensaje = "esto es un mensaje desde la vista"
    ctx = {'msg': mensaje}
    return render(request, 'materias/about.html', ctx)

def contacto_view (request):
    info_enviado = False
    email = ""
    titulo = ""
    texto = ""
    if request.method == "POST":
        formulario = ContactForm(request.POST)
        if formulario.is_valid():
            info_enviado = True
            email = formulario.cleaned_data['Email']
            titulo = formulario.cleaned_data['Titulo']
            texto = formulario.cleaned_data['Texto']
            to_admin = 'scaj8288@gmail.com'
            html_content = "[%s] <br><br><p>Mensaje:%s"%(email,texto)
            msg = EmailMultiAlternatives('Correo',html_content,'from@server.com',[to_admin])
            msg.attach_alternative(html_content,'text/html')
            msg.send()
    else:            
        formulario = ContactForm()
    ctx = {'form':formulario,'email':email,'titulo':titulo,'texto':texto,'info_enviado':info_enviado}
    return render(request, 'materias/contacto.html', ctx)

def login_view(request):
    mensaje = ''
    if request.user.is_authenticated():
        return HttpResponseRedirect('/')
    else:
        if request.method == "POST":
            form = LoginForm(request.POST)
            if form.is_valid():
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                usuario  = authenticate(username=username,password=password)
                if usuario is not None and usuario.is_active:
                    login(request,usuario)
                    return HttpResponseRedirect('/usuario/%s'%(usuario.id))
                else:
                    mensaje = 'Usuario y/o Password es incorrecto'
        form = LoginForm()
        ctx = {'form':form,'mensaje':mensaje}
        return render(request, 'materias/login.html', ctx)

def Logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')

def singleGradoNivel(request,id_niv):
    if request.user.is_authenticated():
        niv = Grado.objects.get(id=id_niv)
        grado = GradoNivel.objects.filter(grado_id=niv.id)
        if request.method == "POST":
            form = AddGrado(request.POST)
            if form.is_valid():
                add = form.save(commit=False)
                add.grado_id = id_niv
                form.save()
                return HttpResponseRedirect('/nivel/%s'%(id_niv))
        else:
            form = AddGrado()     
        ctx = {'niv':niv,'grado':grado,'form':form}
        return render(request, 'materias/singlegradonivel.html', ctx)
    else:
        return HttpResponseRedirect('/login')

def singleGrado(request,id_niv,id_grado):
    if request.user.is_authenticated():
        niv = Grado.objects.get(id=id_niv)
        grados = GradoNivel.objects.get(id=id_grado)
        materia = Materia.objects.filter(grado_id=id_grado)
        form = AddMateria()
        if request.method == "POST":
            if "mat_id" in request.POST:
                try:
                    id_producto = request.POST['mat_id']
                    p = Materia.objects.get(pk=id_producto)
                    mensaje = {"status":"True","product_id":p.id}
                    p.delete()
                    return HttpResponseRedirect('/nivel/%s/%s'%(id_niv,id_grado))
                except:
                    mensae = {"status":"False"}
                    return HttpResponseRedirect('/nivel/%s/%s'%(id_niv,id_grado))
            if "user.id" in request.POST:
                us = request.POST['user.id']
                m = request.POST['m.id']
                if Materia.objects.filter(pk=m,usuarios=us):
                    return HttpResponseRedirect('/nivel/%s/%s/%s'%(id_niv,id_grado,m))
                else:
                    mat = Materia.objects.get(pk=m)
                    mat.usuarios.add(us)
                    mat.save()
                    return HttpResponseRedirect('/nivel/%s/%s/%s'%(id_niv,id_grado,m))
            else:
                form = AddMateria(request.POST,request.FILES)
                if form.is_valid():
                    add = form.save(commit=False)
                    add.grado_id = id_grado
                    add.niv_id = id_niv
                    form.save()
                    return HttpResponseRedirect('/nivel/%s/%s'%(id_niv,id_grado))
                else:
                    form = AddMateria()     
        ctx = {'niv':niv,'grado':grados,'materia':materia,'form':form}
        return render(request, 'materias/singlegrado.html', ctx)
    else:
        return HttpResponseRedirect('/login')
def singleMateria(request,id_niv,id_grado,id_mat):
    if request.user.is_authenticated():
        niv = Grado.objects.get(id=id_niv)
        grados = GradoNivel.objects.get(id=id_grado)
        materia = Materia.objects.get(id=id_mat)
        tema = Temas.objects.filter(materia_id=id_mat)
        if request.method == "POST":
            form = AddTemas(request.POST,request.FILES)
            if form.is_valid():
                add = form.save(commit=False)
                add.materia_id = id_mat
                form.save()
                return HttpResponseRedirect('/nivel/%s/%s/%s'%(id_niv,id_grado,id_mat))
        else:
            form = AddTemas()     
        ctx = {'niv':niv,'grado':grados,'materia':materia,'form':form,'tema':tema}
        return render(request, 'materias/singlemateria.html', ctx)
    else:
        return HttpResponseRedirect('/login')
def singleTema(request,id_niv,id_grado,id_mat,id_tema,id_use):
    if request.user.is_authenticated():
        msg = ""
        niv = Grado.objects.get(id=id_niv)
        grados = GradoNivel.objects.get(id=id_grado)
        materia = Materia.objects.get(id=id_mat)
        tema = Temas.objects.get(id=id_tema)
        contenido = ContentTema.objects.filter(tema_id=id_tema)
        problemas = temaProblema.objects.filter(tema_id=id_tema)
        problemas2 = problemas.exclude(usa=id_use)
        if problemas2:
            problemarandom = random.choice(problemas2)
        else:
            problemarandom=""
        if request.method == "POST":
            if "pro.id" in request.POST: 
                id_prob = request.POST['pro.id']
                id_us = request.POST['user_id']
                problema = temaProblema.objects.get(id=id_prob)
                resultado = request.POST['fname']
                if problema.resultado == resultado:
                    msg = "¡Felicidades! Continua"
                    problema.usa.add(id_use)
                    problema.save()
                    return HttpResponseRedirect('/nivel/%s/%s/%s/%s/%s'%(id_niv,id_grado,id_mat,id_tema,id_use))
                else:
                    msg = "Incorrecto sigue intentando"
                    return HttpResponseRedirect('/nivel/%s/%s/%s/%s/%s'%(id_niv,id_grado,id_mat,id_tema,id_use))
            form = AddContentTema(request.POST,request.FILES)
            if form.is_valid():
                add = form.save(commit=False)
                add.tema_id = id_tema
                form.save()
                return HttpResponseRedirect('/nivel/%s/%s/%s/%s/%s'%(id_niv,id_grado,id_mat,id_tema,id_use))
        else:
            form = AddContentTema()     
        ctx = {'niv':niv,'grado':grados,'materia':materia,'form':form,'tema':tema,'cont':contenido,'pro':problemas2,'msg':msg,'pr':problemarandom}
        return render(request, 'materias/singleTema.html', ctx)
    else:
        return HttpResponseRedirect('/login')




