from django.db import models
# from django.contrib.auth import get_user_model
from .Proveedor import Proveedor
from .Sede import Sede
from app.usuario.models.Usuario import Usuario


class Producto(models.Model):
    nombre = models.CharField("Producto", max_length=200)
    descripcion = models.CharField("Descripcion", max_length=250)
    cantidad = models.PositiveIntegerField("Cantidad")
    preciocompra = models.FloatField("Precio de Compra")
    precioventa = models.FloatField("Precio venta")
    industria = models.CharField("Industria", max_length=50)
    garantia = models.PositiveIntegerField("Garantia")
    marca = models.CharField("Marca", max_length=60)
    imagen = models.ImageField("Imagen", blank=True, null=True, upload_to="productos/")
    estado = models.BooleanField(default=True)
    fecha_registro = models.DateField("Registro", auto_now_add=True)
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    sede = models.ForeignKey(Sede, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        db_table = "producto"
        verbose_name = "Producto"
        ordering = ["fecha_registro"]
        verbose_name_plural = "Productos"

    def __str__(self) -> str:
        return self.nombre
