from django.urls import re_path
from gestor_cursos import views

urlpatterns = [
    re_path(r'^cursos$', views.cursoApi),
    re_path(r'^cursos/([0-9]+)$', views.cursoApi),
    re_path(r'^inscripcion$', views.cursoInscritoApi),
    re_path(r'^inscripcion/([a-zA-Z0-9]+)$', views.cursoInscritoApi),
    re_path(r'^profesor$', views.profesorApi),
    # ruta con argumento alfanumérico para el id del profesor
    re_path(r'^profesor/([a-zA-Z0-9]+)$', views.profesorApi),
    # ruta con argumento para el horario del estudiante
    re_path(r'^horario/([a-zA-Z0-9]+)$', views.horarioApi),
]
