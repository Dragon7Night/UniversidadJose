from django.db import models

# Create your models here.

class Estudiante(models.Model):

    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    correo = models.CharField(max_length=30)
    telefono = models.CharField(max_length=12)
    direccion = models.CharField(max_length=40)
    ciudad = models.CharField(max_length=50)
    pais = models.CharField(max_length=20)
    fecha_registro = models.CharField(max_length=50)
    carrera = models.CharField(max_length=50)
    anio_ingreso = models.IntegerField()
    promedio = models.IntegerField()
    estado = models.CharField(max_length=25)
    fecha_nacimiento = models.CharField(max_length=35)
    genero = models.CharField(max_length=15)
    observaciones = models.CharField(max_length=50)


class Docente(models.Model):

    nombre = models.CharField(max_length=50) 
    apellido = models.CharField(max_length=50) 
    asignatura = models.CharField(max_length=50) 
    grado_academico = models.CharField(max_length=25) 
    correo = models.CharField(max_length=50) 
    telefono = models.CharField(max_length=12) 
    direccion = models.CharField(max_length=50) 
    ciudad = models.CharField(max_length=15) 
    pais = models.CharField(max_length=15) 
    fecha_contratacion = models.CharField(max_length=50) 
    estado = models.CharField(max_length=15) 
    anios_experiencia = models.IntegerField() 
    horario_clases = models.CharField(max_length=50) 
    observaciones = models.CharField(max_length=50) 
