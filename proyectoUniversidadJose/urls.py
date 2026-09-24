"""
URL configuration for proyectoUniversidadJose project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from djangoUniJose import views as app1

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', app1.homeUni, name='homeUniversidad'),
    path('dataEstudiante/', app1.estudianteData, name='estudianteDataName'),
    path('registroEstudiante/', app1.registrarEstudiante, name='estudianteRegisterN'),
    path('editarEstudiante/<int:id>', app1.editarEstudiante, name='estudianteEditarN'),
    path('eliminarEstudiante/<int:id>', app1.eliminarEstudiante, name='estudianteEliminarN'),
    path('dataDocente/', app1.docenteData, name='docenteDataName'),
    path('registroDocente/', app1.registrarDocente, name='docenteRegisterN'),
    path('editarDocente/<int:id>', app1.editarDocente, name='docenteEditarN'),
    path('eliminarDocente/<int:id>', app1.eliminarDocente, name='docenteEliminarN'),
]
