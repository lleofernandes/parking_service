from django.db import models
from django.contrib.auth.models import User

# create database table customer
class Customer(models.Model):
    user = models.OneToOneField(
        User, 
        null=True, 
        blank=True, 
        on_delete=models.PROTECT, #protege contra a exclusão do usuário
        related_name='customer',
        verbose_name='Usuário',
    )
    name = models.CharField(max_length=100, verbose_name='Nome')
    cpf = models.CharField(
        max_length=15, 
        null=True, 
        blank=True, 
        verbose_name='CPF'
    )
    phone = models.CharField(
        max_length=15, 
        null=True, 
        blank=True, 
        verbose_name='Telefone'
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
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'

    def __str__(self):
        return self.name