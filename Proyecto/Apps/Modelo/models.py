
from django.db import models

# Create your models here.
"""
 
class Postal(models.Model):
    id = models.AutoField(primary_key=True)
    numero = models.IntegerField()


class Locacion(models.Model):
    id = models.AutoField(primary_key=True)
    ciudad = models.CharField(max_length=15)
    provincia = models.CharField(max_length=15)
    distrito = models.CharField(max_length=15)


class Telefono(models.Model):
    numero = models.CharField(primary_key=True, unique=True, max_length=9)


class Empresa(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    ruc = models.CharField(max_length=8)
    id_locacion = models.ForeignKey('Locacion', on_delete=models.CASCADE)
    telefono = models.ForeignKey('Telefono', on_delete=models.CASCADE)


class categoria_Servicio(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=25)


class Servicio(models.Model):
    id = models.AutoField(primary_key=True)
    id_categoria = models.ForeignKey(
        'categoria_Servicio', on_delete=models.CASCADE)
    id_empresa = models.ForeignKey('Empresa', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    descripcion = models.TextField()


class servicio_Postal(models.Model):
    id_servicio = models.ForeignKey('Servicio', on_delete=models.CASCADE)
    id_postal = models.ForeignKey('Postal', on_delete=models.CASCADE)


class servicio_Empresa(models.Model):
    id_servicio = models.ForeignKey('Servicio', on_delete=models.CASCADE)
    id_empresa = models.ForeignKey('Empresa', on_delete=models.CASCADE)


class Usuario(models.Model):
    ROLES = (
        ("ADMIN", "Admin"),
        ("CLIENT", "Client"),
        ("GERENT", "Gerent"),
    )

    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=16, unique=True)
    contrasena = models.CharField(max_length=16)
    rol = models.CharField(choices=ROLES, default="CLIENT", max_length=16)


class Cliente(models.Model):
    id_usuario = models.ForeignKey(
        'Usuario', on_delete=models.CASCADE)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    telefono = models.ForeignKey('Telefono', on_delete=models.CASCADE)
    id_locacion = models.ForeignKey('Locacion', on_delete=models.CASCADE)
    correo = models.EmailField()


class Admin(models.Model):
    id_usuario = models.ForeignKey('Usuario', on_delete=models.CASCADE)


class Gerente(models.Model):
    nombre = models.CharField(max_length=50)
    id_usuario = models.ForeignKey('Usuario', on_delete=models.CASCADE)
    id_empresa = models.ForeignKey('Empresa', on_delete=models.CASCADE)
    telefono = models.ForeignKey('Telefono', on_delete=models.CASCADE)
    correo = models.EmailField()


class detalle_Contrato(models.Model):
    id = models.AutoField(primary_key=True)
    id_contrato = models.ForeignKey(
        'Contrato', on_delete=models.CASCADE)
    fecha_inicio = models.DateTimeField()
    fecha_fin = models.DateTimeField()
    detalle = models.TextField()
    


class Contrato(models.Model):
    id = models.AutoField(primary_key=True)
    id_cliente = models.ForeignKey('Cliente', on_delete=models.CASCADE)
    id_servicio = models.ForeignKey('Servicio', on_delete=models.CASCADE)
    #id_detalle_contrato = models.ForeignKey(
    #    'detalle_Contrato', on_delete=models.CASCADE)
    fecha_emision = models.DateTimeField()


class Solicitud(models.Model):
    ESTADO = (
        ("INICIADO", "Iniciado"),
        ("PENDIENTE", "Pendiente"),
        ("EN PROCESO", "En Proceso"),
        ("CANCELADO", "Cancelado"),
        ("APROBADO", "Aprobado")
    )

    id = models.AutoField(primary_key=True)
    id_cliente = models.ForeignKey('Cliente', on_delete=models.CASCADE)
    id_servicio = models.ForeignKey('Servicio', on_delete=models.CASCADE)
    status = models.CharField(
        max_length=15, choices=ESTADO, default="INICIADO")


class Pago(models.Model):
    ESTADO = (
        ("PENDIENTE", "Pendiente"),
        ("CANCELADO", "Cancelado"),
    )

    id = models.AutoField(primary_key=True)
    id_contrato = models.ForeignKey('Contrato', on_delete=models.CASCADE)
    monto_total = models.DecimalField(decimal_places=2, max_digits=5)
    status = models.CharField(
        max_length=15, choices=ESTADO, default="PENDIENTE")


class Transaccion(models.Model):
    ESTADO = (
        ("PENDIENTE", "Pendiente"),
        ("CANCELADO", "Cancelado"),
    )
    id = models.AutoField(primary_key=True)
    id_pago = models.ForeignKey('Pago', on_delete=models.CASCADE)
    monto = models.DecimalField(decimal_places=2, max_digits=5)
    status = models.CharField(
        max_length=15, choices=ESTADO, default="PENDIENTE")
    detalle = models.TextField()
"""