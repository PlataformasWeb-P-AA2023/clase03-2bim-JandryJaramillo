"""
    Manejo de urls para la aplicación
    administrativo
"""
from django.urls import path
# se importa las vistas de la aplicación
from . import views


urlpatterns = [
        path('', views.index, name='index'),
        path('estudiante/<int:id>', views.obtener_estudiante,
            name='obtener_estudiante'),
        path('telefonos/<int:id>', views.obtener_telefonos,
            name='obtener_telefonos'),
        path('crear/estudiante', views.crear_estudiante,
            name='crear_estudiante'),
        path('editar/estudiante/<int:id>', views.editar_estudiante,
            name='editar_estudiante'),
        path('eliminar/estudiante/<int:id>', views.eliminar_estudiante,
            name='eliminar_estudiante'),
        path('eliminar/telefono/<int:id>', views.eliminar_telefono,
            name='eliminar_telefono'),
 ]
