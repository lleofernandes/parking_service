from django.db import models
from customers.models import Customer


class VehicleType(models.Model):
    name = models.CharField(
        max_length=50, 
        unique=True, 
        verbose_name='Nome',
    )
    description = models.TextField(
        null=True, 
        blank=True, 
        verbose_name='Descrição',
    )

    class Meta:
        verbose_name = 'Tipo de Veículo'
        verbose_name_plural = 'Tipos de Veículos'

    def __str__(self):
        return self.name


class Vehicle(models.Model):
    vehicle_type = models.ForeignKey(
        VehicleType, 
        on_delete=models.PROTECT, 
        null=True,
        blank=True,
        related_name='vehicles',
        verbose_name='Tipo de Veículo',
    )
    licence_plate = models.CharField(
        max_length=10, 
        unique=True, 
        verbose_name='Placa',
    )
    brand = models.CharField(
        max_length=50, 
        null=True,
        blank=True,
        verbose_name='Marca',
    )
    model = models.CharField(
        max_length=50, 
        null=True,
        blank=True,
        verbose_name='Modelo',
    )
    color = models.CharField(
        max_length=50, 
        null=True,
        blank=True,
        verbose_name='Cor',
    )
    owner = models.ForeignKey(
        Customer,
        on_delete=models.PROTECT, 
        null=True,
        blank=True,
        related_name='vehicles',
        verbose_name='Proprietário',
    )
    created_at = models.DateTimeField(
        auto_now_add=True, 
        verbose_name='Criado em'
    )
    updated_at = models.DateTimeField(
        auto_now=True, 
        verbose_name='Atualizado em'
    )

    class Meta:
        verbose_name = 'Veículo'
        verbose_name_plural = 'Veículos'

    def __str__(self):
        return self.licence_plate

