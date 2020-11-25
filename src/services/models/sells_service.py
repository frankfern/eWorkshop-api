from django.db import models

from .base_service import BaseService


class SellService(BaseService):

    customer = models.ForeignKey(
        'customers.Customer', on_delete=models.CASCADE)
    products = models.ManyToManyField('stock.Product')
