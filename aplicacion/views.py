from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from .models import *
from .forms import *

from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView


def index(request):
    return render(request, "aplicacion/index.html")

#Creamos rutas para cada uno de los modelos.

class EquipoList(ListView):
    model = Equipo

class EquipoCreate(CreateView):
    model = Equipo
    fields = ['nombre', 'marca', 'sector', 'referencia']
    success_url = reverse_lazy('equipos')

class EquipoDetail(DetailView):
    model = Equipo

class EquipoUpdate(UpdateView):
    model = Equipo
    fields = ['nombre', 'marca', 'sector', 'referencia']
    success_url = reverse_lazy('equipos')

class EquipoDelete(DeleteView):
    model = Equipo
    success_url = reverse_lazy('equipos')

def busquedaEquipo(request):

    return render (request, "aplicacion/equipo_busqueda.html")

def buscarEquipo(request):

    if request.GET["referencia"]:

        referencia = request.GET['referencia']
        equipos = Equipo.objects.filter(referencia__icontains=referencia)
        return render(request, 
                      "aplicacion/equipo_resultados.html", 
                      {"referencia": referencia, "equipos":equipos})
    else:

        return HttpResponse("No se ingresaron datos para buscar!")





class EmpleadoList(ListView):
    model = Empleado

class EmpleadoCreate(CreateView):
    model = Empleado
    fields = ['nombre', 'apellido', 'rol', 'email', 'telefono']
    success_url = reverse_lazy('empleados')

class EmpleadoDetail(DetailView):
    model = Empleado

class EmpleadoUpdate(UpdateView):
    model = Empleado
    fields = ['nombre', 'apellido', 'rol', 'email', 'telefono']
    success_url = reverse_lazy('empleados')

class EmpleadoDelete(DeleteView):
    model = Empleado
    success_url = reverse_lazy('empleados')

def busquedaEmpleado(request):

    return render (request, "aplicacion/empleado_busqueda.html")

def buscarEmpleado(request):

    if request.GET["apellido"]:

        apellido = request.GET['apellido']
        empleados = Empleado.objects.filter(apellido__icontains=apellido)
        return render(request, 
                      "aplicacion/empleado_resultados.html", 
                      {"apellido": apellido, "empleados":empleados})
    else:

        return HttpResponse("No se ingresaron datos para buscar!")





def mantenimientos(request):
    ctx = {"mantenimientos": Mantenimiento.objects.all()}
    return render(request, "aplicacion/mantenimientos.html", ctx)



def mantenimientoForm(request):
    if request.method == "POST":
        miForm = MantenimientoForm(request.POST)
        if miForm.is_valid():
            mant_num_operacion = miForm.cleaned_data.get('numero_operacion')
            mant_descripcion = miForm.cleaned_data.get('descripcion')
            mant_planificado = miForm.cleaned_data.get('planificado')
            mant_fecha = miForm.cleaned_data.get('fecha')
            
            mantenimiento = Mantenimiento(numero_operacion=mant_num_operacion, 
                                          descripcion=mant_descripcion ,
                                          planificado=mant_planificado,
                                          fecha=mant_fecha
                                          )
            mantenimiento.save()
            return render(request, "aplicacion/index.html")
    else:       
        miForm = MantenimientoForm()
    return render(request, "aplicacion/mantenimientoForm.html", {"form":miForm})


