from django.db import models

from app.inventory.models.Product import Product
from .Egreso import Egreso

class DetalleEgreso(models.Model):
    cantidad = models.PositiveIntegerField('Cantidad')
    producto = models.ForeignKey(Product, on_delete=models.CASCADE)
    egreso = models.ForeignKey(Egreso, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'{self.id}'

    class Meta:
        db_table = 'detalle_egreso'
