from django.db import models
from applications.departamento.models import Departamento
from ckeditor.fields import RichTextField # type: ignore
# titulo charfield string
# subtitulo charfield string

class Habilidades (models.Model):
    habilidad = models.CharField("Habilidad", max_length=50)

    class Meta:
        verbose_name= "Habilidad"
        verbose_name_plural = "Habilidades del empleado"
        ordering = ["habilidad"]
        unique_together = ("habilidad",)
    def __str__(self):
        return self.habilidad 



class Empleado (models.Model) :
    # Modelo de Empleado

    # Contador
    # Administrativo
    # Desarrollador
    # Analista Funcional
    # Otro
    JOB_CHOICES =(
        ("0", "Contador"),
        ("1", "Administrativo"),
        ("2", "Desarrollador"),
        ("3", "Analista Funcional"),
        ("4", "Otro")
    ) 

    nombre = models.CharField ("Nombre", max_length=100)
    apellido = models.CharField ("Apellido", max_length=100)
    trabajo = models.CharField ("Puesto", max_length=1, choices=JOB_CHOICES)
    departamento = models.ForeignKey (Departamento, on_delete=models.CASCADE)
    habilidades = models.ManyToManyField (Habilidades)
    fecha_nac = models.DateField('fecha de nacimiento', auto_now=False, auto_now_add=False)
    pais = models.CharField(max_length=100, blank=True) 
    observaciones = RichTextField ()

    

    def __str__(self):
        return f"{self.nombre} - {self.apellido}"

    class Meta:
        verbose_name= "Mi empleado"
        verbose_name_plural = "Empleados de la empresa"
        ordering = ["-nombre", "apellido"]
        unique_together = ("nombre", "departamento")

    def __str__(self):
        return self.nombre + " - " + self.apellido
    
class Tarea(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    fecha_limite = models.DateField()

    def __str__(self):
        return self.nombre

