from django.urls import re_path
from gestor_cursos import views

urlpatterns = [
    re_path(r'^curso$', views.cursoApi),
    re_path(r'^curso/([0-9]+)$', views.cursoApi),
    re_path(r'^inscripcion$', views.cursoInscritoApi),
    re_path(r'^inscripcion/([0-9]+)$', views.cursoInscritoApi),
    re_path(r'^profesor$', views.profesorApi),
    re_path(r'^profesor/([0-9]+)$', views.profesorApi),
]
