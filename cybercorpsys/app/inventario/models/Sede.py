from django.db import models

class Sede(models.Model):
    nombre = models.CharField('Sede',max_length=100, unique=True)
    estado = models.BooleanField('Estado', default=True)
    fecha_registro = models.DateTimeField('Date_Created', auto_now_add=True)
    class Meta:
        db_table = 'sede'
        verbose_name = 'Sede'
        verbose_name_plural = 'Sedes'
    def __str__(self):
        return self.nombre
        