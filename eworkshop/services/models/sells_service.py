from django.db import models

from .base_service import BaseService


class SellService(BaseService):

    customer = models.ForeignKey(
        'customers.Customer', on_delete=models.CASCADE)
    products = models.ManyToManyField(
        'stock.Product',
        through='services.ServiceProduct',
        through_fields=('service', 'product'),
        serialize=True
    )

    def total_amount(self):
        self.price = sum([
            ptb.quantity_bought * ptb.product.price for ptb in self.products_related()
        ])
        self.save()
        return self.price

    def products_related(self):
        return self.serviceproduct_set.select_related('product')
