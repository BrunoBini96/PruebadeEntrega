from django.urls import path
from .views import inicio, pacientes, turnos, doctores,pacienteFormulario,doctorFormulario,turnoFormulario

urlpatterns = [
    path("",inicio),
    path('pacientes/', pacientes , name = "Pacientes"),
    path('doctores/', doctores, name = "Doctores"),
    path('turnos/', turnos, name = "Turnos"),
    path('formuario_de_pacientes/', pacienteFormulario, name = "PacienteFormulario"),
    path('formulario_de_doctor/',doctorFormulario, name = "DoctorFormulario"),
    path('formulario_de_turnos',turnoFormulario, name = "TurnoFormulario")
]
