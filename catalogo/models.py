from django.db import models
class Producto(models.Model):
    nombre=models.CharField(max_length=30)
    descripcion=models.CharField(max_length=80)
    cantidad=models.IntegerField()
    precio=models.FloatField()

    class Meta:
        db_table='productos'


