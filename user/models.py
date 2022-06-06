from django.db import models

class User(models.Model):
    USER_TYPES = (
        ('SU', 'Super_user'),
        ('RU', 'Regular_user'),
    )
    usertype = models.CharField(max_length=2, choices= USER_TYPES)
    usuario = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    last_login = models.DateField()
    activo = models.BooleanField()
