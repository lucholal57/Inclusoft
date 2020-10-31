from django.db import models

# Create your models here.
class alumno (models.Model):
 alumno = models.AutoField(primary_key= True)
 nombre = models.CharField(max_length=50)
 apellido = models.CharField(max_length=50)
 dni = models.CharField(max_length=10)
 celular = models.CharField(max_length=20)
 fecha_nacimiento = models.DateField()
 lugar_nacimineto = models.CharField(max_length=50)
 direccion = models.CharField(max_length=50)

 def __str__(self):
    return ("ID: {} NOMBRE: {} APELLIDO: {} DNI: {}".format(self.alumno,self.nombre,self.apellido,self.dni))
    
class datos_adicionales (models.Model): 
   datos = models.AutoField(primary_key= True)
   jubilacion_si = 'SI'
   jubilacion_no = 'NO'
   opciones_jubilacion = [
      (jubilacion_si, 'SI'),
      (jubilacion_no, 'NO'),
   ]
   jubilacion = models.CharField(max_length=10,choices=opciones_jubilacion)
   pension_nacional = 'NACIONAL'
   pension_privincial = 'PROVINCIAL'
   opciones_pension = [
      (pension_nacional, 'NACIONAL'),
      (pension_privincial, 'PROVINCIAL'),
   ]
   pension = models.CharField(max_length=20,choices=opciones_pension)
   cobertura_social = models.CharField(max_length=50)
   certificado_si = 'SI'
   certificado_no = 'NO'
   opciones_certificado = [
      (certificado_si, 'SI'),
      (certificado_no, 'NO'),
   ]
   certificado_discapacidad = models.CharField(max_length=50, choices=opciones_certificado)
   certificado_vigencia = models.DateField(null=True)
   patologia = models.CharField(max_length=50)
   patologias_asociadas = models.CharField(max_length=50)
   nivel_educacional = models.CharField(max_length=50)
   grupo_familiar = models.CharField(max_length=50)
   actividades = models.CharField(max_length=50)
   dias_actividades = models.CharField(max_length=100)
   horario_actividades = models.CharField(max_length=50)
   trabajo_madre = models.CharField(max_length=100)
   trabajo_padre = models.CharField(max_length=100)
   telefono_madre = models.CharField(max_length=50)
   telefono_padre = models.CharField(max_length=50)
   alumno = models.ForeignKey('alumno', on_delete=models.CASCADE ) 


class telefono_urgencia(models.Model):
   tel_urgencia = models.AutoField(primary_key= True)
   nombre_familiar = models.CharField(max_length=50)
   telefono = models.CharField(max_length=20)
   alumno = models.ForeignKey( 'alumno', on_delete=models.CASCADE)

class antecedente_medico(models.Model):
   ant_medico = models.AutoField(primary_key= True)
   grupo_sanguineo = models.CharField(max_length=10)
   factor_rh = models.CharField(max_length=10)
   n_h_c = models.CharField(max_length=10)
   convulsiona_si = 'SI'
   convulsiona_no = 'NO'
   opciones_convulsion = [
      (convulsiona_si, 'SI'),
      (convulsiona_no, 'NO'),
   ]
   convulsiona = models.CharField(max_length=10,choices=opciones_convulsion)
   medicacion_convulsion = models.CharField(max_length=50)
   tipo_convulsion = models.CharField(max_length=50)
   frecuencia = models.CharField(max_length=50)
   doctor_asistente = models.CharField(max_length=50)
   diabetico_si = 'SI'
   diabetico_no = 'NO'
   opciones_diabetico = [
      (diabetico_si, 'SI'),
      (diabetico_no, 'NO'),
   ]
   diabetico = models.CharField(max_length=10,choices=opciones_diabetico)
   medicacion_diabetico = models.CharField(max_length=50)
   observaciones = models.CharField(max_length=100)
   sangrado_nariz_si = 'SI'
   sangrado_nariz_no = 'NO'
   opciones_sangrado_nariz = [
      (sangrado_nariz_si, 'SI'),
      (sangrado_nariz_no, 'NO'),
   ]
   sangrado_nariz = models.CharField(max_length=10,choices=opciones_sangrado_nariz)
   problema_cardiaco_si = 'SI'
   problema_cardiaco_no = 'NO'
   opciones_problema_cardiaco = [
      (problema_cardiaco_si, 'SI'),
      (problema_cardiaco_no, 'NO'),
   ]
   problema_cardiaco = models.CharField(max_length=10,choices=opciones_problema_cardiaco)
   medicacion_cardiaco = models.CharField(max_length=50)
   hipertension_si = 'SI'
   hipertension_no = 'NO'
   opciones_hipertension = [
      (hipertension_si, 'SI'),
      (hipertension_no, 'NO'),
   ]
   problema_hipertension = models.CharField(max_length=10,choices=opciones_hipertension)
   pulmonar_si = 'SI'
   pulmonar_no = 'NO'
   opciones_pulmonar = [
      (pulmonar_si, 'SI'),
      (pulmonar_no, 'NO'),
   ]
   problemas_pulmonar = models.CharField(max_length=10,choices=opciones_pulmonar)
   medicacion_pulmonar = models.CharField(max_length=50)
   asma_si = 'SI'
   asma_no = 'NO'
   opciones_asma = [
      (asma_si, 'SI'),
      (asma_no, 'NO'),
   ]
   asma = models.CharField(max_length=10,choices=opciones_asma)
   desmayos_si = 'SI'
   desmayos_no = 'NO'
   opciones_desmayo = [
      (desmayos_si, 'SI'),
      (desmayos_no, 'NO'),
   ]
   desmayos = models.CharField(max_length=10,choices=opciones_desmayo)
   hernia_si = 'SI'
   hernia_no = 'NO'
   opciones_hernias = [
      (hernia_si, 'SI'),
      (hernia_no, 'NO'),
   ]
   hernias = models.CharField(max_length=10,choices=opciones_hernias)
   micosis_si = 'SI'
   micosis_no = 'NO'
   opciones_micosis = [
      (micosis_si, 'SI'),
      (micosis_no, 'NO'),
   ]
   micosis = models.CharField(max_length=10,choices=opciones_micosis)
   medicacion_micosis = models.CharField(max_length=50)
   comida_ptohibida = models.CharField(max_length=50)
   dieta_especial = models.CharField(max_length=50)
   tratamientos = models.CharField(max_length=50)
   profesionales_tratamientos = models.CharField(max_length=50)
   otra_medicacion = models.CharField(max_length=50)
   conducta_fuga = models.CharField(max_length=50)
   conduta_auto_o_hetero_agrecion = models.CharField(max_length=50)
   alumno = models.ForeignKey( 'alumno', on_delete=models.CASCADE)

class autorizacion_medica(models.Model):
   autorizacion = models.AutoField(primary_key= True)
   medicamento = models.CharField(max_length=50)
   horario = models.CharField(max_length=10)
   dosis = models.CharField(max_length=50)
   alumno = models.ForeignKey( 'alumno', on_delete=models.CASCADE)

class acta_compromiso(models.Model):
   compromiso = models.AutoField(primary_key= True)
   dias = models.CharField(max_length=10)
   ingreso = models.CharField(max_length=50)
   salida = models.CharField(max_length=50)
   traslado_alumno = models.CharField(max_length=50)
   perzonas_autorizadas_retiro = models.CharField(max_length=50)
   dni = models.CharField(max_length=20)
   alumno = models.ForeignKey( 'alumno', on_delete=models.CASCADE)
