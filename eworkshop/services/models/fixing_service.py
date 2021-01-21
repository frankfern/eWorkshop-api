from django.db import models

from .base_service import BaseService


class FixService(BaseService):

    STATUS = (
        ('pending', 'pendiente'),
        ('finished', 'Terminado'),
    )

    clients_device = models.ForeignKey(
        'customers.CustomerDevice', on_delete=models.CASCADE)

    service_type = models.ManyToManyField('services.ServiceType')

    description = models.CharField(max_length=100, blank=True)

    status = models.CharField(max_length=20, choices=STATUS, default='pending')

    resources = models.ManyToManyField(
        'stock.Sparepart',
        through='services.FixSparepart',
        through_fields=('service', 'sparepart'))
