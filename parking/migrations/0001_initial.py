# Generated by Django 5.1.7 on 2025-03-25 00:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('vehicles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ParkingSpot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('spot_number', models.CharField(max_length=10, unique=True, verbose_name='Número da Vaga')),
                ('is_occupeid', models.BooleanField(default=False, verbose_name='Ocupada')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Atualizado em')),
            ],
            options={
                'verbose_name': 'Vaga',
                'verbose_name_plural': 'Vagas',
            },
        ),
        migrations.CreateModel(
            name='ParkingRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entry_time', models.DateTimeField(auto_now_add=True, verbose_name='Horário de Entrada')),
                ('exit_time', models.DateTimeField(blank=True, null=True, verbose_name='Horário de Saída')),
                ('vehicle', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='parking_records', to='vehicles.vehicle', verbose_name='Veículo')),
                ('parking_spot', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='parking_records', to='parking.parkingspot', verbose_name='Veículo')),
            ],
            options={
                'verbose_name': 'Registro de Estacionamento',
                'verbose_name_plural': 'Registros de Estacionamento',
            },
        ),
    ]
