from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from rest_framework import status

from gestor_cursos.models import Curso, CursoInscrito, Profesor
from gestor_cursos.serializers import CursoSerializer, CursoInscritoSerializer, ProfesorSerializer

# Create your views here.


def inscribir_curso(request):
    curso_inscrito_data = JSONParser().parse(request)
    # valida que el curso exista
    try:
        curso = Curso.objects.get(id_curso=curso_inscrito_data['id_curso'])
    except Curso.DoesNotExist:
        return JsonResponse("El curso no existe", safe=False, status=status.HTTP_400_BAD_REQUEST)

    cursos_inscritos = CursoInscrito.objects.filter(
        documento_estudiante=curso_inscrito_data['documento_estudiante'])

    # valida que el curso no esté inscrito por el mismo estudiante
    cursos_inscritos_repetidos = CursoInscrito.objects.filter(
        id_curso=curso_inscrito_data['id_curso'], documento_estudiante=curso_inscrito_data['documento_estudiante'])
    if cursos_inscritos_repetidos.count() > 0:
        return JsonResponse("Curso ya inscrito", safe=False, status=status.HTTP_400_BAD_REQUEST)

    # Valida que el curso sea de una asignatura que el estudiante no haya ya inscrito
    cursos = Curso.objects.filter(
        id_curso__in=[curso_inscrito.id_curso for curso_inscrito in cursos_inscritos])

    asignaturas_inscritas = [curso.codigo_asignatura for curso in cursos]
    curso = Curso.objects.get(id_curso=curso_inscrito_data['id_curso'])
    if curso.codigo_asignatura in asignaturas_inscritas:
        return JsonResponse("Asignatura ya inscrita", safe=False, status=status.HTTP_400_BAD_REQUEST)

        # valida que cumpla el prerequisito o corequisito
        '''
        prerequisitos = Prerequisito.objects.filter(
            codigo_asignatura=curso.codigo_asignatura)
        for prerequisito in prerequisitos:
            if prerequisito.codigo_asignatura_prerequisito not in asignaturas_cursadas:
                if prerequisito.es_correquisito == 1:
                    if prerequisito.codigo_asignatura_prerequisito not in asignaturas_inscritas:
                        return JsonResponse("El estudiante no cumple con el correquisito", safe=False)
                    else:
                        continue
                return JsonResponse("El estudiante no cumple el prerequisito", safe=False)
        '''
        # valida que el horario no se solape
    solapado = False
    for curso_inscrito in cursos_inscritos:
        curso_temp = Curso.objects.get(
            id_curso=curso_inscrito.id_curso)
        for horario in curso_temp.horarios:
            curso_nuevo = Curso.objects.get(
                id_curso=curso_inscrito_data['id_curso'])
            for horario_nuevo in curso_nuevo.horarios:
                if horario_nuevo['dia'] == horario['dia']:
                    if horario_nuevo['hora_inicio'] >= horario['hora_inicio'] and horario_nuevo['hora_inicio'] < horario['hora_fin']:
                        print(1)
                        solapado = True
                        break
                    if horario_nuevo['hora_fin'] > horario['hora_inicio'] and horario_nuevo['hora_fin'] <= horario['hora_fin']:
                        print(2)

                        solapado = True
                        break
                    if horario_nuevo['hora_inicio'] <= horario['hora_inicio'] and horario_nuevo['hora_fin'] >= horario['hora_fin']:
                        print(3)

                        solapado = True
                        break
    if solapado:
        return JsonResponse("El horario se solapa con otro curso", safe=False, status=status.HTTP_400_BAD_REQUEST)

        # Valida que el curso tenga cupos disponibles
    if curso.cupos_disponibles <= 0:
        return JsonResponse("El curso no tiene cupos disponibles", safe=False, status=status.HTTP_400_BAD_REQUEST)

    curso_inscrito_serializer = CursoInscritoSerializer(
        data=curso_inscrito_data)

    if curso_inscrito_serializer.is_valid():
        curso_inscrito_serializer.save()
        # Actualiza los cupos disponibles del curso
        curso.cupos_disponibles -= 1
        curso.save()
        return JsonResponse("Agregado Correctamente", safe=False)
    return JsonResponse("Fallo al agregar", safe=False, status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
def cursoApi(request, id=0):

    if request.method == 'GET':
        # obtener según el id
        if id != 0:
            try:
                curso = Curso.objects.get(id_curso=id)
                curso_serializer = CursoSerializer(curso)
                return JsonResponse(curso_serializer.data, safe=False)
            except Curso.DoesNotExist:
                return JsonResponse({"id_curso": None}, safe=False, status=status.HTTP_400_BAD_REQUEST)
        cursos = Curso.objects.all()
        cursos_serializer = CursoSerializer(cursos, many=True)
        return JsonResponse(cursos_serializer.data, safe=False)

    elif request.method == 'POST':
        curso_data = JSONParser().parse(request)
        # valida que el curso no exista
        cursos_repetidos = Curso.objects.filter(
            id_curso=curso_data['id_curso'])
        if cursos_repetidos.count() > 0:
            return JsonResponse("El curso ya existe", safe=False, status=status.HTTP_400_BAD_REQUEST)
        curso_serializer = CursoSerializer(data=curso_data)

        if curso_serializer.is_valid():
            curso_serializer.save()
            return JsonResponse("Agregado Correctamente", safe=False)
        return JsonResponse("Fallo al agregar", safe=False, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'PUT':
        curso_data = JSONParser().parse(request)
        curso = Curso.objects.get(id_curso=curso_data['id_curso'])
        curso_serializer = CursoSerializer(curso, data=curso_data)

        if curso_serializer.is_valid():
            curso_serializer.save()
            return JsonResponse("Actualizado Correctamente", safe=False)
        return JsonResponse("Fallo al actualizar", safe=False, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        curso = Curso.objects.get(id_curso=id)
        curso.delete()
        return JsonResponse("Eliminado Correctamente", safe=False)


@csrf_exempt
def cursoInscritoApi(request, id=0):

    if request.method == 'GET':
        # gets the id argument from the url if it has one
        if id != 0:
            cursos_inscritos = CursoInscrito.objects.filter(
                id_curso=id)
        else:
            cursos_inscritos = CursoInscrito.objects.all()
        cursos_inscritos_serializer = CursoInscritoSerializer(
            cursos_inscritos, many=True)
        return JsonResponse(cursos_inscritos_serializer.data, safe=False)

    elif request.method == 'POST':
        return inscribir_curso(request)

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
        # Valida que el profesor no exista
        profesor_repetido = Profesor.objects.filter(
            documento_identidad=profesor_data['documento_identidad'])
        if profesor_repetido.count() > 0:
            return JsonResponse("El profesor ya existe", safe=False, status=status.HTTP_400_BAD_REQUEST)

        profesor_serializer = ProfesorSerializer(data=profesor_data)
        if profesor_serializer.is_valid():
            profesor_serializer.save()
            return JsonResponse("Agregado Correctamente", safe=False)
        return JsonResponse("Fallo al agregar", safe=False, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'PUT':
        profesor_data = JSONParser().parse(request)

        # Valida que el profesor exista
        profesor_repetido = Profesor.objects.filter(
            documento_identidad=profesor_data['documento_identidad'])
        if profesor_repetido.count() == 0:
            return JsonResponse("El profesor no existe", safe=False)
        profesor = Profesor.objects.get(
            documento_identidad=profesor_data['documento_identidad'])
        profesor_serializer = ProfesorSerializer(
            profesor, data=profesor_data)

        if profesor_data['documento_identidad'] == profesor.documento_identidad and profesor_serializer.is_valid():
            profesor_serializer.save()
            return JsonResponse("Actualizado Correctamente", safe=False)
        return JsonResponse("Fallo al actualizar", safe=False, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        profesores = Profesor.objects.all()
        if id not in [profesor.documento_identidad for profesor in profesores]:
            return JsonResponse("El profesor no existe", safe=False, status=status.HTTP_404_NOT_FOUND)
        profesor = Profesor.objects.get(
            documento_identidad=id)
        profesor.delete()
        return JsonResponse("Eliminado Correctamente", safe=False)
