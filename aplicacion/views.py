from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from .models import *
from .forms import *

from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, "aplicacion/index.html")

#------------------------------------------------------------------------------------------


#CLASES BASADAS EN VISTA PARA EL "CRUD" DE LOS EQUIPOS.

class EquipoList(LoginRequiredMixin, ListView):
    model = Equipo

class EquipoCreate(LoginRequiredMixin, CreateView):
    model = Equipo
    fields = ['nombre', 'marca', 'sector', 'referencia']
    success_url = reverse_lazy('equipos')

class EquipoDetail(LoginRequiredMixin, DetailView):
    model = Equipo

class EquipoUpdate(LoginRequiredMixin, UpdateView):
    model = Equipo
    fields = ['nombre', 'marca', 'sector', 'referencia']
    success_url = reverse_lazy('equipos')

class EquipoDelete(LoginRequiredMixin, DeleteView):
    model = Equipo
    success_url = reverse_lazy('equipos')

#FUNCIONES PARA LA BÚSQUEDA DE LOS EQUIPOS EN LA BD DE ACUERDO A LA REFERENCIA.

@login_required
def busquedaEquipo(request):

    return render (request, "aplicacion/equipo_busqueda.html")

@login_required
def buscarEquipo(request):

    if request.GET["referencia"]:

        referencia = request.GET['referencia']
        equipos = Equipo.objects.filter(referencia__icontains=referencia)
        return render(request, 
                      "aplicacion/equipo_resultados.html", 
                      {"referencia": referencia, "equipos":equipos})
    else:

        return HttpResponse("No se ingresaron datos para buscar!")

#------------------------------------------------------------------------------------------


#CLASES BASADAS EN VISTA PARA EL "CRUD" DE LOS EMPLEADOS.

class EmpleadoList(LoginRequiredMixin, ListView):
    model = Empleado

class EmpleadoCreate(LoginRequiredMixin, CreateView):
    model = Empleado
    fields = ['nombre', 'apellido', 'rol', 'email', 'telefono']
    success_url = reverse_lazy('empleados')

class EmpleadoDetail(LoginRequiredMixin, DetailView):
    model = Empleado

class EmpleadoUpdate(LoginRequiredMixin, UpdateView):
    model = Empleado
    fields = ['nombre', 'apellido', 'rol', 'email', 'telefono']
    success_url = reverse_lazy('empleados')

class EmpleadoDelete(LoginRequiredMixin, DeleteView):
    model = Empleado
    success_url = reverse_lazy('empleados')

#FUNCIONES PARA LA BÚSQUEDA DE LOS EMPLEADOS EN LA BD DE ACUERDO A LA REFERENCIA.

@login_required
def busquedaEmpleado(request):

    return render (request, "aplicacion/empleado_busqueda.html")

@login_required
def buscarEmpleado(request):

    if request.GET["apellido"]:

        apellido = request.GET['apellido']
        empleados = Empleado.objects.filter(apellido__icontains=apellido)
        return render(request, 
                      "aplicacion/empleado_resultados.html", 
                      {"apellido": apellido, "empleados":empleados})
    else:

        return HttpResponse("No se ingresaron datos para buscar!")

#------------------------------------------------------------------------------------------


#CLASES BASADAS EN VISTA PARA EL "CRUD" DE LOS MANTENIMIENTOS.

class MantenimientoList(LoginRequiredMixin, ListView):
    model = Mantenimiento

class MantenimientoCreate(LoginRequiredMixin, CreateView):
    model = Mantenimiento
    fields = ['numero_operacion', 'descripcion', 'planificado', 'fecha']
    success_url = reverse_lazy('mantenimientos')

class MantenimientoDetail(LoginRequiredMixin, DetailView):
    model = Mantenimiento

class MantenimientoUpdate(LoginRequiredMixin, UpdateView):
    model = Mantenimiento
    fields = ['numero_operacion', 'descripcion', 'planificado', 'fecha']
    success_url = reverse_lazy('mantenimientos')

class MantenimientoDelete(LoginRequiredMixin, DeleteView):
    model = Mantenimiento
    success_url = reverse_lazy('mantenimientos')

