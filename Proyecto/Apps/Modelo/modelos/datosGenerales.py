from django.db import models


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