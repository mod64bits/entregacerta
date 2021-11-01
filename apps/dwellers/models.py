from django.db import models
from apps.users.models import User


class Block(models):
    block = models.CharField('Bloco', max_length=30)
    created_at = models.DateTimeField('Cadastrado em', auto_now_add=True)
    updated_at = models.DateTimeField('Modificado em', auto_now=True)

    def __str__(self):
        return self.block

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Bloco"
        verbose_name_plural = "Blocos"


class Street(models.Model):
    name = models.CharField('Rua', max_length=100)
    created_at = models.DateTimeField('Cadastrado em', auto_now_add=True)
    updated_at = models.DateTimeField('Modificado em', auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Rua"
        verbose_name_plural = "Ruas"


class Address(models.Model):
    street = models.ForeignKey(Street, on_delete=models.SET_NULL, verbose_name='Rua', related_name='ste_adr')
    block = models.ManyToManyField(Block, on_delete=models.SET_NULL, verbose_name='Bloco', related_name='adr_bloc')
    complement = models.CharField('Complemento', max_length=100, null=True, blank=True)
    number = models.PositiveIntegerField('Número')
    created_at = models.DateTimeField('Cadastrado em', auto_now_add=True)
    updated_at = models.DateTimeField('Modificado em', auto_now=True)

    def __str__(self):
        return f"Rua: {self.street.name}, Bloco: {self.block.block}"

    class Meta:
        ordering = ["-created_at"]
        verbose_name_plural = "Endereços"


class Dwellers(models.Model):
    residents = models.ManyToManyField(User, verbose_name='Moradores',  on_delete=models.SET_NULL,
                                       related_name='user_dwe')
    address = models.ForeignKey(Address, on_delete=models.SET_NULL, verbose_name='Endereço')

    def __str__(self):
        return self.residents.username

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Rua"
        verbose_name_plural = "Ruas"




