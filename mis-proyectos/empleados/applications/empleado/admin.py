from datetime import date
from django.contrib import admin
from .models import Empleado, Habilidades
from applications.empleado import models
from . import models
# Register your models here.
admin.site.register(Habilidades)

class EmpleadoAdmin (admin.ModelAdmin):
    list_display = (
        "nombre",
        "apellido",
        "fecha_nac",
        "calcularEdad",
        "pais",
        "trabajo",
        "departamento",
    )

    def calcularEdad (self,obj):
        today = date.today ()
        age = today.year - obj.fecha_nac.year - ((today.month, today.day) < (obj.fecha_nac.month, obj.fecha_nac.day))
        return age
        print (obj)
    

    calcularEdad.short_description = 'edad'
    
    search_fields =(
    'apellido',
    'nombre',
    )
    list_filter = (
        'departamento',
        'trabajo',
        'pais',
        'habilidades',
    )
    filter_horizontal= (
        'habilidades',
    )

admin.site.register(Empleado,EmpleadoAdmin)
