from django.db import models

class Compra(models.Model):
    paquete = models.CharField(max_length=40)
    cantidad_pasajeros = models.IntegerField()
    dias = models.IntegerField()
    fecha_partida = models.DateField()
    fecha_regreso = models.DateField()
    fecha_venta = models.DateField(auto_now = True)
    PAYMENT_TYPES = (
        ('TR', 'Transferencia bancaria'),
        ('TC', 'Tarjeta de credito'),
        ('TD', 'Tarjeta de debito'),
        ('MP', 'Mercado Pago'),
    )
    forma_pago = models.CharField(max_length=2, choices=PAYMENT_TYPES)
    activo = models.BooleanField()
