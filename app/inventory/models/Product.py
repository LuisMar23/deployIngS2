from django.db import models

from . import Supplier
# from django.contrib.auth import get_user_model
from .BranchOffice import BranchOffice
from app.users.models.User import User


class Product(models.Model):
    name = models.CharField("Product", max_length=200)
    description = models.CharField("Description", max_length=250)
    stock = models.PositiveIntegerField("Stock")
    purchase_price = models.FloatField("Purchase price")
    selling_price = models.FloatField("Selling price")
    industry = models.CharField("Industry", max_length=50)
    assurance_months = models.PositiveIntegerField("Assurance months")
    marca = models.CharField("Marca", max_length=60, null=True, blank=True)
    image = models.ImageField("Imagen", blank=True, null=True, upload_to="productos/")
    bar_code = models.ImageField('Bar code', null=True, upload_to="productos/barcode/")
    is_active = models.BooleanField(default=True)
    date_created = models.DateField("Registration date", auto_now_add=True)
    # supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    branchOffice = models.ForeignKey(BranchOffice, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        db_table = "product"
        verbose_name = "Product"
        ordering = ["date_created"]
        verbose_name_plural = "Products"

    def __str__(self) -> str:
        return self.name
