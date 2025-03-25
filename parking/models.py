from django.db import models
from vehicles.models import Vehicle

class ParkingSpot(models.Model):
    spot_number = models.CharField(
        max_length=10, 
        unique=True, 
        verbose_name='Número da Vaga',
    )
    is_occupeid = models.BooleanField(
        default=False,
        verbose_name='Ocupada',
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
        verbose_name = 'Vaga'
        verbose_name_plural = 'Vagas'

    def __str__(self):
        return self.spot_number


class ParkingRecord(models.Model):
    vehicle = models.ForeignKey(
        Vehicle,
        on_delete=models.PROTECT,
        related_name='parking_records',
        verbose_name='Veículo',
    )
    parking_spot = models.ForeignKey(
        ParkingSpot,
        on_delete=models.PROTECT,
        related_name='parking_records',
        verbose_name='Vaga',
    )
    entry_time = models.DateTimeField(
        auto_now_add=True, 
        verbose_name='Horário de Entrada'
    )
    exit_time = models.DateTimeField(
        null=True,
        blank=True,
        verbose_name='Horário de Saída'
    )

    class Meta:
        verbose_name = 'Registro'
        verbose_name_plural = 'Registros'

    def __str__(self):
        return f'{self.vehicle} - {self.parking_spot} - {self.entry_time}'
