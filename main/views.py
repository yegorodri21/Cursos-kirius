from django.core.files.base import File
from django.http import request
from main.form import NuevoCurso, UserForm, Matriculados
import main
from .models import Curso
from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Curso

# Create your views here.
def homepage (request):
    return render (request, "main/inicio.html", {"cursos": Curso.objects.all})

def registro (request):
    form = UserCreationForm(request.POST)
    
    if request.method=="POST":
        if form.is_valid():
            usuario=form.save()
            nombre_usuario=form.cleaned_data.get('username')
            messages.success(request, f"Nueva cuenta creada : {nombre_usuario}")
            login(request, usuario)
            messages.info(request, f"Haz sido logeado como {nombre_usuario}")
            return redirect("main:homepage")
        else:
            for msg in form.error_messages:
                messages.error(request, f"{msg}: {form.error_messages[msg]}")

    form = UserCreationForm
    return render(request, "main/registro.html", {"form":form})
        
def logout_request(request):
    logout (request)
    messages.info (request,"Saliste exitosamente")
    return redirect("main:homepage")

def login_request(request):

    if request.method=="POST":
        form=AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            usuario=form.cleaned_data.get('username')
            contraseña = form.cleaned_data.get ('password')
            user = authenticate(username=usuario, password=contraseña)

            if user is not None:
                login(request,user)
                messages.info(request, f"Estas logeado como{usuario}")
                return redirect ("main:homepage")
            else:
                messages.error(request, "Usuario o contraseña equivocado")
        else:
            messages.error(request,"Usuario o contraseña equivocada")

    form= AuthenticationForm ()
    return render(request, "main/login.html",{"form":form})

def curso_form(request):
    if request.method == 'GET':
        form = NuevoCurso
        contexto = {
        'form' : form
        }
    else:
        form = NuevoCurso(request.POST, request.FILES)
        contexto = {
        'form' : form
        }
        if form.is_valid():
               curso_form=form.save()
               return redirect('main:homepage')

    return render(request,  "main/cursos.html", contexto)

def registroM(request):
    form = UserForm(request.POST)

    if request.method=='POST':

        if form.is_valid():
            estudiante=form.save()
            registroM=form.cleaned_data.get('Estudiante')
            messages.success(request, f"Estudiante registrado : {registroM}")
            return redirect("main:homepage")
    else:
        
        form = UserForm
  
    return render (request, "main/registroM.html", {"form":form})

def materias(request):
    form = Matriculados(request.POST)

    if request.method=='POST':

        if form.is_valid():
            materia=form.save()
            materias=form.cleaned_data.get('Materia')
            messages.success(request, f"Materia registrada : {materias}")
            return redirect("main:homepage")
    else:

        form = Matriculados
    return render (request, "main/materias.html", {"form":form})

# def materias(request, id):
#     curso = Curso.objects.get(id=id)
#     materia = materias.objects.filter(curso = curso)
#     contexto = {
#         'curso': curso,
#         'materia': materia, 
#     }
#     return render(request, 'main/materias.html', contexto)