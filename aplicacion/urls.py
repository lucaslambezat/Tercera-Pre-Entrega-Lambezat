from django.urls import path, include
from .views import *

urlpatterns = [
    
    #Si a continuación de la ruta aplicación no aparece nada. Entonces se ejecuta la función index dentro de views.py
    path('', index, name='inicio'),

    path('equipos/', equipos, name='equipos'),
    path('mantenimientos/', mantenimientos, name='mantenimientos'),
    path('empleados/', empleados, name='empleados'),
    path('mantenimiento_form/', mantenimientoForm, name='mantenimiento_form'),
    path('buscar_mantenimiento/', buscarMantenimiento, name='buscar_mantenimiento'),

    path('cursos/', cursos, name='cursos'),

    #path('curso_form2/', cursoForm2, name='curso_form2'),

    path('buscar_comision/', buscarComision, name='buscar_comision'),
    path('buscar2/', buscar2, name='buscar2'),

    
    
]
