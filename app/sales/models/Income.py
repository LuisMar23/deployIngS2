from django.db import models
from app.inventory.models import Product, Supplier


class Income(models.Model):
    receipt_type = models.CharField("Receipt type", max_length=250)
    serial_number = models.PositiveIntegerField("Serial number")
    total_amount = models.FloatField("Total amount")
    income_tax = models.FloatField("Income tax")
    is_active = models.BooleanField(default=True)
    date_created = models.DateField("Registration date", auto_now_add=True)
    products = models.ManyToManyField(Product, through="IncomeDetail")
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)

    class Meta:
        db_table = "income"
        verbose_name = "Income"
        ordering = ["date_created"]
        verbose_name_plural = "Incomes"

    def __str__(self) -> str:
        return f"Income {self.receipt_type}"
