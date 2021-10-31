from django.db import models


class Adresses(models.Model):
    road = models.CharField('Rua', max_length=50)
    block = models.CharField('Quadra/Bloco', max_length=7)
    number = models.PositiveIntegerField('Numero')
    complement = models.CharField('Complement', max_length=5, help_text='Exemplo "B"', null=True, blank=True)
    reference = models.TextField('Ponto de Referencia', null=True, blank=True)

    def __str__(self):
        return f'Rua: {self.road}, Numero: {str(self.number)}, Bloco/Quadra: {self.block}'

