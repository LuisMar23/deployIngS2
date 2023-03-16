from django.db import models

class Proveedor(models.Model):
    nombre = models.CharField("Nombre", max_length=150)
    contacto = models.CharField("Contacto", max_length=50)
    correo = models.EmailField("Correo", max_length=30)
    direccion = models.CharField("Direccion", max_length=250)
    estado = models.BooleanField(default=True)
    fecha_registro = models.DateField("Registro", auto_now_add=True)

    class Meta:
        db_table = "proveedor"
        verbose_name = "Proveedor"
        verbose_name_plural = "Proveedores"
        ordering = ["fecha_registro"]

    def __str__(self) -> str:
        return self.nombre