from django.db import models
from django.db.models.deletion import SET_NULL


class Brand(models.Model):

    name = models.CharField(max_length=15)

    def __str__(self):
        return self.name


class DeviceType(models.Model):

    name = models.CharField(max_length=15)

    def __str__(self):
        return self.name


class Modelo(models.Model):

    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    device = models.ForeignKey(DeviceType, on_delete=models.CASCADE)

    tipe = models.CharField(max_length=15)  # ????
    name = models.CharField(max_length=15)

    def __str__(self):
        return self.name
