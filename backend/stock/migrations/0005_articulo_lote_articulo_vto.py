# Generated by Django 4.0 on 2023-12-14 23:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0004_rename_categoria_id_articulo_categoria_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='articulo',
            name='lote',
            field=models.CharField(blank=True, default=None, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='articulo',
            name='vto',
            field=models.DateField(blank=True, default=None, null=True),
        ),
    ]
