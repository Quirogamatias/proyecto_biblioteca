from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import *
#from .formsets import FormsetAutor

urlpatterns = [  
    path('inicio_alumno/',InicioAlumno.as_view(), name = 'inicio_alumno'),
    path('crear_alumno/',login_required(CrearAlumno.as_view()), name = 'crear_alumno'),
    path('listar_alumnos/',login_required(ListadoAlumnos.as_view()),name = 'listado_alumnos'),
    path('editar_alumno/<int:pk>/',login_required(ActualizarAlumno.as_view()),name = 'editar_alumno'),
    path('eliminar_alumno/<int:pk>/',login_required(EliminarAlumno.as_view()),name = 'eliminar_alumno'),

    path('inicio_administrador/',InicioAdministrador.as_view(), name = 'inicio_administrador'),
    path('crear_administrador/',login_required(CrearAdministrador.as_view()), name = 'crear_administrador'),
    path('listar_administradores/',login_required(ListadoAdministradores.as_view()),name = 'listado_administradores'),
    path('editar_administrador/<int:pk>/',login_required(ActualizarAdministrador.as_view()),name = 'editar_administrador'),
    path('eliminar_administrador/<int:pk>/',login_required(EliminarAdministrador.as_view()),name = 'eliminar_administrador'),

    path('inicio_profesor/',InicioProfesor.as_view(), name = 'inicio_profesor'),
    path('inicio_profesort/',InicioProfesort.as_view(), name = 'inicio_profesort'),
    path('inicio_profesores/',InicioProfesores.as_view(), name = 'inicio_profesores'),
    path('crear_profesor/',login_required(CrearProfesor.as_view()), name = 'crear_profesor'),
    path('listar_profesorest/',login_required(ListadoProfesorest.as_view()),name = 'listado_profesorest'),
    path('listar_profesores/',login_required(ListadoProfesores.as_view()),name = 'listado_profesores'),
    path('estado_profesor/',login_required(EstadoProfesor.as_view()),name = 'estado_profesor'),
    path('editar_profesor/<int:pk>/',login_required(ActualizarProfesor.as_view()),name = 'editar_profesor'),
    path('editar_profesor2/<int:pk>/',login_required(ActualizarProfesor2.as_view()),name = 'editar_profesor2'),
    path('eliminar_profesor/<int:pk>/',login_required(EliminarProfesor.as_view()),name = 'eliminar_profesor'),

    path('inicio_entrega/',InicioEntrega.as_view(), name = 'inicio_entrega'),
    path('crear_entrega_libro/',login_required(CrearEntrega.as_view()), name = 'crear_entrega_libro'),
    path('listar_entrega_libro/',login_required(ListadoEntrega.as_view()),name = 'listado_entrega'),
    path('editar_entrega_libro/<int:pk>/',login_required(ActualizarEntrega.as_view()),name = 'editar_entrega_libro'),
    path('eliminar_entrega_libro/<int:pk>/',login_required(EliminarEntrega.as_view()),name = 'eliminar_entrega_libro'),

    path('inicio_devolucion/',InicioDevolucion.as_view(), name = 'inicio_devolucion'),
    path('crear_devolucion_libro/',login_required(CrearDevolucion.as_view()), name = 'crear_devolucion_libro'),
    path('listar_devolucion_libro/',login_required(ListadoDevolucion.as_view()),name = 'listado_devolucion'),
    path('editar_devolucion_libro/<int:pk>/',login_required(ActualizarDevolucion.as_view()),name = 'editar_devolucion_libro'),
    path('eliminar_devolucion_libro/<int:pk>/',login_required(EliminarDevolucion.as_view()),name = 'eliminar_devolucion_libro'),

    #path('inicio_autor/',InicioAutor.as_view(), name = 'inicio_autor'),
    #path('listar_autor/',login_required(ListadoAutor.as_view()),name = 'listar_autor'),  
    #path('crear_autor/',login_required(CrearAutor.as_view()),name='crear_autor'),    
    #path('editar_autor/<int:pk>/',login_required(ActualizarAutor.as_view()),name='editar_autor'),
    #path('eliminar_autor/<int:pk>/',login_required(EliminarAutor.as_view()),name='eliminar_autor'),
    path('inicio_libro/',InicioLibro.as_view(), name = 'inicio_libro'),
    path('listas_libros/', login_required(ListadoLibros.as_view()), name= 'listado_libros'),
    path('crear_libro/', login_required(CrearLibro.as_view()), name= 'crear_libro'),
    path('editar_libro/<int:pk>/', login_required(ActualizarLibro.as_view()), name= 'editar_libro'),
    path('eliminar_libro/<int:pk>/', login_required(EliminarLibro.as_view()), name= 'eliminar_libro'),
    # URLS GENERALES
    path('reservas/',Reservas.as_view(), name = 'reservas'),
    path('reservas-vencidas/',ReservasVencidas.as_view(), name = 'reservas_vencidas'),
    path('listado-libros-disponibles/',ListadoLibrosDisponibles.as_view(), name = 'listado_libros_disponibles'),
    path('listado-reservas-vencidas/',ListadoReservasVencias.as_view(), name = 'listado_reservas_vencidas'),
    path('listado-libros-reservados/',ListadoLibrosReservados.as_view(), name = 'listado_libros_reservados'),
    path('detalle-libro/<int:pk>/',DetalleLibroDiponible.as_view(), name = 'detalle_libro'),
    path('reservar-libro/',RegistrarReserva.as_view(), name = 'reservar_libro'),
    # FORMSETS
    #path('crear_autor_formset', FormsetAutor.as_view(), name = 'crear_autor_formset')
]
