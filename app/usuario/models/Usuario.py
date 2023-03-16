from django.db import models

from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin

class UsuarioManager(BaseUserManager):
    def create_user(self, username, password=None, **kwargs):
        user = self.model(username=username, **kwargs)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, password=None, **kwargs):
        user = self.create_user(
            username=username, password=password, **kwargs
        )
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user


class Usuario(AbstractBaseUser, PermissionsMixin):
    USERTYPE_CHOICES = (
        ('admin', 'administrador'),
        ('asesor', 'asesor'),
        ('contador', 'contador')
    )
    username = models.CharField("Usuario", max_length=50, unique=True)
    nombre = models.CharField("Nombres", max_length=50)
    apellido = models.CharField("Apellidos", max_length=70)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    usertype = models.CharField(max_length=40, choices=USERTYPE_CHOICES)
    objects = UsuarioManager()
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["nombre", "apellido", "usertype"]

    class Meta:
        db_table = "usuario"

    def __str__(self) -> str:
        return self.username

