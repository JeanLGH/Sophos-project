# Generated by Django 4.2.5 on 2023-11-10 14:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ProyectoUno', '0007_rename_correo_electronico_cliente_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='venta',
            name='alquiler',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='ProyectoUno.alquiler'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='juego',
            name='plataforma',
            field=models.CharField(choices=[('Xbox', 'Xbox'), ('PlayStation', 'PlayStation'), ('Nintendo', 'Nintendo'), ('PC', 'PC')], max_length=20),
        ),
    ]
