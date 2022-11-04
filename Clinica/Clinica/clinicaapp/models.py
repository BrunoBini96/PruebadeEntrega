from django.db import models

class Pacientes(models.Model):
    nombre = models.CharField(max_length = 20)
    apellido = models.CharField(max_length = 20)
    dni = models.CharField(max_length = 8)
    telefono = models.CharField(max_length = 10)
    obra_social = models.CharField(max_length = 20)

class Doctores(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    dni = models.CharField(max_length=8)
    especialidad = models.CharField(max_length=20)
    consultorio = models.CharField(max_length=20)

class Turnos(models.Model):
    doctor = models.CharField(max_length=20)
    paciente = models.CharField(max_length=20)
    horario = models.TimeField()
    fecha = models.DateField()
    consultorio = models.CharField(max_length=20)
