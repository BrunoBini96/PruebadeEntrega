from django import forms 
from .models import *

class PacienteFormulario(forms.Form):
    nombre = forms.CharField(max_length = 20)
    apellido = forms.CharField(max_length= 20)
    dni = forms.CharField(max_length= 8)
    telefono = forms.CharField(max_length=10)
    obra_social = forms.CharField(max_length=20)

class DoctorFormulario(forms.Form):
    nombre = forms.CharField(max_length=20)
    apellido = forms.CharField(max_length=20)
    dni = forms.CharField(max_length=8)
    especialidad = forms.CharField(max_length=20)
    consultorio = forms.CharField(max_length=20)

class TurnosFormulario(forms.Form):
    doctor = forms.CharField(max_length = 20)
    paciente = forms.CharField(max_length = 20) 
    horario = forms.TimeField
    fecha = forms.DateField
    consultorio = forms.CharField(max_length = 20)   