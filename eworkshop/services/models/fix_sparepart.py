from django.db import models
from eworkshop.utils.models import TimeModel


class FixSparepart(TimeModel):
    service = models.ForeignKey(
        'services.FixService', on_delete=models.CASCADE)
    sparepart = models.ForeignKey(
        'stock.Sparepart', on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return 'Fix: {} Sparepart: {} Cant:{}'.format(
            self.service,
            self.sparepart,
            self.quantity
        )
