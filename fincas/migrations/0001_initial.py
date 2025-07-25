# Generated by Django 5.2.4 on 2025-07-19 22:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Finca',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('ubicacion', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Lote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('tamaño_m2', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('descripcion', models.TextField(blank=True)),
                ('finca', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lotes', to='fincas.finca')),
            ],
        ),
    ]
