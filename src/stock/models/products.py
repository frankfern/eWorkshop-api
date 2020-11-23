from django.db import models

from utils.models import StockModel


class Product(StockModel):

    STATE = (
        ('available', 'Disponible'),
        ('out_of_stock', 'Agotado'),
    )

    modelo = models.ForeignKey(
        'stock.DeviceModel', on_delete=models.CASCADE, blank=True)

    state = models.CharField(max_length=30, null=False,
                             choices=STATE, default='disponible')

    def __str__(self):
        return self.modelo.name
