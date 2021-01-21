from django.db import models

from .stock_base_model import StockModel
from eworkshop.services.models import ServiceProduct


class Product(StockModel):

    @property
    def used_quantity(self):
        quantity = ServiceProduct.objects.filter(
            product=self.id).aggregate(models.Sum('quantity_bought'))
        return quantity['quantity_bought__sum']

    def __str__(self):
        return self.device_model.name
