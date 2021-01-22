from django.db import models
from eworkshop.utils.models import TimeModel


class FixSparepartManager(models.Manager):

    def create_or_update_quantity(self, service, product, quantity=1):
        object, created = self.get_or_create(
            service=service, product=product
        )
        if not created:
            quantity = object.quantity + (quantity - object.quantity)

        object.update_quantity(quantity)
        return object


class FixSparepart(TimeModel):
    service = models.ForeignKey(
        'services.FixService', on_delete=models.CASCADE)
    sparepart = models.ForeignKey(
        'stock.Sparepart', on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    objects = FixSparepartManager()

    def update_quantity(self, quantity=1):
        self.quantity = quantity
        self.save()

    def __str__(self):
        return 'Fix: {} Sparepart: {} Cant:{}'.format(
            self.service,
            self.sparepart,
            self.quantity
        )
