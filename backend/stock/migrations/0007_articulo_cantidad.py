# Generated by Django 4.0 on 2024-01-25 01:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0006_stock_cantidad_ingresada_stock_cantidad_salida_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='articulo',
            name='cantidad',
            field=models.PositiveIntegerField(blank=True, default=0, null=True),
        ),
    ]
