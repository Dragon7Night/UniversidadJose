from django import forms
from djangoUniJose.models import Estudiante, Docente

from django.core import validators

# ---↓↓↓--[FORMULARIO DE ESTUDIANTE]--↓↓↓------------------------------------------------


# EDITAR un estudiante
class RegistroEstudianteForm(forms.Form):

# Definicion de campos del fourmulario + validaciones simples
    nombre = forms.CharField(validators=[
        validators.MinLengthValidator(3),
        validators.MaxLengthValidator(25)
    ])
    apellido = forms.CharField(validators=[
        validators.MinLengthValidator(3),
        validators.MaxLengthValidator(25)
    ])
    correo = forms.CharField()
    telefono = forms.CharField(validators=[
        validators.MinLengthValidator(9),
        validators.MaxLengthValidator(12)
    ])
    direccion = forms.CharField(validators=[
        validators.MinLengthValidator(10),
        validators.MaxLengthValidator(25)
    ])
    ciudad = forms.CharField(validators=[
        validators.MinLengthValidator(3),
        validators.MaxLengthValidator(25)
    ])
    pais = forms.CharField(validators=[
        validators.MinLengthValidator(3),
        validators.MaxLengthValidator(25)
    ])
    fecha_registro = forms.CharField()
    carrera = forms.CharField(validators=[
        validators.MinLengthValidator(3),
        validators.MaxLengthValidator(25)
    ])
    anio_ingreso = forms.IntegerField(validators=[
        validators.MinValueValidator(1960),
        validators.MaxValueValidator(2100)
    ])
    promedio = forms.IntegerField(validators=[
        validators.MinValueValidator(10),
        validators.MaxValueValidator(70)
    ])
    estado = forms.CharField(validators=[
        validators.MinLengthValidator(3),
        validators.MaxLengthValidator(20)
    ])
    fecha_nacimiento = forms.CharField()
    genero = forms.CharField(validators=[
        validators.MinLengthValidator(3),
        validators.MaxLengthValidator(20)
    ])
    observaciones = forms.CharField(validators=[
        validators.MinLengthValidator(3),
        validators.MaxLengthValidator(300)
    ])


    # validacion de correo electronico
    def clean_email(self):
        correo_ingresado = self.cleaned_data['correo']
        if correo_ingresado.find('@') == -1:
            raise forms.ValidationError("El correo debe tener un @ para ser valido")
        return correo_ingresado


    # Style formulario de BS5
    nombre.widget.attrs['class'] = 'form-control'
    apellido.widget.attrs['class'] = 'form-control'
    correo.widget.attrs['class'] = 'form-control'
    telefono.widget.attrs['class'] = 'form-control'
    direccion.widget.attrs['class'] = 'form-control'
    ciudad.widget.attrs['class'] = 'form-control'
    pais.widget.attrs['class'] = 'form-control'
    fecha_registro.widget.attrs['class'] = 'form-control'
    carrera.widget.attrs['class'] = 'form-control'
    anio_ingreso.widget.attrs['class'] = 'form-control'
    promedio.widget.attrs['class'] = 'form-control'
    estado.widget.attrs['class'] = 'form-control'
    fecha_nacimiento.widget.attrs['class'] = 'form-control'
    genero.widget.attrs['class'] = 'form-control'
    observaciones.widget.attrs['class'] = 'form-control'

    # Tag para nombres personalizado
    nombre.label = 'Nombre'
    apellido.label = 'Apellido'
    correo.label = 'Correo'
    telefono.label = 'Teléfono'
    direccion.label = 'Dirección'
    ciudad.label = 'Ciudad'
    pais.label = 'País'
    fecha_registro.label = 'Fecha de registro'
    carrera.label = 'Carrera'
    anio_ingreso.label = 'Año de ingreso'
    promedio.label = 'Promedio'
    estado.label = 'Estado'
    fecha_nacimiento.label = 'Fecha de nacimiento'
    genero.label = 'Género'
    observaciones.label = 'Observaciones'


# REGISTRAR un estudiante
class RegistroEstudianteForm(forms.ModelForm):
    class Meta:
        model = Estudiante
        fields = '__all__'
    
