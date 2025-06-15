from django.contrib import admin
from django.urls import path
from applications.empleado.views import IndexView, PruebaListView, ModeloPruebaListView,Listar_todos_los_empleados,Listar_todos_los_empleados_por_departamento,EmpleadoDetailView, TareaCreateView,EliminarTareaView,ListaTareasView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', IndexView.as_view()),
    path('lista/', PruebaListView.as_view()),
    path('lista-prueba/', ModeloPruebaListView.as_view()),
    path('listar_todos_los_empleados/',Listar_todos_los_empleados.as_view()),
    path('listar_por_departamento/<nombres>/',Listar_todos_los_empleados_por_departamento.as_view()),
    path('detalle-empleado/<int:pk>/', EmpleadoDetailView.as_view(), name='detalle-empleado'),
    path('crear-tarea/', TareaCreateView.as_view(), name='crear_tarea'),
    path('tarea/<int:pk>/eliminar/', EliminarTareaView.as_view(), name='eliminar-tarea'),
    path('tareas/', ListaTareasView.as_view(), name='lista-de-tareas'),
]