from django.db import models

from utils.models import TimeModel


class StockModel(TimeModel):

    CONDITION = (
        ('new', 'Nuevo'),
        ('used', 'De uso')
    )
    description = models.CharField(max_length=100, blank=True)
    sn = models.CharField(max_length=30, null=False, blank=True)
    price = models.FloatField(null=False)
    condition = models.CharField(
        max_length=30, null=False, choices=CONDITION, default='new')
    quantity = models.PositiveIntegerField(null=False)
    supplier = models.ForeignKey(
        'suppliers.Supplier', on_delete=models.PROTECT, null=True)

    class Meta():
        abstract = True
