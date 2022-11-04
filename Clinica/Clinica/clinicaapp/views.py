
from django.shortcuts import render,redirect
from .models import Pacientes,Doctores,Turnos
from django.http import HttpResponse
from .forms import PacienteFormulario, DoctorFormulario,TurnosFormulario


def inicio(request):
    
    return render(request,"inicio.html")

def pacientes(request):
    return render(request,'pacientes.html')

def doctores(request):
    return render(request,'doctores.html')

def turnos(request):
    return render(request, 'turnos.html')


def pacienteFormulario(request):
    print('method:', request.method)
    print('post: ', request.POST)
    if request.method == "POST":
        mi_formulario = PacienteFormulario(request.POST)
        if mi_formulario.is_valid():
            data = mi_formulario.cleaned_data
            paciente = Pacientes(nombre=data['nombre'],apellido=data['apellido'],dni=data['dni'],telefono=data['telefono'],obra_social=data['obra_social'])
            paciente.save()
            return redirect('Pacientes')
    else:
        mi_formulario = PacienteFormulario()
        return render(request,'pacienteFormulario.html', {'mi_formulario': mi_formulario})
    
    
def doctorFormulario(request):
    
    if request.method == "POST":
        mi_formulario = DoctorFormulario(request.POST)
        if mi_formulario.is_valid():
            data = mi_formulario.cleaned_data
            doctor = Doctores(nombre=data['nombre'],apellido=data['apellido'],dni=data['dni'],especialidad=data['especialidad'],consultorio=data['consultorio'])
            doctor.save()
            return redirect('Doctores')
    else:
        mi_formulario = DoctorFormulario
        return render(request,'doctorFormulario.html',{'mi_formulario': mi_formulario})

def turnoFormulario(request):
    
    if request.method == "POST":
        mi_formulario = TurnosFormulario(request.POST)
        if  mi_formulario.is_valid():
            data = mi_formulario.cleaned_data
            turno = Turnos(doctor=data['doctor'], paciente=data['paciente'],horario=data['horario'],fecha=data['fecha'],consultorio=data['consultorio'])
            turno.save()
            return redirect('Turnos')
    else:
        mi_formulario = TurnosFormulario
        return render(request,'turnoFormulario.html',{'mi_formulario': mi_formulario})


        
            

    
    
    
        
      
    
    

