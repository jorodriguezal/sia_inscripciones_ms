from django.db import models

# Create your models here.
from django.db import models


class Asignatura(models.Model):
    codigo_asignatura = models.IntegerField(primary_key=True)
    nombre_asignatura = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=50)
    creditos = models.IntegerField()
    id_programa = models.ForeignKey(
        'Programa', models.DO_NOTHING, db_column='id_programa')
    id_tipologia = models.ForeignKey(
        'Tipologiaasignatura', models.DO_NOTHING, db_column='id_tipologia')

    class Meta:
        managed = False
        db_table = 'Asignatura'


class Facultad(models.Model):
    id_facultad = models.IntegerField(primary_key=True)
    nombre_facultad = models.CharField(max_length=50)
    id_sede = models.ForeignKey('Sede', models.DO_NOTHING, db_column='id_sede')

    class Meta:
        managed = False
        db_table = 'Facultad'


class Prerequisito(models.Model):
    id_prerequisito = models.IntegerField(primary_key=True)
    codigo_asignatura = models.ForeignKey(
        Asignatura, models.DO_NOTHING, db_column='codigo_asignatura')
    codigo_asignatura_prerequisito = models.IntegerField(blank=True, null=True)
    es_correquisito = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'Prerequisito'
        app_label = 'asignaturas'


class Programa(models.Model):
    id_programa = models.IntegerField(primary_key=True)
    nombre_programa = models.CharField(max_length=100)
    id_facultad = models.ForeignKey(
        Facultad, models.DO_NOTHING, db_column='id_facultad')

    class Meta:
        managed = False
        db_table = 'Programa'
        app_label = 'asignaturas'


class Sede(models.Model):
    id_sede = models.IntegerField(primary_key=True)
    nombre_sede = models.CharField(max_length=16)

    class Meta:
        managed = False
        db_table = 'Sede'
        app_label = 'asignaturas'


class Tipologiaasignatura(models.Model):
    id_tipologia = models.IntegerField(primary_key=True)
    nombre_tipologia = models.CharField(max_length=16)

    class Meta:
        managed = False
        db_table = 'TipologiaAsignatura'
        app_label = 'asignaturas'
