from django.urls import re_path
from asignaturas import views

urlpatterns = [
    re_path(r'^asignatura$', views.asignaturaApi),
    re_path(r'^asignatura/([0-9]+)$', views.asignaturaApi),
    re_path(r'^sede$', views.sedeApi),
    re_path(r'^sede/([0-9]+)$', views.sedeApi),
    re_path(r'^facultad$', views.facultadApi),
    re_path(r'^facultad/([0-9]+)$', views.facultadApi),
    re_path(r'^programa$', views.programaApi),
    re_path(r'^programa/([0-9]+)$', views.programaApi),
    re_path(r'^tipologiaasignatura$', views.tipologiaasignaturaApi),
    re_path(r'^tipologiaasignatura/([0-9]+)$', views.tipologiaasignaturaApi),
    re_path(r'^prerequisito$', views.prerequisitoApi),
    re_path(r'^prerequisito/([0-9]+)$', views.prerequisitoApi),
]
