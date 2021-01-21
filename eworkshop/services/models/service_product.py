from django.db import models

from eworkshop.utils.models import TimeModel


class ServiceProduct(TimeModel):

    service = models.ForeignKey(
        'services.SellService', on_delete=models.CASCADE)
    product = models.ForeignKey(
        'stock.Product', on_delete=models.CASCADE)
    quantity_bought = models.IntegerField(default=1)

    def __str__(self):
        return 'Compra: {} Product: {} Cant:{}'.format(
            self.service,
            self.product,
            self.quantity_bought
        )
