from django.db import models

class Paquete(models.Model):
    destino = models.CharField(max_length=40)    
    descripcion = models.CharField(max_length=200)   
    dias = models.IntegerField()
    fecha_partida = models.DateField()
    fecha_regreso = models.DateField()
    Image_Set_1 = models.CharField(max_length=30, blank=True)
    Image_Set_2 = models.CharField(max_length=30, blank=True)
    precio_publico = models.FloatField()
    costo = models.FloatField()
    oferta = models.BooleanField()
    activo = models.BooleanField()
