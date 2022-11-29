from rest_framework import serializers
from Apps.Modelo.modelos.contrato import Pago
from Apps.Modelo.modelos.usuarios import Usuario

class PagosSerializers(serializers.ModelSerializer):
    class Meta:
        model = Pago
        fields = ('id','id_contrato','monto_total','status')
        #read_only_fields = ('monto_total',)

class LoginSerializers(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields =('nombre','contrasena','rol')