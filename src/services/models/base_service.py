from django.db import models

from utils.models import TimeModel


class BaseService(TimeModel):

    STATUS = (
        ('pending', 'pendiente'),
        ('finished', 'Terminado'),
    )

    worker = models.ForeignKey(
        'staff.Staff', on_delete=models.CASCADE, null=False, blank=False)

    clients_device = models.ForeignKey(
        'customers.CustomerDevice', on_delete=models.CASCADE)

    status = models.CharField(max_length=20, choices=STATUS, default='pending')

    price = models.PositiveIntegerField()

    class Meta:
        abstract = True
