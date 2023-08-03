from django import forms

#Creo las clases formulario que van a resolver todos los campos de mis formularios. 

class MantenimientoForm(forms.Form):
    numero_operacion = forms.IntegerField(label="Número de Operación", required=True)
    descripcion = forms.CharField(label="Descripción",max_length=50, required=True)
    
    """OPCIONES = (
        ("SI"),
        ("NO"),
        ("DESCONOCE"),
    )"""

    planificado = forms.CharField(label="Fue Planificado?",max_length=10, required=True)
    fecha = forms.DateField(label="Fecha (DD/MM/AAAA)",required=True)
    

class EquipoForm(forms.Form):
    
    nombre = forms.CharField(label="Nombre del Equipo:", max_length=50, required=True)
    marca = forms.CharField(label="Marca y Modelo:", max_length=50, required=True)
    sector = forms.CharField(label="Sector de la Planta:", max_length=50, required=True)
    referencia = forms.CharField(label="Referencia:", max_length=6, required=True)


class EmpleadoForm(forms.Form):

    nombre = forms.CharField(max_length=50, required=True)
    apellido = forms.CharField(max_length=50, required=True)
    rol = forms.CharField(max_length=50, required=True)
    email = forms.EmailField(required=True)
    telefono = forms.CharField(max_length=50)