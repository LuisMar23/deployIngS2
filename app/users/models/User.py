from django.db import models

from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin


class UserManager(BaseUserManager):
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


class User(AbstractBaseUser, PermissionsMixin):
    USERTYPE_CHOICES = (
        ('admin', 'Administrator'),
        ('assessor', 'Assessor'),
        ('accountant', 'Accountant')
    )
    username = models.CharField("User name", max_length=50, unique=True)
    name = models.CharField("First name", max_length=50)
    last_name = models.CharField("Last name", max_length=70)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    usertype = models.CharField(max_length=40, choices=USERTYPE_CHOICES)
    objects = UserManager()
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["name", "last_name", "usertype"]

    class Meta:
        db_table = "user"

    def __str__(self) -> str:
        return self.username
