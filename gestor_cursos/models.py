from djongo import models

# Create your models here.

# MODELO DE CURSOS


class Horario(models.Model):
    # Día de la semana de la clase
    dia = models.SmallIntegerField(max_length=1)
    hora_inicio = models.SmallIntegerField()
    hora_fin = models.SmallIntegerField()
    salon = models.CharField(max_length=50)  # Salón de la clase
    documento_profesor = models.CharField(
        max_length=50)  # Profesor de la clase
    # Tipo de clase (lab, teoría, taller, virtual, etc.)
    tipo = models.CharField(max_length=20)

    class Meta:
        abstract = True
        app_label = 'gestor_cursos'


class Curso(models.Model):
    id_curso = models.CharField(max_length=30, primary_key=True)
    codigo_asignatura = models.IntegerField()
    grupo = models.SmallIntegerField()
    horarios = models.ArrayField(
        model_container=Horario
    )
    cupos_disponibles = models.SmallIntegerField()
    cupos_totales = models.SmallIntegerField()

    class Meta:
        app_label = 'gestor_cursos'

# MODELO ASIGNATURA INSCRITA


class CursoInscrito(models.Model):
    id_curso = models.CharField(max_length=30)
    documento_estudiante = models.CharField(max_length=50)

    class Meta:
        app_label = 'gestor_cursos'

# MODELO DE PROFESORES


class Profesor(models.Model):
    documento_identidad = models.CharField(max_length=50, primary_key=True)
    nombre_completo = models.CharField(max_length=100)
    email_institucional = models.EmailField()

    class Meta:
        app_label = 'gestor_cursos'
