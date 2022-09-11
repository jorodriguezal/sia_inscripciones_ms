from django.urls import include, re_path
from gestor_cursos import views

urlpatterns = [
    re_path(r'^curso$', views.cursoApi),
    re_path(r'^curso/([0-9]+)$', views.cursoApi),
    re_path(r'^estudiante$', views.estudianteApi),
    re_path(r'^estudiante/([0-9]+)$', views.estudianteApi),
    re_path(r'^profesor$', views.profesorApi),
    re_path(r'^profesor/([0-9]+)$', views.profesorApi),
]
