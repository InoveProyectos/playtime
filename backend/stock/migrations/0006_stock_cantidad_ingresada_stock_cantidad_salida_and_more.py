# Generated by Django 4.0 on 2024-01-24 23:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0005_articulo_lote_articulo_vto'),
    ]

    operations = [
        migrations.AddField(
            model_name='stock',
            name='cantidad_ingresada',
            field=models.PositiveIntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='stock',
            name='cantidad_salida',
            field=models.PositiveIntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='stock',
            name='fecha_ingreso',
            field=models.DateField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='stock',
            name='fecha_salida',
            field=models.DateField(blank=True, default=None, null=True),
        ),
    ]
