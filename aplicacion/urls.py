from django.urls import path, include
from .views import *

urlpatterns = [
    
    #Si a continuación de la ruta aplicación no aparece nada. Entonces se ejecuta la función index dentro de views.py
    path('', index, name='inicio'),

    path('equipos/', equipos, name='equipos'),
    path('mantenimientos/', mantenimientos, name='mantenimientos'),
    path('empleados/', empleados, name='empleados'),

    path('mantenimiento_form/', mantenimientoForm, name='mantenimiento_form'),
    path('busquedaMantenimiento/', busquedaMantenimiento, name='busquedaMantenimiento'),
    path('buscarMantenimiento/', buscarMantenimiento),

    path('equipo_form/', equipoForm, name='equipo_form'),
    path('busquedaEquipo/', busquedaEquipo, name='busquedaEquipo'),
    path('buscarEquipo/', buscarEquipo),

    path('empleado_form/', empleadoForm, name='empleado_form'),
    path('empleadoMantenimiento/', busquedaEmpleado, name='busquedaEmpleado'),
    path('buscarEmpleado/', buscarEmpleado),

    
]
