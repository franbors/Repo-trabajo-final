from django.db import models

class Cliente(models.Model):
    id_user = models.IntegerField(unique=True)
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    pasaporte = models.IntegerField()
    vencimiento = models.DateField()
    dni = models.IntegerField()
    domicilio = models.CharField(max_length=40)
    telefono = models.IntegerField()
