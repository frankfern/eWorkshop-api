from django.db import models
from django.core.validators import RegexValidator, validators
from suppliers.models import Supplier


class TimeModel(models.Model):

    """ bla bla vbla"""
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta():
        abstract = True


class BasicInfoModel(TimeModel):
    """ bla bla vbla"""
    phone_regex = RegexValidator(
        regex=r'\+?2?\d{8-15}$',
        message='Phone number must be enteredin format: +5399999999. Upto 15 digits allowed.'
    )

    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    phone = models.CharField(
        validators=[phone_regex], max_length=17, blank=False)
    cellphone = models.CharField(
        validators=[phone_regex], max_length=17, blank=False)

    class Meta():
        abstract = True


class AdvanceInfoModel(BasicInfoModel):
    """ bla bla vbla"""
    ci_regex = '{11}\d$'

    address = models.CharField(max_length=30, null=False, blank=False)
    ci = models.PositiveIntegerField(
        validators=[ci_regex], unique=True, null=False, blank=False)

    class Meta():
        abstract = True


class StockModel(TimeModel):

    CONDITION = (
        ('new', 'Nuevo'),
        ('used', 'De uso')
    )
    description = models.CharField(max_length=100, blank=True)
    sn = models.CharField(max_length=30, null=False, blank=True)
    price = models.FloatField(null=False)
    condition = models.CharField(max_length=30, null=False, choices=CONDITION)
    quantity = models.PositiveIntegerField(null=False)
    supplier = models.ForeignKey(Supplier, on_delete=models.PROTECT, null=True)

    class Meta():
        abstract = True
