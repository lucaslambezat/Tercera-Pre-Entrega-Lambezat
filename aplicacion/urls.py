from django.urls import path, include
from .views import *

urlpatterns = [
    
    #Si a continuación de la ruta aplicación no aparece nada. Entonces se ejecuta la función index dentro de views.py
    path('', index, name='inicio'),

    path('equipos/', EquipoList.as_view(), name='equipos'),
    path('create_equipo', EquipoCreate.as_view(), name='create_equipo'),
    path('detail_equipo/<int:pk>/', EquipoDetail.as_view(), name='detail_equipo'),
    path('update_equipo/<int:pk>/', EquipoUpdate.as_view(), name='update_equipo'),
    path('delete_equipo/<int:pk>/', EquipoDelete.as_view(), name='delete_equipo'),
    path('busqueda_equipo/', busquedaEquipo, name='busqueda_equipo'),
    path('buscar_equipo/', buscarEquipo),


    path('empleados/', EmpleadoList.as_view(), name='empleados'),
    path('create_empleado', EmpleadoCreate.as_view(), name='create_empleado'),
    path('detail_empleado/<int:pk>/', EmpleadoDetail.as_view(), name='detail_empleado'),
    path('detail_empleado/<int:pk>/', EmpleadoDetail.as_view(), name='detail_empleado'),
    path('update_empleado/<int:pk>/', EmpleadoUpdate.as_view(), name='update_empleado'),
    path('delete_empleado/<int:pk>/', EmpleadoDelete.as_view(), name='delete_empleado'),
    path('busqueda_empleado/', busquedaEmpleado, name='busqueda_empleado'),
    path('buscar_empleado/', buscarEmpleado),




    path('mantenimientos/', mantenimientos, name='mantenimientos'),
    path('mantenimiento_form/', mantenimientoForm, name='mantenimiento_form'),

    
]
