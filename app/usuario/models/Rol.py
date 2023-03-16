from django.db import models

class Rol(models.Model):
    nombre = models.CharField('Nombre Rol', max_length=50, unique=True)
    descripcion = models.CharField('Descripcion', max_length=100)
    estado = models.BooleanField('Estado', default=True)

    class Meta:
        db_table = 'rol'
    
    def __str__(self) -> str:
        return self.nombre