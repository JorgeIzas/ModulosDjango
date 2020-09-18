from django.db import models

# Create your models here.
class ventas(models.Model):
    codigo = models.CharField(max_length = 50)
    direccion = models.CharField(max_length = 45)
    fecha = models.DateTimeField(auto_now = True)
    descuento = models.DecimalField(max_digits = 6, decimal_places = 2)
    estado = models.CharField(max_length = 45)
    total = models.DecimalField(max_digits = 6, decimal_places = 2)
    cliente = models.IntegerField(default = 0)
    repartidor = models.IntegerField(default = 0)
    formadepago = models.IntegerField(default = 0)
