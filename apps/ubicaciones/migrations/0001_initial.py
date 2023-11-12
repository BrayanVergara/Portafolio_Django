# Generated by Django 4.2.6 on 2023-10-25 23:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lugares',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='Nombre Sucursal')),
                ('address', models.CharField(max_length=250, verbose_name='Dirección')),
                ('lat', models.FloatField(verbose_name='Latitud')),
                ('lng', models.FloatField(verbose_name='Longitud')),
            ],
            options={
                'verbose_name': 'Sucursal',
                'verbose_name_plural': 'Sucursales',
                'ordering': ['name'],
            },
        ),
    ]