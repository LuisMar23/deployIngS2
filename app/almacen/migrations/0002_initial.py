# Generated by Django 4.1.1 on 2023-03-27 23:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("almacen", "0001_initial"),
        ("inventory", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="egreso",
            name="detalle_egresos",
            field=models.ManyToManyField(
                through="almacen.DetalleEgreso", to="inventory.product"
            ),
        ),
        migrations.AddField(
            model_name="detalleegreso",
            name="egreso",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="almacen.egreso"
            ),
        ),
        migrations.AddField(
            model_name="detalleegreso",
            name="producto",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="inventory.product"
            ),
        ),
    ]
