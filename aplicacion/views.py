from django.shortcuts import render
from .models import *
from .forms import *

def index(request):
    return render(request, "aplicacion/index.html")

#Creamos rutas para cada uno de los modelos.

def equipos(request):
    ctx = {"equipos": Equipo.objects.all()}
    return render(request, "aplicacion/equiposPlanta.html", ctx)

def mantenimientos(request):
    ctx = {"mantenimientos": Mantenimiento.objects.all()}
    return render(request, "aplicacion/mantenimientos.html", ctx)

def empleados(request):
    ctx = {"empleados": Empleado.objects.all()}
    return render(request, "aplicacion/empleados.html", ctx)

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

def buscarMantenimiento(request):
    if request.GET['numero_operacion']:
        numero_operacion = request.GET['numero_operacion']
        mantenimientos = Mantenimiento.objects.filter(numero_operacion__icontains=numero_operacion)
        return render(request, 
                      "aplicacion/resultadosMantenimientos.html", 
                      {"numero_operacion": numero_operacion, "mantenimientos":mantenimientos})
    #return HttpResponse("No se ingresaron datos para buscar!")




def cursos(request):
    ctx = {"cursos": Curso.objects.all()}
    return render(request, "aplicacion/cursos.html",ctx)

def buscarComision(request):
    return render(request, "aplicacion/buscarComision.html")

def buscar2(request):
    if request.GET['comision']:
        comision = request.GET['comision']
        cursos = Curso.objects.filter(comision__icontains=comision)
        return render(request, 
                      "aplicacion/resultadosComision.html", 
                      {"comision": comision, "cursos":cursos})
    """return HttpResponse("No se ingresaron datos para buscar!")"""