from django.db import models

from eworkshop.utils.models import TimeModel


class BaseStock(TimeModel):

    device_model = models.ForeignKey(
        'stock.DeviceModel', on_delete=models.CASCADE, null=True, blank=True)
    description = models.CharField(max_length=100, blank=True)
    sn = models.CharField(max_length=30, null=False, blank=True)

    class Meta:
        abstract = True


class StockModel(BaseStock):

    CONDITION = (
        ('new', 'Nuevo'),
        ('used', 'De uso')
    )
    price = models.FloatField(null=False)

    condition = models.CharField(
        max_length=30, null=False, choices=CONDITION, default='new')
    quantity = models.PositiveIntegerField(null=False)
    supplier = models.ForeignKey(
        'suppliers.Supplier', on_delete=models.PROTECT, null=True)

    class Meta:
        abstract = True