#FUNCIONES PARA LA BÚSQUEDA DE LOS MANTENIMIENTOS EN LA BD DE ACUERDO AL NÚMERO DE OPERACIÓN.

@login_required
def busquedaMantenimiento(request):

    return render (request, "aplicacion/mantenimiento_busqueda.html")

@login_required
def buscarMantenimiento(request):

    if request.GET["numero_operacion"]:

        numero_operacion = request.GET['numero_operacion']
        mantenimientos = Mantenimiento.objects.filter(numero_operacion__icontains=numero_operacion)
        return render(request, 
                      "aplicacion/mantenimiento_resultados.html", 
                      {"numero_operacion": numero_operacion, "mantenimientos":mantenimientos})
    else:

        return HttpResponse("No se ingresaron datos para buscar!")

#------------------------------------------------------------------------------------------

def login_request(request):
    if request.method == "POST":
        miForm = AuthenticationForm(request, data=request.POST)
        if miForm.is_valid():
            usuario = miForm.cleaned_data.get('username')
            clave = miForm.cleaned_data.get('password')
            user = authenticate(username=usuario, password=clave)
            if user is not None:
                login(request, user)
                #-------------
                try:
                    avatar = Avatar.objects.get(user=request.user.id).imagen.url
                except:
                    avatar = '/media/avatares/default.png'
                finally:
                    request.session['avatar'] = avatar
                #----------------
                return render(request, "aplicacion/index.html", {"mensaje": f"Bienvenido {usuario}"})
            else:
                return render(request, "aplicacion/login.html", {"form":miForm, "mensaje": "Datos Inválidos"})
        else:    
            return render(request, "aplicacion/login.html", {"form":miForm, "mensaje": "Datos Inválidos"})

    miForm = AuthenticationForm()
    return render(request, "aplicacion/login.html", {"form":miForm}) 


def register(request):
    if request.method == 'POST':
        form = RegistroUsuariosForm(request.POST) # UserCreationForm 
        if form.is_valid():  # Si pasó la validación de Django
            usuario = form.cleaned_data.get('username')
            form.save()
            return render(request, "aplicacion/index.html") #{"mensaje":""})        
    else:
        form = RegistroUsuariosForm() # UserCreationForm 

    return render(request, "aplicacion/registro.html", {"form": form})   
 

#---------------------------------------------------------------------

@login_required
def editarPerfil(request):
    usuario = request.user
    if request.method == "POST":
        form = UserEditForm(request.POST)
        if form.is_valid():
            usuario.email = form.cleaned_data.get('email')
            usuario.password1 = form.cleaned_data.get('password1')
            usuario.password2 = form.cleaned_data.get('password2')
            usuario.first_name = form.cleaned_data.get('first_name')
            usuario.last_name = form.cleaned_data.get('last_name')
            usuario.save()
            return render(request, "aplicacion/index.html", {'mensaje': f"Usuario {usuario.username} actualizado correctamente"})
        else:
            return render(request, "aplicacion/editarPerfil.html", {'form': form})
    else:
        form = UserEditForm(instance=usuario)
    return render(request, "aplicacion/editarPerfil.html", {'form': form, 'usuario':usuario.username})



@login_required
def agregarAvatar(request):
    if request.method == "POST":
        form = AvatarFormulario(request.POST, request.FILES)
        if form.is_valid():
            u = User.objects.get(username=request.user)
            #_________________ Esto es para borrar el avatar anterior
            avatarViejo = Avatar.objects.filter(user=u)
            if len(avatarViejo) > 0: # Si esto es verdad quiere decir que hay un Avatar previo
                avatarViejo[0].delete()

            #_________________ Grabo avatar nuevo
            avatar = Avatar(user=u, imagen=form.cleaned_data['imagen'])
            avatar.save()

            #_________________ Almacenar en session la url del avatar para mostrarla en base
            imagen = Avatar.objects.get(user=request.user.id).imagen.url
            request.session['avatar'] = imagen

            return render(request, "aplicacion/index.html")
    else:
        form = AvatarFormulario()
    return render(request, "aplicacion/agregarAvatar.html", {'form': form})







def mantenimientos(request):
    ctx = {"mantenimientos": Mantenimiento.objects.all()}
    return render(request, "aplicacion/mantenimientos.html", ctx)
