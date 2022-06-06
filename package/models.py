from django.db import models

class Paquete(models.Model):
    destino = models.CharField(max_length=30)    
    descripcion = models.CharField(max_length=30)   
    dias = models.DateField()
    fecha_partida = models.DateField()
    fecha_regreso = models.DateField()
    precio_publico = models.FloatField()
    costo = models.FloatField()
    oferta = models.BooleanField()
    activo = models.BooleanField()
