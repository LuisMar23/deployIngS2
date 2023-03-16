from django.db import models

from app.inventario.models.Producto import Producto

class Egreso(models.Model):
    fecha_registro = models.DateTimeField("Fecha Registro", auto_now_add=True)
    detalle_egresos = models.ManyToManyField(Producto, through='DetalleEgreso')