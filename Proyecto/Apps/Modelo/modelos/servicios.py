from django.db import models


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