# Definicion de campos del fourmulario + validaciones simples
    nombre = forms.CharField(validators=[
        validators.MinLengthValidator(3),
        validators.MaxLengthValidator(25)
    ])
    apellido = forms.CharField(validators=[
        validators.MinLengthValidator(3),
        validators.MaxLengthValidator(25)
    ])
    correo = forms.CharField()
    telefono = forms.CharField(validators=[
        validators.MinLengthValidator(9),
        validators.MaxLengthValidator(12)
    ])
    direccion = forms.CharField(validators=[
        validators.MinLengthValidator(10),
        validators.MaxLengthValidator(25)
    ])
    ciudad = forms.CharField(validators=[
        validators.MinLengthValidator(3),
        validators.MaxLengthValidator(25)
    ])
    pais = forms.CharField(validators=[
        validators.MinLengthValidator(3),
        validators.MaxLengthValidator(25)
    ])
    fecha_registro = forms.CharField()
    carrera = forms.CharField(validators=[
        validators.MinLengthValidator(3),
        validators.MaxLengthValidator(25)
    ])
    anio_ingreso = forms.IntegerField(validators=[
        validators.MinValueValidator(1960),
        validators.MaxValueValidator(2100)
    ])
    promedio = forms.IntegerField(validators=[
        validators.MinValueValidator(10),
        validators.MaxValueValidator(70)
    ])
    estado = forms.CharField(validators=[
        validators.MinLengthValidator(3),
        validators.MaxLengthValidator(20)
    ])
    fecha_nacimiento = forms.CharField()
    genero = forms.CharField(validators=[
        validators.MinLengthValidator(3),
        validators.MaxLengthValidator(20)
    ])
    observaciones = forms.CharField(validators=[
        validators.MinLengthValidator(3),
        validators.MaxLengthValidator(300)
    ])

    
    # validacion de correo electronico
    def clean_email(self):
        correo_ingresado = self.cleaned_data['correo']
        if correo_ingresado.find('@') == -1:
            raise forms.ValidationError("El correo debe tener un @ para ser valido")
        return correo_ingresado


    # Style formulario de BS5
    nombre.widget.attrs['class'] = 'form-control'
    apellido.widget.attrs['class'] = 'form-control'
    correo.widget.attrs['class'] = 'form-control'
    telefono.widget.attrs['class'] = 'form-control'
    direccion.widget.attrs['class'] = 'form-control'
    ciudad.widget.attrs['class'] = 'form-control'
    pais.widget.attrs['class'] = 'form-control'
    fecha_registro.widget.attrs['class'] = 'form-control'
    carrera.widget.attrs['class'] = 'form-control'
    anio_ingreso.widget.attrs['class'] = 'form-control'
    promedio.widget.attrs['class'] = 'form-control'
    estado.widget.attrs['class'] = 'form-control'
    fecha_nacimiento.widget.attrs['class'] = 'form-control'
    genero.widget.attrs['class'] = 'form-control'
    observaciones.widget.attrs['class'] = 'form-control'

    # Tag para nombres personalizado
    nombre.label = 'Nombre'
    apellido.label = 'Apellido'
    correo.label = 'Correo'
    telefono.label = 'Teléfono'
    direccion.label = 'Dirección'
    ciudad.label = 'Ciudad'
    pais.label = 'País'
    fecha_registro.label = 'Fecha de registro'
    carrera.label = 'Carrera'
    anio_ingreso.label = 'Año de ingreso'
    promedio.label = 'Promedio'
    estado.label = 'Estado'
    fecha_nacimiento.label = 'Fecha de nacimiento'
    genero.label = 'Género'
    observaciones.label = 'Observaciones'


# ---↓↓↓--[FORMULARIO DE DOCENTE]--↓↓↓------------------------------------------------

# EDITAR un docente
class RegistroDocenteForm(forms.Form):

    # Definicion de campos del fourmulario + validaciones simples
    nombre = forms.CharField(validators=[
        validators.MinLengthValidator(3),
        validators.MaxLengthValidator(25)
    ])
    apellido = forms.CharField(validators=[
        validators.MinLengthValidator(3),
        validators.MaxLengthValidator(25)
    ])
    asignatura = forms.CharField(validators=[
        validators.MinLengthValidator(3),
        validators.MaxLengthValidator(50)
    ])
    grado_academico = forms.CharField(validators=[
        validators.MinLengthValidator(3),
        validators.MaxLengthValidator(30)
    ])
    correo = forms.CharField()
    telefono = forms.CharField(validators=[
        validators.MinLengthValidator(9),
        validators.MaxLengthValidator(12)
    ])
    direccion = forms.CharField(validators=[
        validators.MinLengthValidator(3),
        validators.MaxLengthValidator(20)
    ])
    ciudad = forms.CharField(validators=[
        validators.MinLengthValidator(3),
        validators.MaxLengthValidator(20)
    ])
    pais = forms.CharField(validators=[
        validators.MinLengthValidator(3),
        validators.MaxLengthValidator(20)
    ])
    fecha_contratacion = forms.CharField()
    estado = forms.CharField(validators=[
        validators.MinLengthValidator(3),
        validators.MaxLengthValidator(25)
    ])
    anios_experiencia = forms.IntegerField(validators=[
        validators.MinValueValidator(0),
        validators.MaxValueValidator(80)
    ])
    horario_clases = forms.CharField()
    observaciones = forms.CharField(validators=[
        validators.MinLengthValidator(10),
        validators.MaxLengthValidator(300)
    ])

    # validacion de correo electronico
    def clean_email(self):
        correo_ingresado = self.cleaned_data['correo']
        if correo_ingresado.find('@') == -1:
            raise forms.ValidationError("El correo debe tener un @ para ser valido")
        return correo_ingresado

    # Style formulario de BS5
    nombre.widget.attrs['class'] = 'form-control'
    apellido.widget.attrs['class'] = 'form-control'
    asignatura.widget.attrs['class'] = 'form-control'
    grado_academico.widget.attrs['class'] = 'form-control'
    correo.widget.attrs['class'] = 'form-control'
    telefono.widget.attrs['class'] = 'form-control'
    direccion.widget.attrs['class'] = 'form-control'
    ciudad.widget.attrs['class'] = 'form-control'
    pais.widget.attrs['class'] = 'form-control'
    fecha_contratacion.widget.attrs['class'] = 'form-control'
    estado.widget.attrs['class'] = 'form-control'
    anios_experiencia.widget.attrs['class'] = 'form-control'
    horario_clases.widget.attrs['class'] = 'form-control'
    observaciones.widget.attrs['class'] = 'form-control'

    # Tag para nombres personalizado
    nombre.label = 'Nombre'
    apellido.label = 'Apellido'
    asignatura.label = 'Asignatura'
    grado_academico.label = 'Grado Académico'
    correo.label = 'Correo'
    telefono.label = 'Teléfono'
    direccion.label = 'Dirección'
    ciudad.label = 'Ciudad'
    pais.label = 'País'
    fecha_contratacion.label = 'Fecha de Contratación'
    estado.label = 'Estado'
    anios_experiencia.label = 'Años de Experiencia'
    horario_clases.label = 'Horario de Clases'
    observaciones.label = 'Observaciones'

