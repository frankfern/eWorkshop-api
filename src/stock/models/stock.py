from django.db import models

from utils.models import TimeModel


class Brand(TimeModel):

    name = models.CharField(max_length=15)

    def __str__(self):
        return self.name


class DeviceType(TimeModel):

    name = models.CharField(max_length=15)

    def __str__(self):
        return self.name


class DeviceModel(TimeModel):
    DEVICE_TYPE = (
        ('product', 'Producto'),
        ('sparepart', 'Pieza')
    )
    device = models.ForeignKey(DeviceType, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)

    name = models.CharField(max_length=15)
    type_of_sparepart = models.CharField(
        max_length=10, choices=DEVICE_TYPE, null=False, blank=False)

    def __str__(self):
        return self.name


class SparePartType(TimeModel):
    name = models.CharField(max_length=15)
    main_property_value = models.CharField(max_length=10)

    def __str__(self):
        return self.name
