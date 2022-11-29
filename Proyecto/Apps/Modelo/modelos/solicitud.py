from django.db import models


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