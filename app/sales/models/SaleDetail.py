from django.db import models
from app.inventory.models import Product
from .Sales import Sales


class SaleDetail(models.Model):
    quantity = models.PositiveIntegerField("quantity")
    unit_price = models.FloatField("unit price")
    discount = models.FloatField("discount")
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    sale = models.ForeignKey(Sales, on_delete=models.CASCADE)

    class Meta:
        db_table = "sale_detail"
        verbose_name = "Sale Detail"
        verbose_name_plural = "Sale Detail"

    def __str__(self) -> str:
        return f"Sale detail {self.sale}"
