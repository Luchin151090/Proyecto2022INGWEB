from django.db import models


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