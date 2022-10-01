from rest_framework import serializers
from asignaturas.models import Asignatura, Programa, Facultad, Sede, Prerequisito, Tipologiaasignatura, Asignatura


class AsignaturaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asignatura
        fields = '__all__'


class FacultadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Facultad
        fields = '__all__'


class PrerequisitoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prerequisito
        fields = '__all__'


class ProgramaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Programa
        fields = '__all__'


class SedeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sede
        fields = '__all__'


class TipologiaasignaturaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tipologiaasignatura
        fields = '__all__'
