from django.contrib import admin
#from .models import *

from .modelos.contrato import *
from .modelos.datosGenerales import *
from .modelos.empresa import *
from .modelos.servicios import *
from .modelos.solicitud import *
from .modelos.usuarios import *
# Register your models here.

admin.site.register(Postal)
admin.site.register(Locacion)
admin.site.register(Telefono)
admin.site.register(Empresa)
admin.site.register(categoria_Servicio)
admin.site.register(Servicio)
admin.site.register(servicio_Postal)
admin.site.register(servicio_Empresa)
admin.site.register(Usuario)
admin.site.register(Cliente)
admin.site.register(Admin)
admin.site.register(Gerente)
admin.site.register(detalle_Contrato)
admin.site.register(Contrato)
admin.site.register(Solicitud)
admin.site.register(Pago)
admin.site.register(Transaccion)
