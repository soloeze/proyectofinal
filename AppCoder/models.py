from django.db import models

# Create your models here.

class Tarea(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()
    fecha_de_creacion = models.DateField()

    def __str__(self):
        return self.nombre

class Personas_del_equipo(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    edad = models.IntegerField()

    def __str__(self):
        return self.nombre

opciones_consultas = [
    [0,'consulta'],
    [1,'reclamo'],
    [2,'sugerencia'],
    [3,'felicitaciones']
]

class Contacto(models.Model):
    nombre = models.CharField(max_length=50)
    correo = models.EmailField()
    tipo_consulta = models.IntegerField(choices=opciones_consultas)
    mensaje = models.TextField()
    avisos = models.BooleanField()

    def __str__(self):
        return self.nombre