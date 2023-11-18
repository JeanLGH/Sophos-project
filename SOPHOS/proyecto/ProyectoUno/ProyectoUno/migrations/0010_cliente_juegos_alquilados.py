# Generated by Django 4.2.5 on 2023-11-11 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ProyectoUno', '0009_juego_stock'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='juegos_alquilados',
            field=models.ManyToManyField(related_name='clientes', through='ProyectoUno.Alquiler', to='ProyectoUno.juego'),
        ),
    ]
