from django.db import models


class Empresa(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    ruc = models.CharField(max_length=8)
    id_locacion = models.ForeignKey('Locacion', on_delete=models.CASCADE)
    telefono = models.ForeignKey('Telefono', on_delete=models.CASCADE)