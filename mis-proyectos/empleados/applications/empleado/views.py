from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView, DeleteView
from django.views.generic.edit import CreateView
from .models import Empleado, Tarea
class IndexView (TemplateView):
    template_name= 'empleado/home.html'

class PruebaListView (ListView):
    template_name = 'empleado/lista.html'
    queryset = ['A','B','C']
    context_object_name = 'lista_prueba'


class ModeloPruebaListView(ListView):
    model = Empleado
    template_name = 'empleado/lista-prueba.html'
    context_object_name = 'lista_prueba'

#lista de todos los empleados de la empresa

class Listar_todos_los_empleados (ListView):
    template_name = 'empleado/listar_todos_los_empleados.html'
    model = Empleado

#lista de todos los empleados que pertenecen a un departamento especifico
class Listar_todos_los_empleados_por_departamento (ListView):
    template_name = 'empleado/listar_todos_los_empleados_por_departamento.html'

    def get_queryset(self):
        departamento = self.kwargs ['nombres']
        lista = Empleado.objects.filter(departamento__nombre=departamento)
        return lista
    context_object_name = 'listar_por_departamento'

class EmpleadoDetailView(DetailView):
    model = Empleado
    template_name = 'empleado/empleado_detail.html'
    
class TareaCreateView(CreateView):
    model = Tarea
    template_name = 'empleado/crear_tarea.html'  
    fields = ['nombre', 'descripcion', 'fecha_limite'] 
    
    def get_success_url(self):
        return '/tareas/'  
    
class EliminarTareaView(DeleteView):
    model = Tarea
    template_name = 'empleado/eliminar_tarea.html' 
    success_url = reverse_lazy('lista-de-tareas') 

class ListaTareasView(ListView):
    model = Tarea
    template_name = 'empleado/lista_tareas.html'
    context_object_name = 'tareas'