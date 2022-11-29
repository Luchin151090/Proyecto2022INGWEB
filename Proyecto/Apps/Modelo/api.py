from Apps.Modelo.modelos.contrato import Pago
from Apps.Modelo.modelos.usuarios import Usuario
from rest_framework import viewsets,permissions
from Apps.Modelo.serializers import PagosSerializers
from Apps.Modelo.serializers import LoginSerializers

class PagoViewSet (viewsets.ModelViewSet):
    queryset = Pago.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = PagosSerializers

class LoginViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = LoginSerializers