from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from gestor_cursos.models import Curso, CursoInscrito, Profesor
from gestor_cursos.serializers import CursoSerializer, CursoInscritoSerializer, ProfesorSerializer

# Create your views here.


@csrf_exempt
def cursoApi(request, id=0):
    if request.method == 'GET':
        cursos = Curso.objects.all()
        cursos_serializer = CursoSerializer(cursos, many=True)
        return JsonResponse(cursos_serializer.data, safe=False)
    elif request.method == 'POST':
        curso_data = JSONParser().parse(request)
        curso_serializer = CursoSerializer(data=curso_data)
        if curso_serializer.is_valid():
            curso_serializer.save()
            return JsonResponse("Agregado Correctamente", safe=False)
        return JsonResponse("Fallo al agregar", safe=False)
    elif request.method == 'PUT':
        curso_data = JSONParser().parse(request)
        curso = Curso.objects.get(id_curso=curso_data['id_curso'])
        curso_serializer = CursoSerializer(curso, data=curso_data)
        if curso_serializer.is_valid():
            curso_serializer.save()
            return JsonResponse("Actualizado Correctamente", safe=False)
        return JsonResponse("Fallo al actualizar", safe=False)
    elif request.method == 'DELETE':
        curso = Curso.objects.get(id_curso=id)
        curso.delete()
        return JsonResponse("Eliminado Correctamente", safe=False)


@csrf_exempt
def cursoInscritoApi(request, id=0):
    if request.method == 'GET':
        cursos_inscritos = CursoInscrito.objects.all()
        cursos_inscritos_serializer = CursoInscritoSerializer(
            cursos_inscritos, many=True)
        return JsonResponse(cursos_inscritos_serializer.data, safe=False)
    elif request.method == 'POST':
        curso_inscrito_data = JSONParser().parse(request)
        curso_inscrito_serializer = CursoInscritoSerializer(
            data=curso_inscrito_data)
        if curso_inscrito_serializer.is_valid():
            curso_inscrito_serializer.save()
            return JsonResponse("Agregado Correctamente", safe=False)
        return JsonResponse("Fallo al agregar", safe=False)
    elif request.method == 'PUT':
        curso_inscrito_data = JSONParser().parse(request)
        curso_inscrito = CursoInscrito.objects.get(
            id_curso_inscrito=curso_inscrito_data['id_curso_inscrito'])
        curso_inscrito_serializer = CursoInscritoSerializer(
            curso_inscrito, data=curso_inscrito_data)
        if curso_inscrito_serializer.is_valid():
            curso_inscrito_serializer.save()
            return JsonResponse("Actualizado Correctamente", safe=False)
        return JsonResponse("Fallo al actualizar", safe=False)
    elif request.method == 'DELETE':
        curso_inscrito = CursoInscrito.objects.get(id_curso_inscrito=id)
        curso_inscrito.delete()
        return JsonResponse("Eliminado Correctamente", safe=False)


@csrf_exempt
def profesorApi(request, id=0):
    if request.method == 'GET':
        profesores = Profesor.objects.all()
        profesores_serializer = ProfesorSerializer(profesores, many=True)
        return JsonResponse(profesores_serializer.data, safe=False)
    elif request.method == 'POST':
        profesor_data = JSONParser().parse(request)
        profesor_serializer = ProfesorSerializer(data=profesor_data)
        if profesor_serializer.is_valid():
            profesor_serializer.save()
            return JsonResponse("Agregado Correctamente", safe=False)
        return JsonResponse("Fallo al agregar", safe=False)
    elif request.method == 'PUT':
        profesor_data = JSONParser().parse(request)
        profesor = Profesor.objects.get(
            documento_identidad=profesor_data['documento_identidad'])
        profesor_serializer = ProfesorSerializer(
            profesor, data=profesor_data)
        if profesor_serializer.is_valid():
            profesor_serializer.save()
            return JsonResponse("Actualizado Correctamente", safe=False)
        return JsonResponse("Fallo al actualizar", safe=False)
    elif request.method == 'DELETE':
        profesor = Profesor.objects.get(
            documento_identidad=id)
        profesor.delete()
        return JsonResponse("Eliminado Correctamente", safe=False)
