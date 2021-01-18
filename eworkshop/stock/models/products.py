from django.db import models

from .stock_base_model import StockModel
from eworkshop.services.models import ServiceProduct


class Product(StockModel):

    STATE = (
        ('available', 'Disponible'),
        ('out_of_stock', 'Agotado'),
    )

    state = models.CharField(max_length=30, null=False,
                             choices=STATE, default='disponible')

    def __str__(self):
        return self.device_model.name

    @property
    def used_quantity(self):
        quantity = ServiceProduct.objects.filter(
            product=self.id).aggregate(models.Sum('quantity_bought'))
        return quantity['quantity_bought__sum']

    @property
    def get_real_quantity(self):
        return self.quantity - self.used_quantity
