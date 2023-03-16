from django.db import models


class Supplier(models.Model):
    name = models.CharField("Name", max_length=150)
    phone_number = models.CharField("Phone number", max_length=50)
    email_address = models.EmailField("Email address", max_length=30)
    address = models.CharField("Address", max_length=250)
    is_active = models.BooleanField(default=True)
    date_created = models.DateField("Registration date", auto_now_add=True)

    class Meta:
        db_table = "supplier"
        verbose_name = "Supplier"
        verbose_name_plural = "Suppliers"
        ordering = ["date_created"]

    def __str__(self) -> str:
        return self.name
