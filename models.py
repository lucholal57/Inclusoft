from django.db import models

# Create your models here.
class alumno (models.Model):
 id_alumno = models.CharField(max_length=3)
 nombre = models.CharField(max_length=50)
 apellido = models.CharField(max_length=50)
 dni = models.CharField(max_length=10)
 celular = models.CharField(max_length=20)
 fecha_nacimiento = models.DateField()
 lugar_nacimineto = models.CharField(max_length=50)
 direccion = models.CharField(max_length=50)

 def __str__(self):
    return ("ID: {} NOMBRE: {} APELLIDO: {} DNI: {} CELULAR: {} FEHCA DE NACIMIENTO: {} LUGAR DE NACIMIENTO: {} DIRECCION: {}".format(self.id_alumno,self.nombre,self.apellido,self.dni,self.celular,self.fecha_nacimiento,self.lugar_nacimineto,self.direccion))
    prueba_cambio

      