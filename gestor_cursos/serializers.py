from rest_framework import serializers
from gestor_cursos.models import Curso, Profesor, CursoInscrito


class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = '__all__'


class CursoInscritoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CursoInscrito
        fields = '__all__'


class ProfesorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profesor
        fields = '__all__'
