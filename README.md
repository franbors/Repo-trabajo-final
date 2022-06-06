# proyectofinal

Empresa de viajes

Tiene 3 apps declaradas:

costumer
package
user

Cada APPS va a crear en la base de datos unas 4 tablas que tienen los siguientes campos


-------------------------
APP costumer
class Cliente(models.Model):
    id_user = models.IntegerField(unique=True)
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    pasaporte = models.IntegerField()
    vencimiento = models.DateField()
    dni = models.IntegerField()
    domicilio = models.CharField(max_length=40)
    telefono = models.IntegerField()

-------------------------
APP package
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

-------------------------
APP user
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




