from django.db import models

from app.inventory.models.Product import Product

class Egreso(models.Model):
    fecha_registro = models.DateTimeField("Fecha Registro", auto_now_add=True)
    detalle_egresos = models.ManyToManyField(Product, through='DetalleEgreso')
