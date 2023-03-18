# Generated by Django 4.1.1 on 2023-03-17 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("inventory", "0002_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="product",
            name="supplier",
        ),
        migrations.AlterField(
            model_name="product",
            name="marca",
            field=models.CharField(
                blank=True, max_length=60, null=True, verbose_name="Marca"
            ),
        ),
    ]