from django.contrib import admin

from djangoUniJose.models import Estudiante, Docente

# Register your models here.

class EstudianteAdmin(admin.ModelAdmin):
    list_display = ['id','nombre','apellido','correo','telefono','direccion','ciudad','pais','fecha_registro','carrera','anio_ingreso','promedio','estado','fecha_nacimiento','genero','observaciones']

admin.site.register(Estudiante, EstudianteAdmin)


class DocenteAdmin(admin.ModelAdmin):
    list_display = ['id','nombre','apellido','asignatura','grado_academico','correo','telefono','direccion','ciudad','pais','fecha_contratacion','estado','anios_experiencia','horario_clases','observaciones']

admin.site.register(Docente, DocenteAdmin)



