from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from rest_framework import status

from asignaturas.models import Asignatura, Programa, Facultad, Sede, Prerequisito, Tipologiaasignatura, Asignatura
from asignaturas.serializers import AsignaturaSerializer, FacultadSerializer, PrerequisitoSerializer, ProgramaSerializer, SedeSerializer, TipologiaasignaturaSerializer


def asignaturaApi(request, id=0):
    if request.method == 'GET':
        asignaturas = Asignatura.objects.all()
        asignaturas_serializer = AsignaturaSerializer(asignaturas, many=True)
        return JsonResponse(asignaturas_serializer.data, safe=False)


def facultadApi(request, id=0):
    if request.method == 'GET':
        facultades = Facultad.objects.all()
        facultades_serializer = FacultadSerializer(facultades, many=True)
        return JsonResponse(facultades_serializer.data, safe=False)


def programaApi(request, id=0):
    if request.method == 'GET':
        programas = Programa.objects.all()
        programas_serializer = ProgramaSerializer(programas, many=True)
        return JsonResponse(programas_serializer.data, safe=False)


def tipologiaasignaturaApi(request, id=0):
    if request.method == 'GET':
        tipologias = Tipologiaasignatura.objects.all()
        tipologias_serializer = TipologiaasignaturaSerializer(
            tipologias, many=True)
        return JsonResponse(tipologias_serializer.data, safe=False)


def prerequisitoApi(request, id=0):
    if request.method == 'GET':
        prerequisitos = Prerequisito.objects.all()
        prerequisitos_serializer = PrerequisitoSerializer(
            prerequisitos, many=True)
        return JsonResponse(prerequisitos_serializer.data, safe=False)


def sedeApi(request, id=0):
    if request.method == 'GET':
        sedes = Sede.objects.all()
        sedes_serializer = SedeSerializer(sedes, many=True)
        return JsonResponse(sedes_serializer.data, safe=False)