# REGISTRAR un docente
class RegistroDocenteForm(forms.ModelForm):
    class Meta:
        model = Docente
        fields = '__all__'

    # Definicion de campos del fourmulario + validaciones simples
    nombre = forms.CharField(validators=[
        validators.MinLengthValidator(3),
        validators.MaxLengthValidator(25)
    ])
    apellido = forms.CharField(validators=[
        validators.MinLengthValidator(3),
        validators.MaxLengthValidator(25)
    ])
    asignatura = forms.CharField(validators=[
        validators.MinLengthValidator(3),
        validators.MaxLengthValidator(50)
    ])
    grado_academico = forms.CharField(validators=[
        validators.MinLengthValidator(3),
        validators.MaxLengthValidator(30)
    ])
    correo = forms.CharField()
    telefono = forms.CharField(validators=[
        validators.MinLengthValidator(9),
        validators.MaxLengthValidator(12)
    ])
    direccion = forms.CharField(validators=[
        validators.MinLengthValidator(3),
        validators.MaxLengthValidator(20)
    ])
    ciudad = forms.CharField(validators=[
        validators.MinLengthValidator(3),
        validators.MaxLengthValidator(20)
    ])
    pais = forms.CharField(validators=[
        validators.MinLengthValidator(3),
        validators.MaxLengthValidator(20)
    ])
    fecha_contratacion = forms.CharField()
    estado = forms.CharField(validators=[
        validators.MinLengthValidator(3),
        validators.MaxLengthValidator(25)
    ])
    anios_experiencia = forms.IntegerField(validators=[
        validators.MinValueValidator(0),
        validators.MaxValueValidator(80)
    ])
    horario_clases = forms.CharField()
    observaciones = forms.CharField(validators=[
        validators.MinLengthValidator(10),
        validators.MaxLengthValidator(300)
    ])

    # validacion de correo electronico
    def clean_email(self):
        correo_ingresado = self.cleaned_data['correo']
        if correo_ingresado.find('@') == -1:
            raise forms.ValidationError("El correo debe tener un @ para ser valido")
        return correo_ingresado

    # Style formulario de BS5
    nombre.widget.attrs['class'] = 'form-control'
    apellido.widget.attrs['class'] = 'form-control'
    asignatura.widget.attrs['class'] = 'form-control'
    grado_academico.widget.attrs['class'] = 'form-control'
    correo.widget.attrs['class'] = 'form-control'
    telefono.widget.attrs['class'] = 'form-control'
    direccion.widget.attrs['class'] = 'form-control'
    ciudad.widget.attrs['class'] = 'form-control'
    pais.widget.attrs['class'] = 'form-control'
    fecha_contratacion.widget.attrs['class'] = 'form-control'
    estado.widget.attrs['class'] = 'form-control'
    anios_experiencia.widget.attrs['class'] = 'form-control'
    horario_clases.widget.attrs['class'] = 'form-control'
    observaciones.widget.attrs['class'] = 'form-control'

    # Tag para nombres personalizado
    nombre.label = 'Nombre'
    apellido.label = 'Apellido'
    asignatura.label = 'Asignatura'
    grado_academico.label = 'Grado Académico'
    correo.label = 'Correo'
    telefono.label = 'Teléfono'
    direccion.label = 'Dirección'
    ciudad.label = 'Ciudad'
    pais.label = 'País'
    fecha_contratacion.label = 'Fecha de Contratación'
    estado.label = 'Estado'
    anios_experiencia.label = 'Años de Experiencia'
    horario_clases.label = 'Horario de Clases'
    observaciones.label = 'Observaciones'

