from django.db import models


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
