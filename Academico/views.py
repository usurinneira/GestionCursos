from django.shortcuts import render, redirect
from .models import Curso
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate

# Create your views here.

def home(request):
    cursos = Curso.objects.all()
    return render(request,'gestionCursos.html',{'cursos':cursos})

def registroCurso(request):
    codigo = request.POST['txtCodigo']
    nombre = request.POST['txtNombre']
    creditos = request.POST['txtCredito']

    curso = Curso.objects.create(codigo = codigo, nombre = nombre, creditos = creditos)
    return redirect('/')

def eliminarCurso(request,codigo):
    curso = Curso.objects.get(codigo=codigo)
    curso.delete()
    
    return redirect('/')

def edicionCurso(request,codigo):
    curso = Curso.objects.get(codigo=codigo)

    return render(request,'edicionCurso.html',{'curso':curso})

def editarCurso(request):
    codigo = request.POST['txtCodigo']
    nombre = request.POST['txtNombre']
    creditos = request.POST['txtCredito']

    curso = Curso.objects.get(codigo=codigo)
    curso.nombre = nombre
    curso.creditos = creditos
    curso.save()

    return redirect('/')

def signup(request):
    if request.method == 'GET':
        return render(request,'signup.html',{'form':UserCreationForm})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(username = request.POST['username'], password = request.POST['password1'])
                user.save()
                login(request,user)
                return redirect('inicio')
            except:
                return render(request,'signup.html',{'form':UserCreationForm,'error':'Usuario ya existe'})
            
        return render(request,'signup.html',{'form':UserCreationForm,'error':'Contraseña no coincide'})
    
def signout(request):
    logout(request)
    return redirect('inicio')

def signin(request):
    if request.method == 'GET':
        return render(request,'signin.html',{'form':AuthenticationForm})
    else:
        user = authenticate(request,username=request.POST['username'],password=request.POST['password'])
        if user is None:
            return render(request,'signin.html',{'form':AuthenticationForm,'error':'Usuario y/o contraseña incorrecto'})
        else:
            login(request,user)
            return redirect('inicio')