from django.shortcuts import render
from .models import *
from .forms import *
from django.http import HttpResponse

def index(request):
    return render(request, "aplicacion/index.html")

#Creo rutas para cada uno de los modelos.

def equipos(request):
    ctx = {"equipos": Equipo.objects.all()}
    return render(request, "aplicacion/equipos.html", ctx)


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


def busquedaMantenimiento(request):

    return render(request, "aplicacion/busquedaMantenimiento.html")

def buscarMantenimiento(request):

    if request.GET["numero_operacion"]:
        num_op_buscada = request.GET['numero_operacion']
        mantenimientos = Mantenimiento.objects.filter(numero_operacion__icontains= num_op_buscada)
        return render(request, "aplicacion/resultadosMantenimiento.html", {"mantenimientos": mantenimientos})
    
    else:
        
        respuesta = "No enviaste datos."
    
    #respuesta = f"Estoy buscando el mantenimiento con número de operación: {request.GET['numero_operacion']}"

    return HttpResponse(respuesta)




def equipoForm(request):
    if request.method == "POST":
        miForm = EquipoForm(request.POST)
        if miForm.is_valid():
            eq_nombre = miForm.cleaned_data.get('nombre')
            eq_marca = miForm.cleaned_data.get('marca')
            eq_sector = miForm.cleaned_data.get('sector')
            eq_referencia = miForm.cleaned_data.get('referencia')
            
            equipo = Equipo(nombre=eq_nombre, 
                            marca=eq_marca ,
                            sector=eq_sector,
                            referencia =eq_referencia
                            )
            
            equipo.save()
            return render(request, "aplicacion/index.html")
    else:       
        miForm = EquipoForm()
    return render(request, "aplicacion/equipoForm.html", {"form":miForm})

def busquedaEquipo(request):

    return render(request, "aplicacion/busquedaEquipo.html")

def buscarEquipo(request):
    
    if request.GET["referencia"]:
        ref_buscada = request.GET['referencia']
        equipos = Equipo.objects.filter(referencia__icontains= ref_buscada)
        return render(request, "aplicacion/resultadosEquipo.html", {"equipos": equipos, "referencia":ref_buscada})
    
    else:
        
        respuesta = "No enviaste datos."
    
    #respuesta = f"Estoy buscando el mantenimiento con número de operación: {request.GET['numero_operacion']}"

    return HttpResponse(respuesta)




def empleadoForm(request):
    if request.method == "POST":
        miForm = EmpleadoForm(request.POST)
        if miForm.is_valid():
            emp_nombre = miForm.cleaned_data.get('nombre')
            emp_apellido = miForm.cleaned_data.get('apellido')
            emp_rol = miForm.cleaned_data.get('rol')
            emp_email = miForm.cleaned_data.get('email')
            emp_telefono = miForm.cleaned_data.get('telefono')
            
            empleado = Empleado(nombre = emp_nombre, 
                            apellido = emp_apellido ,
                            rol = emp_rol,
                            email = emp_email,
                            telefono = emp_telefono
                            )
            
            empleado.save()
            return render(request, "aplicacion/index.html")
    else:       
        miForm = EmpleadoForm()
    return render(request, "aplicacion/empleadoForm.html", {"form":miForm})

def busquedaEmpleado(request):

    return render(request, "aplicacion/busquedaEmpleado.html")

def buscarEmpleado(request):
    
    if request.GET["apellido"]:
        apellido_buscado = request.GET['apellido']
        empleados = Empleado.objects.filter(apellido__icontains= apellido_buscado)
        return render(request, "aplicacion/resultadosEmpleado.html", {"empleados": empleados})
    
    else:
        
        respuesta = "No enviaste datos."

    return HttpResponse(respuesta)