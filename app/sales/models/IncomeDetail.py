from django.db import models
from app.inventory.models import Product
from .Income import Income 


class IncomeDetail(models.Model):
    quantity = models.PositiveIntegerField("quantity")
    amount = models.FloatField("amount")
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    income = models.ForeignKey(Income, on_delete=models.CASCADE)

    class Meta:
        db_table = "income_detail"
        verbose_name = "Income Detail"
        verbose_name_plural = "Income Detail"

    def __str__(self) -> str:
        return self.name
