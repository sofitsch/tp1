from django.db import models

# Create your models here.


class alumno(models.Model):
    nombre_alumno = models.CharField(max_length=30)
    apellido_alumno = models.CharField(max_length=30)
    telefono_alumno = models.IntegerField()

class asignatura(models.Model):
    nombre_asignatura = models.CharField(max_length=30)
    modulos = models.CharField(max_length=30)

class asignatura_de_alumno(models.Model):
    alumno = models.CharField(max_length=30)
    aprobado = models.BooleanField(default=False)

