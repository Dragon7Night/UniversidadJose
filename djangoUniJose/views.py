from django.shortcuts import render

from djangoUniJose.models import Estudiante, Docente

from djangoUniJose.forms import RegistroEstudianteForm, RegistroDocenteForm

from django.urls import reverse
from django.http import HttpResponseRedirect

# Create your views here.


def homeUni(request):
    data = {'imgLogo':'img/logo.jpg'}
    return render(request, 'djangoUniJose/index.html',data)


# ----------[view para el ESTUDIANTE]-------------------------------------------------

def estudianteData(request):
    estudianteObject = Estudiante.objects.all()
    data = {
        'estudianteKey':estudianteObject,
        'mainTitle':'Registros de estudiantes',
        'titulo':'Estudiates registrados',
        'colorBg':'text-bg-success'
    }
    return render(request, 'djangoUniJose/dataEstudiante.html',data)


def registrarEstudiante(request):
    form = RegistroEstudianteForm()
    if request.method == 'POST':
        form = RegistroEstudianteForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('estudianteDataName'))
        
    data = {
        'formKey':form,
        'mainTitle':'Registro de estudiantes',
        'txtForm':'Formulario de registro estudiantes',
        'txtBtn':'Registrar estudiante',
        'colorBg':'text-bg-warning'
    }
    return render(request, 'djangoUniJose/registroUsuarios.html',data)

def editarEstudiante(request, id):
    estudianteObjects = Estudiante.objects.get(id=id)
    form = RegistroEstudianteForm(instance=estudianteObjects) 

    if request.method == 'POST':
        form = RegistroEstudianteForm(request.POST, instance=estudianteObjects) 
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('estudianteDataName'))
    
    data = {
        'formKey':form,
        'txtForm':'Modificar datos del estudiante',
        'txtBtn':'Confirmar cambios',
        'colorBg':'text-bg-info'
    }

    return render(request, 'djangoUniJose/registroUsuarios.html',data)

def eliminarEstudiante(request, id):
    estudianteObjects = Estudiante.objects.get(id=id)
    estudianteObjects.delete()
    return HttpResponseRedirect(reverse('estudianteDataName'))



# ----------[view para el DOCENTE]-------------------------------------------------

def docenteData(request):
    docenteObject = Docente.objects.all()
    data = {
        'docenteKey':docenteObject,
        'mainTitle':'Registros de docentes',
        'titulo':'Docentes registrados',
        'colorBg':'text-bg-danger'
    }
    return render(request, 'djangoUniJose/dataDocente.html',data)


def registrarDocente(request):
    form = RegistroDocenteForm()
    if request.method == 'POST':
        form = RegistroDocenteForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('docenteDataName'))
        
    data = {
        'formKey':form,
        'mainTitle':'Registro de docentes',
        'txtForm':'Formulario de registro docentes',
        'txtBtn':'Registrar docente',
        'colorBg':'text-bg-warning'
    }
    return render(request, 'djangoUniJose/registroUsuarios.html',data)

def editarDocente(request, id):
    docenteObjects = Docente.objects.get(id=id)
    form = RegistroDocenteForm(instance=docenteObjects) 

    if request.method == 'POST':
        form = RegistroDocenteForm(request.POST, instance=docenteObjects) 
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('docenteDataName'))

    data = {
        'formKey':form,
        'txtForm':'Modificar datos del docente',
        'txtBtn':'Confirmar cambios',
        'colorBg':'text-bg-info'
    }
    return render(request, 'djangoUniJose/registroUsuarios.html',data)


def eliminarDocente(request, id):
    estudianteObjects = Docente.objects.get(id=id)
    estudianteObjects.delete()
    return HttpResponseRedirect(reverse('docenteDataName'))
