from django.db import models
from app.inventory.models import Product


class Sales(models.Model):
    receipt_type = models.CharField("Receipt type", max_length=250)
    serial_number = models.PositiveIntegerField("Serial number")
    sale_price = models.FloatField("Sale price")
    buy_price = models.FloatField("Buy price")
    sale_tax = models.FloatField("Sale tax")
    sale_total = models.FloatField("Sale total")
    is_active = models.BooleanField(default=True)
    date_created = models.DateField("Registration date", auto_now_add=True)
    products = models.ManyToManyField(Product, through="SaleDetail")

    class Meta:
        db_table = "sale"
        verbose_name = "Sale"
        ordering = ["date_created"]
        verbose_name_plural = "Sales"

    def __str__(self) -> str:
        return self.name
