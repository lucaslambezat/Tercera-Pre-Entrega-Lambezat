from django import forms

#Creo una clase formulario que va a resolver todos los campos de mi formulario. 

class MantenimientoForm(forms.Form):
    numero_operacion = forms.IntegerField(label="Número de Operación", required=True)
    descripcion = forms.CharField(label="Descripción",max_length=50, required=True)
    
    OPCIONES = (
        (1, "SI"),
        (2, "NO"),
        (3, "DESCONOCE"),
    )
    planificado = forms.ChoiceField(label="¿Fue Planificado?", choices=OPCIONES, required=True)
    
    
    fecha = forms.CharField(label="Fecha (DD/MM/AAAA)",max_length=10, required=True)
    

    