from django.db import models

from eworkshop.utils.models import TimeModel
from .customers import Customer


class Contact(TimeModel):
    """
    contact with client
    """
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    description = models.CharField(max_length=50, blank=False)

    def _str__(self):
        return self.time
