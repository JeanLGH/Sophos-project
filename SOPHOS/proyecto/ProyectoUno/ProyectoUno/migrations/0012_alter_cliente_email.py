# Generated by Django 4.2.5 on 2023-11-17 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ProyectoUno', '0011_remove_cliente_juegos_alquilados_venta_codigo_venta'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]
