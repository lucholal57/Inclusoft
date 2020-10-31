from django.contrib import admin
from inclusoft.models import alumno
from inclusoft.models import datos_adicionales
from inclusoft.models import telefono_urgencia
from inclusoft.models import antecedente_medico
from inclusoft.models import autorizacion_medica
from inclusoft.models import acta_compromiso
# Register your models here.
admin.site.register(alumno)
admin.site.register(datos_adicionales)
admin.site.register(telefono_urgencia)
admin.site.register(antecedente_medico)
admin.site.register(autorizacion_medica)
admin.site.register(acta_compromiso)
