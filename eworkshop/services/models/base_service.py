from django.db import models
from django.utils import tree

from eworkshop.utils.models import TimeModel


class BaseService(TimeModel):

    worker = models.ForeignKey(
        'staff.Staff', on_delete=models.CASCADE, null=False, blank=False)

    price = models.FloatField(blank=False)

    discount = models.FloatField(blank=True, null=True)

    description = models.CharField(max_length=100, blank=True)

    has_warranty = models.BooleanField(default=False)

    warrantyoff = models.DateField(editable=True, blank=True, null=True)

    class Meta:
        abstract = True
